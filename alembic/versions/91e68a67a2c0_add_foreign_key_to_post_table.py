"""add foreign key to post table

Revision ID: 91e68a67a2c0
Revises: efd5a462343d
Create Date: 2022-11-08 14:13:41.135966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91e68a67a2c0'
down_revision = 'efd5a462343d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts",
                          referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
