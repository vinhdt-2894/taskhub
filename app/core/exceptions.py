from http import HTTPStatus

from app.core.messages import PROJECT_NOT_FOUND


class AppError(Exception):
    def __init__(self, status_code: int, detail: str) -> None:
        super().__init__(detail)
        self.status_code = status_code
        self.detail = detail


class ProjectNotFoundError(AppError):
    def __init__(self) -> None:
        super().__init__(HTTPStatus.NOT_FOUND, PROJECT_NOT_FOUND)
