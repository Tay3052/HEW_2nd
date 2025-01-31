"""empty message

Revision ID: 4155ff013443
Revises: b90ba1ff83da
Create Date: 2023-11-30 17:45:10.196018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4155ff013443'
down_revision = 'b90ba1ff83da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.drop_constraint('user_images_ibfk_2', type_='foreignkey')
        batch_op.create_foreign_key(None, 'conditions', ['condition'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('user_images_ibfk_2', 'colors', ['color'], ['id'])

    # ### end Alembic commands ###
