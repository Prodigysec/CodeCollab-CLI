from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base, session


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer(), primary_key=True)
    username = Column(String(), unique=True, nullable=False)
    availability_status = Column(Boolean, default=False)
    current_task = Column(String())

    collaboration_requests_sent = relationship('CollaborationRequest', foreign_keys='CollaborationRequest.requester_id')
    collaboration_requests_received = relationship('CollaborationRequest', foreign_keys='CollaborationRequest.recipient_id')
    code_snippets = relationship('CodeSnippet', back_populates='user')
    pair_programming_sessions = relationship('PairProgrammingSession', back_populates='participants')

