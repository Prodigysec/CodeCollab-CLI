from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base, session
 

class CollaborationRequest(Base):
    __tablename__ = 'collaboration_requests'

    request_id = Column(Integer, primary_key=True)
    requester_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    recipient_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    status = Column(String, default='Pending')


    @classmethod
    def send_request(cls, requester_id, recipient_id):
        new_request = cls(requester_id=requester_id, recipient_id=recipient_id, status="Pending")
        session.add(new_request)
        session.commit()

    @classmethod
    def accept_request(cls, request_id):
        request = cls.query.get(request_id)
        if request:
            request.status = "Accepted"
            session.commit()

    @classmethod
    def decline_request(cls, request_id):
        request = cls.query.get(request_id)
        if request:
            request.status = "Declined"
            session.commit()

    @classmethod
    def list_requests_for_user(cls, user_id):
        return session.query(cls).filter_by(recipient_id=user_id).all()
