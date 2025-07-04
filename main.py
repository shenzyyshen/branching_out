from filter_users import filter_users_by_name, filter_users_by_age



if __name__=="__main__":
    filter_option = input("What would you like to filter by? (age or name) ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        try:
            min_age = int(input("Enter minimum age to filter users: ").strip())
            filter_users_by_age(min_age)

        except ValueError:
            print("please enter a valid number.")
    else:
        print("filtering by that option is not yet supported. ")
