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
    