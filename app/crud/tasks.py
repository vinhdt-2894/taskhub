from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import InvalidTaskReferenceError, ProjectNotFoundError
from app.core.messages import (
    TASK_ASSIGNEE_NOT_FOUND,
    TASK_CREATOR_NOT_FOUND,
    TASK_LABELS_OUTSIDE_PROJECT,
)
from app.models.label import Label
from app.models.project import Project
from app.models.task import Task
from app.models.user import User
from app.schemas.task import TaskCreate


async def create_task(db: AsyncSession, project_id: int, data: TaskCreate) -> Task:
    async with db.begin():
        project = await db.get(
            Project, project_id, with_for_update={"read": True, "key_share": True}
        )
        if project is None:
            raise ProjectNotFoundError()

        user_ids = {data.created_by}
        if data.assignee_id is not None:
            user_ids.add(data.assignee_id)
        users = await db.scalars(
            select(User.id)
            .where(User.id.in_(user_ids))
            .order_by(User.id)
            .with_for_update(read=True, key_share=True)
        )
        existing_ids = set(users)
        if data.created_by not in existing_ids:
            raise InvalidTaskReferenceError(TASK_CREATOR_NOT_FOUND)
        if data.assignee_id is not None and data.assignee_id not in existing_ids:
            raise InvalidTaskReferenceError(TASK_ASSIGNEE_NOT_FOUND)

        label_ids = set(data.label_ids)
        labels = []
        if label_ids:
            result = await db.scalars(
                select(Label)
                .where(Label.project_id == project_id, Label.id.in_(label_ids))
                .order_by(Label.id)
                .with_for_update(read=True)
            )
            labels = list(result)
            if len(labels) != len(label_ids):
                raise InvalidTaskReferenceError(TASK_LABELS_OUTSIDE_PROJECT)

        task = Task(
            project_id=project_id,
            labels=labels,
            **data.model_dump(exclude={"label_ids"}),
        )
        db.add(task)
        await db.flush()

    return task
