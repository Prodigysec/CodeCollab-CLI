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

    @classmethod
    def create_snippet(cls, user_id, code, description=None):
        """Create a new code snippet and add it to the database."""
        snippet = cls(user_id=user_id, code=code, description=description)
        session.add(snippet)
        session.commit()

    @classmethod
    def get_snippet_by_id(cls, snippet_id):
        """Retrieve a code snippet by its ID."""
        return session.query(cls).filter_by(snippet_id=snippet_id).first()
    
    @classmethod
    def update_snippet(cls, snippet_id, code, description=None):
        """Update a code snippet."""
        snippet = session.query(cls).filter_by(snippet_id=snippet_id).first()
        if snippet:
            snippet.code = code
            snippet.description = description
            session.commit()

    @classmethod
    def delete_snippet(cls, snippet_id):
        """Delete a code snippet."""
        snippet = session.query(cls).filter_by(snippet_id=snippet_id).first()
        if snippet:
            session.delete(snippet)
            session.commit()
    
    @classmethod
    def list_snippets_by_user(cls, user_id):
        """List all code snippets created by a user."""
        return session.query(cls).filter_by(user_id=user_id).all()