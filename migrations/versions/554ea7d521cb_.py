"""empty message

Revision ID: 554ea7d521cb
Revises: a9f837e1022c
Create Date: 2022-11-19 18:11:50.546385

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '554ea7d521cb'
down_revision = 'a9f837e1022c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('token', 'token',
               existing_type=mysql.VARCHAR(length=230),
               type_=sa.String(length=270),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('token', 'token',
               existing_type=sa.String(length=270),
               type_=mysql.VARCHAR(length=230),
               existing_nullable=False)
    # ### end Alembic commands ###
