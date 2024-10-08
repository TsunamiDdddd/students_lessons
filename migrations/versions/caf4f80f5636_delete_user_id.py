"""delete user id

Revision ID: caf4f80f5636
Revises: e59ce8e0973b
Create Date: 2024-09-08 19:31:27.450850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caf4f80f5636'
down_revision = 'e59ce8e0973b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('completed_exercises', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('completed_exercises', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
