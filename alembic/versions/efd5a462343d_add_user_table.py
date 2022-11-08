"""Add user table

Revision ID: efd5a462343d
Revises: 92eb38190025
Create Date: 2022-11-08 13:29:30.125148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efd5a462343d'
down_revision = '92eb38190025'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
