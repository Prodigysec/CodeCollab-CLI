from faker import Faker
from random import randint

from app.connect import Session
from app.models import User, CodeSnippet, ProgrammingSession


if __name__ == '__main__':
    session = Session()

    session.query(User).delete()
    session.query(CodeSnippet).delete()
    session.query(ProgrammingSession).delete()

    fake = Faker()

    users = []
    for _ in range(10):
        user = User(first_name=fake.first_name(),
            last_name=fake.last_name(),
        )
        users.append(user)
        session.add(user)
        session.commit()

    code_snippets = []

    for _ in range(10):
        code_snippet = CodeSnippet(code=fake.text(),
            description=fake.text(),
        )
        code_snippets.append(code_snippet)
        session.add(code_snippet)
        session.commit()

    for _ in range(10):
        session.add(ProgrammingSession(user_id=randint(1, 10),
            code_snippet_id=randint(1, 10),
            start_time=fake.date_time(),
            end_time=fake.date_time(),
            description=fake.text(),
        ))
        session.commit()
    
