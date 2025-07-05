import json

def load_users(filepath="users.json"):
    """load users from a json file"""
    with open (filepath, "r") as file:
        return json.load(file)

def filter_users_by_name(users, name):
    """ filter users by exact name match -users(list) -name(str) -returns (list)"""
    return [user for user in users if user.get("name", "").lower() == name.lower()]


def filter_users_by_age(users, min_age):
    """filters users by minimum age."""
    return [user for user in users if user.get("age", 0) >= min_age]

def filter_by_email(users, email_substring):
    """Returns users whose email contains the given substring"""
    return [user for user in users if email_substring.lower() in user.get("email", "").lower()]

if __name__ == "__main__":
    users = load_users()

    filter_option = input("What would you like to filter by? (name, age, email) : ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        results = filter_users_by_name(users, name_to_search)

    elif filter_option == "age":
        try:
            min_age = int(input("Enter a minimum age: ").strip())
            results = filter_users_by_age(users, min_age)
        except ValueError:
            print("Please enter a valid number. ")
            results = []

    elif filter_option == "email":
        substring = input("Enter an email substring to search for: ").strip()
        results = filter_by_email(users, substring)

    else:
        print("Filtering by that option is not yet supported.")
        results = []

    for user in results:
        print(user)
