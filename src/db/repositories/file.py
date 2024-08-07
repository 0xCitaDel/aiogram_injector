"""File repository file."""

from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from bot.structures.role import Role

from ..models import Base, User, File
from .abstract import AbstractRepository


class FileRepo(AbstractRepository[File]):
    """User repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize file repository as for all users or only for one user."""
        super().__init__(model=File, session=session)

