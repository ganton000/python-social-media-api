"""Add foreign-key to post table

Revision ID: fc99bb17caaa
Revises: 0ca4580283ee
Create Date: 2022-04-13 10:07:12.949367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc99bb17caaa'
down_revision = '0ca4580283ee'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
    sa.Column('owner_id', sa.Integer(), nullable=False)
    )
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts')
    pass
