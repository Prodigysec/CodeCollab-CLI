from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .connect import Base, session
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)

    sessions = relationship("ProgrammingSession", backref="user", cascade="all, delete")

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_sessions(self):
        return self.sessions
    


class CodeSnippet(Base):
    __tablename__ = 'code_snippets'

    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False)
    description = Column(String)
    sessions = relationship("ProgrammingSession", backref="code_snippet")

    def __repr__(self):
        return f"<CodeSnippet {self.id}>"
    
    def get_code(self):
        return self.code
    
    def get_description(self):
        return self.description
    
    def get_sessions(self):
        return self.sessions
    


class ProgrammingSession(Base):
    __tablename__ = 'programming_sessions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    code_snippet_id = Column(Integer, ForeignKey('code_snippets.id'), nullable=False)
    start_time = Column(DateTime, default=datetime.datetime.utcnow)
    end_time = Column(DateTime)
    description = Column(String)

    def __repr__(self):
        return f"<ProgrammingSession {self.id}>"
    
    def get_user_id(self):
        return self.user_id
    
    def get_code_snippet(self):
        return self.code_snippet_id
    
    def get_start_time(self):
        return self.start_time
    
    def get_end_time(self):
        return self.end_time
    
    def get_description(self):
        return self.description
    
    def get_user(self):
        return self.user
    
    def get_code_snippet(self):
        return self.code_snippet