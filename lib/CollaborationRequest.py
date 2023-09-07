from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base, session
 

class CollaborationRequest(Base):
    __tablename__ = 'collaboration_requests'

    request_id = Column(Integer, primary_key=True)
    requester_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    recipient_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    status = Column(String, default='Pending')

