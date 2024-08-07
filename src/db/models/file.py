import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class File(Base):
    __tablename__ = 'files'

    file_name: Mapped[str] = mapped_column(
        sa.Text, unique=True, nullable=False
    )
    file_code: Mapped[str] = mapped_column(
        sa.Text, unique=True, nullable=False
    )





