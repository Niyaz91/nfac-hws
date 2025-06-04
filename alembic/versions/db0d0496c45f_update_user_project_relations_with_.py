"""Update user-project relations with cascade

Revision ID: db0d0496c45f
Revises: ea9d7afd4896
Create Date: 2025-06-03 09:51:51.335198

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import enum

# revision identifiers, used by Alembic.
revision: str = 'db0d0496c45f'
down_revision: Union[str, None] = 'ea9d7afd4896'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

class RoleEnum(str, enum.Enum):
    OWNER = "owner"
    MEMBER = "member"

def upgrade() -> None:
    op.execute("""
    DO $$
    BEGIN
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'roleenum') THEN
            CREATE TYPE roleenum AS ENUM ('OWNER', 'MEMBER');
        END IF;
    END$$;
    """)

def downgrade() -> None:
    op.execute("""
    DO $$
    BEGIN
        IF EXISTS (SELECT 1 FROM pg_type WHERE typname = 'roleenum') THEN
            DROP TYPE roleenum;
        END IF;
    END$$;
    """)