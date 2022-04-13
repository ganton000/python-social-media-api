"""Add content column to post table

Revision ID: 2c75792afc31
Revises: e59f2de4f6f3
Create Date: 2022-04-12 23:26:20.261012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c75792afc31'
down_revision = 'e59f2de4f6f3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
