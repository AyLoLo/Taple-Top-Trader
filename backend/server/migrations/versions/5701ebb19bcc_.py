"""empty message

Revision ID: 5701ebb19bcc
Revises: 146576aa4c67
Create Date: 2024-07-25 14:30:00.554360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5701ebb19bcc'
down_revision = '146576aa4c67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('board_game_posts',
    sa.Column('board_game_post_id', sa.Integer(), nullable=False),
    sa.Column('board_game_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['board_game_id'], ['board_games.board_game_id'], name=op.f('fk_board_game_posts_board_game_id_board_games')),
    sa.ForeignKeyConstraint(['post_id'], ['posts.post_id'], name=op.f('fk_board_game_posts_post_id_posts')),
    sa.PrimaryKeyConstraint('board_game_post_id')
    )
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('board_game_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('fk_posts_boardgame_id_board_games', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_posts_board_game_id_board_games'), 'board_games', ['board_game_id'], ['board_game_id'])
        batch_op.drop_column('boardgame_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('boardgame_id', sa.INTEGER(), nullable=False))
        batch_op.drop_constraint(batch_op.f('fk_posts_board_game_id_board_games'), type_='foreignkey')
        batch_op.create_foreign_key('fk_posts_boardgame_id_board_games', 'board_games', ['boardgame_id'], ['board_game_id'])
        batch_op.drop_column('board_game_id')

    op.drop_table('board_game_posts')
    # ### end Alembic commands ###
