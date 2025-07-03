def filter_by_age(users, min_age):

    """Return a list of users whose age is greater or equal to min_age"""

    return [user for user in users if user.get("age", 0) >= min_age]


def filter_by_email(users, email_substring):

    """Returns users whose email contains the given substring
    -users(list of dict) -email_substring (str)
    returns- -list """

    return [user for user in users if email_substring.lower() in user.get("email", "").lower()]

if __name__=="__main__":


    users = [
        {"name": "Alice", "email": "alice@gmail.com", "age": 24},
        {"name": "Bob", "email": "bob@gmail.com", "age": 19},
        {"name": "dylan", "email": "dylan@yahoo.com", "age":49},
    ]

"""filter by age"""
print("Users age 20 and above: ")
result_age = filter_by_age(users, 20)
print(result_age)

"""filter by email"""
print("Users with email containing 'gmail': ")
result_email = filter_by_email(users,"gmail")
print(result_email)