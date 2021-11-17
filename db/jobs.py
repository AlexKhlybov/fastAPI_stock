from datetime import datetime

from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        Table)

from .base import metadata

jobs = Table(
    "jobs",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, unique=True),
    Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
    Column("title", String),
    Column("description", String),
    Column("salary_from", Integer),
    Column("salary_to", Integer),
    Column("is_active", Boolean),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow),
)
