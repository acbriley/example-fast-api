"""Add remaining columns to post table

Revision ID: bcd547938423
Revises: 91e68a67a2c0
Create Date: 2022-11-08 14:21:48.507741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcd547938423'
down_revision = '91e68a67a2c0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
