"""'添加user模型类'

Revision ID: 1b31a3b54848
Revises: 
Create Date: 2020-10-08 15:17:00.480516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b31a3b54848'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('source', sa.String(length=64), nullable=False),
    sa.Column('digest', sa.String(length=512), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('clicks', sa.Integer(), nullable=True),
    sa.Column('index_image_url', sa.String(length=256), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('reason', sa.String(length=256), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news')
    op.drop_table('category')
    # ### end Alembic commands ###
