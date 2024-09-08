"""completed_exercises

Revision ID: cb42d4781f63
Revises: c04b67f4c858
Create Date: 2024-07-19 21:55:41.624345

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cb42d4781f63'
down_revision = 'c04b67f4c858'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('completed_exercises',
    sa.Column('completed_exercise_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('exercise_id', sa.Integer(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('completed_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('answers', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('completed_exercise_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('completed_exercises')
    # ### end Alembic commands ###
