"""empty message

Revision ID: d0ec047d374c
Revises: 418f36207ef6
Create Date: 2023-11-02 19:10:03.563579

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd0ec047d374c'
down_revision = '418f36207ef6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('category', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('size', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('condition', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('ship', sa.Integer(), nullable=True))
        batch_op.alter_column('explain',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_images', schema=None) as batch_op:
        batch_op.alter_column('explain',
               existing_type=sa.Text(),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.drop_column('ship')
        batch_op.drop_column('condition')
        batch_op.drop_column('size')
        batch_op.drop_column('category')
        batch_op.drop_column('title')

    # ### end Alembic commands ###
