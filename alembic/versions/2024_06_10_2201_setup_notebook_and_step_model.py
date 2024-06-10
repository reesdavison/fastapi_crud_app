"""Setup notebook and step model

Revision ID: 29b763365968
Revises: 
Create Date: 2024-06-10 22:01:03.202253

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "29b763365968"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "notebook",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "notebook_step",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("index", sa.Integer(), nullable=False, unique=True),
        sa.Column("type", sa.String(), nullable=False),
        sa.Column("content", sa.String(), nullable=False),
        sa.Column("notebook_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["notebook_id"],
            ["notebook.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("index"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("notebook_step")
    op.drop_table("notebook")
    # ### end Alembic commands ###