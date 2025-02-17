"""Initial migration

Revision ID: edb56d9d046e
Revises: 6139171d57af
Create Date: 2025-01-21 13:35:02.583946

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'edb56d9d046e'
down_revision: Union[str, None] = '6139171d57af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('mobile', sa.Integer(), nullable=True))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('users', 'mobile')
    # ### end Alembic commands ###
