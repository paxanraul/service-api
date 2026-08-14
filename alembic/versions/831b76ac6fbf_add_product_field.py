"""add product field

Revision ID: 831b76ac6fbf
Revises: 6ec60f03fdc3
Create Date: 2026-08-14 17:18:47.016973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '831b76ac6fbf'
down_revision: Union[str, Sequence[str], None] = '6ec60f03fdc3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "products",
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=True,
        ),
    )


def downgrade() -> None:
    op.drop_column("products", "created_at")