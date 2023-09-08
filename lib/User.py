from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base, session


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer(), primary_key=True)
    username = Column(String(), unique=True, nullable=False)
    availability_status = Column(Boolean, default=True)
    current_task = Column(String())

    collaboration_requests_sent = relationship('CollaborationRequest', foreign_keys='CollaborationRequest.requester_id')
    collaboration_requests_received = relationship('CollaborationRequest', foreign_keys='CollaborationRequest.recipient_id')
    code_snippets = relationship('CodeSnippet', back_populates='user')
    pair_programming_sessions = relationship('PairProgrammingSession', back_populates='participants')

    @classmethod
    def create_user(cls, username, availability_status=True, current_task=None):
        new_user = cls(username=username, availability_status=availability_status, current_task=current_task)
        session.add(new_user)
        session.commit()

    @classmethod
    def get_user_by_id(cls, user_id):
        return session.query(cls).filter_by(user_id=user_id).first()
    
    @classmethod
    def set_availability_status(cls, user_id, status):
        user = cls.get_user_by_id(user_id)
        if user:
            user.availability_status = status
            session.commit()

    @classmethod
    def update_current_task(cls, user_id, task_description):
        user = cls.get_user_by_id(user_id)
        if user:
            user.current_task = task_description
            session.commit()