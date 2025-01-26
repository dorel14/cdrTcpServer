"""add description  on event types

Revision ID: 6b4ef429c085
Revises: 4a6d3c1ea7ba
Create Date: 2025-01-25 18:27:08.945351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b4ef429c085'
down_revision = '4a6d3c1ea7ba'
branch_labels = None
depends_on = None

# Surcharge de la méthode create_table pour ajouter if_not_exists=True
_original_create_table = op.create_table
def create_table_with_if_not_exists(*args, **kwargs):
    kwargs['if_not_exists'] = True
    return _original_create_table(*args, **kwargs)
op.create_table = create_table_with_if_not_exists

def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events_types', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events_types', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
