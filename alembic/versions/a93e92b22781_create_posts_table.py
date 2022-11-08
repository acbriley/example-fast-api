"""create posts table

Revision ID: a93e92b22781
Revises:
Create Date: 2022-11-08 12:57:54.568712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a93e92b22781'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column(
        'id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False))


def downgrade():
    op.drop_table('posts')
