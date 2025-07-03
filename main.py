def filter_by_age(users, min_age):
    """Returns a list of users whose age is greater or equal to min_age"""
    return [user for user in users if user.get("age", 0) >= min_age]

def filter_by_email(users, email_substring):
    """
    Returns users whose email contains the given substring
    -users(list of dict) -email_substring (str)
    returns- -list """

    return [user for user in users if email_substring.lower() in user.get("email", "").lower()]

if __name__=="__main__":
    users = [
        {"name": "Alice", "email": "alice@gmail.com", "age": 35},
        {"name": "Bob", "email": "bob@yahoo.com", "age": 26},
        {"name": "dylan", "email": "dylan@gmail.com", "age":17}
    ]
    print("Users age 20 and above: ")
    result_age = filter_by_age(users, 20)
    print(result_age)

    print("Users with email containing 'gmail':")
    result_email = filter_by_email(users,"gmail")
    print(result_email)