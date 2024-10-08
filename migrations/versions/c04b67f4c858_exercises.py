"""exercises

Revision ID: c04b67f4c858
Revises: 2370bb6b0865
Create Date: 2024-07-19 13:13:11.175699

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c04b67f4c858'
down_revision = '2370bb6b0865'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercises',
    sa.Column('exercise_id', sa.Integer(), nullable=False),
    sa.Column('lesson_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('type', sa.VARCHAR(), nullable=True),
    sa.Column('questions', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('exercise_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exercises')
    # ### end Alembic commands ###
