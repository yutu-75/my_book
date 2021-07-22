"""initial1 migration

Revision ID: a0f0f39c7cc1
Revises: 
Create Date: 2021-05-08 14:58:10.557732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0f0f39c7cc1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('b_data',
    sa.Column('name', sa.String(length=255), nullable=True, comment='名称/标题'),
    sa.Column('is_deleted', sa.Boolean(), nullable=True, comment='逻辑删除'),
    sa.Column('orders', sa.Integer(), nullable=True, comment='排序'),
    sa.Column('status', sa.Boolean(), nullable=True, comment='状态(是否显示,是否激活)'),
    sa.Column('created_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('updated_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('img_name', sa.String(length=50), nullable=True, comment='书封面'),
    sa.Column('book_name', sa.String(length=50), nullable=True, comment='书名'),
    sa.Column('author', sa.String(length=50), nullable=True, comment='作者名'),
    sa.Column('book_type', sa.String(length=50), nullable=True, comment='小说类型'),
    sa.Column('book_byte', sa.String(length=255), nullable=True, comment='小说字数'),
    sa.Column('brief_introduction', sa.String(255), nullable=True, comment='小说简介'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('b_text',
    sa.Column('name', sa.String(length=255), nullable=True, comment='名称/标题'),
    sa.Column('is_deleted', sa.Boolean(), nullable=True, comment='逻辑删除'),
    sa.Column('orders', sa.Integer(), nullable=True, comment='排序'),
    sa.Column('status', sa.Boolean(), nullable=True, comment='状态(是否显示,是否激活)'),
    sa.Column('created_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('updated_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('book_chapter', sa.String(length=50), nullable=True, comment='章节名'),
    sa.Column('chapter_text', sa.Text(), nullable=True, comment='章节内容'),
    sa.Column('book_data_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_data_id'], ['b_data.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('b_text')
    op.drop_table('b_data')
    # ### end Alembic commands ###
