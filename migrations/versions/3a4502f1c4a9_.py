"""empty message

Revision ID: 3a4502f1c4a9
Revises: 4ef54b816173
Create Date: 2023-11-08 08:02:05.915471

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3a4502f1c4a9'
down_revision = '4ef54b816173'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.alter_column('explain',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=255),
               existing_nullable=True)
        batch_op.drop_column('ship')
        batch_op.drop_column('title')
        batch_op.drop_column('category')
        batch_op.drop_column('size')
        batch_op.drop_column('price')
        batch_op.drop_column('condition')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.add_column(sa.Column('condition', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('price', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('size', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('category', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('title', mysql.VARCHAR(length=255), nullable=True))
        batch_op.add_column(sa.Column('ship', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.alter_column('explain',
               existing_type=sa.String(length=255),
               type_=mysql.TEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###
