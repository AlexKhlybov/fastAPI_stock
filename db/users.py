from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Table

from .base import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, unique=True),
    Column("email", String, primary_key=True, unique=True),
    Column("name", String),
    Column("hashed_password", String),
    Column("is_company", Boolean),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow),
)
