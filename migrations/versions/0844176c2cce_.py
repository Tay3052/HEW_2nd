"""empty message

Revision ID: 0844176c2cce
Revises: 21039d53045b
Create Date: 2023-12-01 16:35:32.534409

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0844176c2cce'
down_revision = '21039d53045b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categoryname',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('categoryname', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8mb4'
    )
    op.drop_table('categories')
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'colors', ['color'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    op.create_table('categories',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('categoryname')
    # ### end Alembic commands ###
