import subprocess
import json

def get_bootstrap_server():
    """Gets the bootstrap server address from the user."""
    while True:
        try:
            bootstrap_server = input("Enter bootstrap server address (e.g., kafka1:29092): ")
            # Basic validation (can be more robust)
            if ":" in bootstrap_server:
                break
            else:
                print("Invalid format. Please enter in the format 'hostname:port'.")
        except KeyboardInterrupt:
            print("\nExiting...")
            exit(0)
    return bootstrap_server

def create_user_group():
    """Creates a new user group."""
    group_name = input("Enter the group name: ")
    # (You might want to add logic here to check if the group already exists)
    print(f"User group '{group_name}' created.")

def create_user():
    """Creates a new user within a group."""
    group_name = input("Enter the group name: ")
    user_name = input("Enter the user name: ")
    # (You might want to add logic here to check if the user already exists)
    print(f"User '{user_name}' created in group '{group_name}'.")

def print_topic_list():
    """Prints a list of topics with unique IDs."""
    # Replace with your actual topic listing logic 
    # This is a simplified example
    topic_list = [
        {"id": 1, "name": "test1"},
        {"id": 2, "name": "test2"},
        {"id": 3, "name": "test3"}
    ]
    for topic in topic_list:
        print(f"ID: {topic['id']}, Name: {topic['name']}")

def define_topic_access():
    """Defines topic access permissions for users."""
    access_rules = {}
    while True:
        try:
            user_access = input("Enter user access rule (e.g., username-1rwed or usernameN): ")
            if not user_access:
                break
            user, access_str = user_access.split("-") if "-" in user_access else (user_access, "")
            if access_str:
                access_rules[user] = access_str
            else:
                if user.endswith("N"):
                    access_rules[user[:-1]] = "N"  # Cannot create topic
                elif user.endswith("C"):
                    access_rules[user[:-1]] = "C"  # Can create topic
        except KeyboardInterrupt:
            print("\nExiting...")
            break
    # (You would then need to implement logic to apply these access rules)
    print("Topic access rules defined.")

def main():
    bootstrap_server = get_bootstrap_server()

    while True:
        print("\nMenu:")
        print("[0]. Configuration: get bootstrap server name")
        print("[1]. Create user group")
        print("[2]. Create user")
        print("[3]. Print topic list by unique ID")
        print("[4]. Define topics and user access")
        print("[5]. Set creation topic access for user")
        print("[q]. Quit")

        choice = input("Enter your choice: ")

        if choice == "0":
            bootstrap_server = get_bootstrap_server()
        elif choice == "1":
            create_user_group()
        elif choice == "2":
            create_user()
        elif choice == "3":
            print_topic_list()
        elif choice == "4":
            define_topic_access()
        elif choice == "5":
            define_topic_access()  # Reuse for creation topic access
        elif choice == "q":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()