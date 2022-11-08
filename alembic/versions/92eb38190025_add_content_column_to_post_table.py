"""Add content column to post table

Revision ID: 92eb38190025
Revises: a93e92b22781
Create Date: 2022-11-08 13:13:36.446388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92eb38190025'
down_revision = 'a93e92b22781'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
