from typing import Optional
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo
from app import db

class User(db.Model):
	id: sqlo.Mapped[int] = sqlo.mapped_column(primary_key = True)
	username: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(64), index = True, unique = True)
	email: sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(120), index = True, unique = True)
	password_hash: sqlo.Mapped[Optional[str]] = sqlo.mapped_column(sqla.String[256])
	
	def __repr__(self):
		return '<User {}>'.format(self.username)