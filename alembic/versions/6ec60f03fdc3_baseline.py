"""baseline

Revision ID: 6ec60f03fdc3
Revises: 652772b3d436
Create Date: 2026-08-14 17:18:23.247776

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ec60f03fdc3'
down_revision: Union[str, Sequence[str], None] = '652772b3d436'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
