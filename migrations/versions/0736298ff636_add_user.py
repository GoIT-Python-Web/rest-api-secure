"""add user

Revision ID: 0736298ff636
Revises: 3394dd376d9e
Create Date: 2023-02-01 09:35:04.835248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0736298ff636'
down_revision = '3394dd376d9e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('crated_at', sa.DateTime(), nullable=True),
    sa.Column('avatar', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.add_column('notes', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'notes', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.add_column('tags', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_unique_constraint('unique_tag_user', 'tags', ['name', 'user_id'])
    op.create_foreign_key(None, 'tags', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tags', type_='foreignkey')
    op.drop_constraint('unique_tag_user', 'tags', type_='unique')
    op.drop_column('tags', 'user_id')
    op.drop_constraint(None, 'notes', type_='foreignkey')
    op.drop_column('notes', 'user_id')
    op.drop_table('users')
    # ### end Alembic commands ###
