from cli import manage_users, manage_code_snippets, manage_programming_sessions

def main():
    choice = 1

    while choice != 4:
        print("1. Users")
        print("2. Code Snippets")
        print("3. Programming Sessions")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            manage_users()
        elif choice == 2:
            manage_code_snippets()
        elif choice == 3:
            manage_programming_sessions()


if __name__ == "__main__":
    main()
