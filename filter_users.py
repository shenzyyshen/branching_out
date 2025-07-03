
def filter_by_email(users, email_substring):
    """
    Returns users whose email contains the given substring
    -users(list of dict) -email_substring (str)
    returns- -list """

    return [user for user in users if email_substring.lower() in user.get("email", "").lower()]

if __name__=="__main__":
    users = [
        {"name": "Alice", "email": "alice@gmail.com"},
        {"name": "Bob", "email": "bob@gmail.com"},
        {"name": "dylan", "email": "dylan@gmail.com"},
    ]

    result = filter_by_email(users,"gmail")
    print(result)