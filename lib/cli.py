from services import UserService, CodeSnippetService, ProgrammingSessionService
def manage_users():
    print("Currently managing Users")
    choice = 1
    

    while choice != 4:
        print("1. List Users")
        print("2. Create Users")
        print("3. Delete User")
        print("4. Back")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            list_users()
        elif choice == 2:
            create_user()
        elif choice == 3:
            delete_user()
        

def list_users():
    print("Listing Users")
    users = UserService.get_users()

    for user in users:
        print(user.get_full_name())

def create_user():
    print("Creating User")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    UserService.create_user(first_name, last_name)
    print(f"Created user")

def delete_user():
    print("Deleting User")
    user_id = input("Enter user id: ")
    UserService.delete_user(user_id)
    print(f"Deleted user")





def manage_code_snippets():
    print("Currently managing Code Snippets")
    choice = 1
    

    while choice != 4:
        print("1. List Code Snippets")
        print("2. Create Code Snippet")
        print("3. Delete Code Snippet")
        print("4. Back")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            list_code_snippets()
        elif choice == 2:
            create_code_snippet()
        elif choice == 3:
            delete_code_snippet()

def list_code_snippets():
    print("Listing Code Snippets")
    code_snippets = CodeSnippetService.get_code_snippets()

    for code_snippet in code_snippets:
        print(code_snippet.get_code())

def create_code_snippet():
    print("Creating Code Snippet")
    code = input("Enter code: ")
    description = input("Enter description: ")
    CodeSnippetService.create_code_snippet(code, description)
    print(f"Created code snippet")


def delete_code_snippet():
    print("Deleting Code Snippet")
    code_snippet_id = input("Enter code snippet id: ")
    CodeSnippetService.delete_code_snippet(code_snippet_id)
    print(f"Deleted code snippet")




def manage_programming_sessions():
    print("Currently managing Programming Sessions")
    choice = 1
    

    while choice != 4:
        print("1. List Programming Sessions")
        print("2. Create Programming Session")
        print("3. Delete Programming Session")
        print("4. Back")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            list_programming_sessions()
        elif choice == 2:
            create_programming_session()
        elif choice == 3:
            delete_programming_session()

def list_programming_sessions():
    print("Listing Programming Sessions")
    programming_sessions = ProgrammingSessionService.get_programming_sessions()

    for programming_session in programming_sessions:
        print(programming_session.get_code_snippet())

def create_programming_session():
    print("Creating Programming Session")
    code_snippet_id = input("Enter code snippet id: ")
    user_id = input("Enter user id: ")
    description = input("Enter description: ")
    ProgrammingSessionService.create_programming_session(int(user_id), int(code_snippet_id), description)
    print(f"Created programming session")

def delete_programming_session():
    print("Deleting Programming Session")
    programming_session_id = input("Enter programming session id: ")
    ProgrammingSessionService.delete_programming_session(programming_session_id)
    print(f"Deleted programming session")
