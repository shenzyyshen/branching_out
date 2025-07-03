def filter_by_age(users, min_age):
    return [user for user in users if user.get("age", 0) >= min_age]