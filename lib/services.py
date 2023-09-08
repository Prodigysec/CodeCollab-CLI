from app.connect import Session
from app.models import User, CodeSnippet, ProgrammingSession
import datetime


class UserService:
    @classmethod
    def get_users(cls):
        session = Session()
        return session.query(User).all()


    @classmethod
    def create_user(cls, first_name, last_name):
        session = Session()
        user = User(first_name=first_name, last_name=last_name)
        session.add(user)
        session.commit()
        # return user
    
    @classmethod
    def update_user(cls, user_id, first_name, last_name):
        session = Session()
        user = session.query(User).get(user_id)
        user.first_name = first_name
        user.last_name = last_name
        session.commit()
        return user 
    
    @classmethod
    def delete_user(cls, user_id):
        session = Session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return user
    
    @classmethod
    def get_user_sessions(cls, user_id):
        session = Session()
        user = session.query(User).get(user_id)
        return user.get_sessions()




class CodeSnippetService:
    @classmethod
    def get_code_snippets(cls):
        session = Session()
        return session.query(CodeSnippet).all()

    @classmethod
    def create_code_snippet(cls, code, description):
        session = Session()
        code_snippet = CodeSnippet(code=code, description=description)
        session.add(code_snippet)
        session.commit()
        return code_snippet
    
    @classmethod
    def update_code_snippet(cls, code_snippet_id, code, description):
        session = Session()
        code_snippet = session.query(CodeSnippet).get(code_snippet_id)
        code_snippet.code = code
        code_snippet.description = description
        session.commit()
        return code_snippet
    
    @classmethod
    def delete_code_snippet(cls, code_snippet_id):
        session = Session()
        code_snippet = session.query(CodeSnippet).get(code_snippet_id)
        session.delete(code_snippet)
        session.commit()
        return code_snippet
    
    @classmethod
    def get_code_snippet_sessions(cls, code_snippet_id):
        session = Session()
        code_snippet = session.query(CodeSnippet).get(code_snippet_id)
        return code_snippet.get_sessions()





class ProgrammingSessionService:
    @classmethod
    def get_programming_sessions(cls):
        session = Session()
        return session.query(ProgrammingSession).all()


    @classmethod
    def create_programming_session(cls, user_id, code_snippet_id, description):
        session = Session()
        programming_session = ProgrammingSession(user_id=user_id, code_snippet_id=code_snippet_id, description=description)
        session.add(programming_session)
        session.commit()
        return programming_session
    
    @classmethod
    def update_programming_session(cls, programming_session_id, user_id, code_snippet_id, description):
        session = Session()
        programming_session = session.query(ProgrammingSession).get(programming_session_id)
        programming_session.user_id = user_id
        programming_session.code_snippet_id = code_snippet_id
        programming_session.description = description
        session.commit()
        return programming_session
    
    @classmethod
    def delete_programming_session(cls, programming_session_id):
        session = Session()
        programming_session = session.query(ProgrammingSession).get(programming_session_id)
        session.delete(programming_session)
        session.commit()
        return programming_session
    
    @classmethod
    def end_programming_session(cls, programming_session_id):
        session = Session()
        programming_session = session.query(ProgrammingSession).get(programming_session_id)
        programming_session.end_time = datetime.datetime.utcnow()
        session.commit()
        return programming_session
    
    @classmethod
    def get_programming_session_user(cls, programming_session_id):
        session = Session()
        programming_session = session.query(ProgrammingSession).get(programming_session_id)
        return programming_session.user
    
    @classmethod
    def get_programming_session_code_snippet(cls, programming_session_id):
        session = Session()
        programming_session = session.query(ProgrammingSession).get(programming_session_id)
        return programming_session.code_snippet
    
    @classmethod
    def get_programming_session_start_time(cls, programming_session_id):
        session = Session()
        programming_session = session.query(ProgrammingSession).get(programming_session_id)
        return programming_session.start_time
    
    @classmethod
    def get_programming_session_end_time(cls, programming_session_id):
        session = Session()
        programming_session = session.query(ProgrammingSession).get(programming_session_id)
        return programming_session.end_time
    
    @classmethod
    def get_programming_session_description(cls, programming_session_id):
        session = Session()
        programming_session = session.query(ProgrammingSession).get(programming_session_id)
        return programming_session.description
