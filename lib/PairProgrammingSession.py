from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base, session
import datetime


class PairProgrammingSession(Base):
    __tablename__ = 'pair_programming_sessions'

    session_id = Column(Integer, primary_key=True)
    user1_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    user2_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    start_time = Column(DateTime, default=datetime.datetime.utcnow)
    end_time = Column(DateTime)
    description = Column(String)

    participants = relationship('User', secondary='pair_programming_sessions', back_populates='pair_programming_sessions')

    @classmethod
    def create_session(cls, user1_id, user2_id, description=None):
        """Create a new pair programming session."""
        session = cls(user1_id=user1_id, user2_id=user2_id, description=description)
        session.start_time = datetime.datetime.utcnow()
        session.end_time = None
        session.commit()

    @classmethod
    def end_session(cls, session_id):
        """End pair programming session."""
        session_to_end = session.query(cls).filter_by(session_id=session_id).first()
        if session_to_end:
            session_to_end.end_time = datetime.datetime.utcnow()
            session.commit()

    @classmethod
    def list_sessions_by_user(cls, user_id):
        """List all pair programming sessions related to a user."""
        sessions = session.query(cls).filter((cls.user1_id == user_id) | (cls.user2_id == user_id)).all()
        return sessions
