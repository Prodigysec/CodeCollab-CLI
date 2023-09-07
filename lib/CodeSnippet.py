from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base, session


class CodeSnippet(Base):
    __tablename__ = 'code_snippets'

    snippet_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    code = Column(String, nullable=False)
    description = Column(String)

    user = relationship('User', back_populates='code_snippets')

