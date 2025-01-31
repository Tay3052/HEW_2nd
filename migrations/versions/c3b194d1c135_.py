"""empty message

Revision ID: c3b194d1c135
Revises: b6c24d62aff6
Create Date: 2023-11-30 18:08:04.656138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3b194d1c135'
down_revision = 'b6c24d62aff6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sizes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('size', sa.String(length=255), nullable=True))

    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'sizes', ['size'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('sizes', schema=None) as batch_op:
        batch_op.drop_column('size')

    # ### end Alembic commands ###
