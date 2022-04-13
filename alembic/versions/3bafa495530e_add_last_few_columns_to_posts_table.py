"""Add last few columns to posts table

Revision ID: 3bafa495530e
Revises: fc99bb17caaa
Create Date: 2022-04-13 10:11:52.534153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bafa495530e'
down_revision = 'fc99bb17caaa'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
    sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts',
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
