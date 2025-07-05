from filter_users import load_users, filter_users_by_name, filter_users_by_age, filter_by_email

if __name__ == "__main__":
    users = load_users()

    filter_option = input("What would you like to filter by? (name, age, or email): ").strip().lower()

    if filter_option == "name":
        name = input("Enter name to search: ").strip()
        results = filter_users_by_name(users, name)

    elif filter_option == "age":
        try:
            min_age = int(input("Enter minimum age: ").strip())
            results = filter_users_by_age(users, min_age)
        except ValueError:
            print("Invalid age. Please enter a number.")
            result = []
    elif filter_option == "email":
        email_substring = input("Enter part of the email to search for : ").strip()
        results = []
    else:
        print("Unsupported filter options.")
        results = []

        if results:
            for user in results:
                print(user)
        else:
            print("no users found.")


