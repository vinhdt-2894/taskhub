"""Add unique usernames to users.

Revision ID: 2cb426680626
Revises: a48dbce13852
"""

import sqlalchemy as sa
from alembic import op


revision = "2cb426680626"
down_revision = "a48dbce13852"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("username", sa.String(64), nullable=True))
    op.execute("UPDATE users SET username = 'user-' || id")
    op.alter_column("users", "username", existing_type=sa.String(64), nullable=False)
    op.create_unique_constraint("users_username_key", "users", ["username"])


def downgrade() -> None:
    op.drop_constraint("users_username_key", "users", type_="unique")
    op.drop_column("users", "username")
