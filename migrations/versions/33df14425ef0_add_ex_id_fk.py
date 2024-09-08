"""add ex id fk

Revision ID: 33df14425ef0
Revises: f868feab8d71
Create Date: 2024-09-08 19:36:18.407087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33df14425ef0'
down_revision = 'f868feab8d71'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'completed_exercises', 'exercises', ['exercise_id'], ['exercise_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'completed_exercises', type_='foreignkey')
    # ### end Alembic commands ###
