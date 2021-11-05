"""Add hostname col to windbox

Revision ID: 869252dbae7a
Revises: 453f6242792c
Create Date: 2021-10-23 03:03:07.268815

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '869252dbae7a'
down_revision = '453f6242792c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('windboxes', sa.Column('hostname', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('windboxes', 'hostname')
    # ### end Alembic commands ###
