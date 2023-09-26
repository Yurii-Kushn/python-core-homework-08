from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізація домашнього завдання
    birthday_in_monday, birthday_in_tuesday, birthday_in_wednesday, birthday_in_thursday, birthday_in_friday = [], [], [], [], []
    days_name = {
        0: birthday_in_monday,
        1: birthday_in_tuesday,
        2: birthday_in_wednesday,
        3: birthday_in_thursday,
        4: birthday_in_friday,
        5: birthday_in_monday,
        6: birthday_in_monday,
    }
    users_dict = {
        "Monday": birthday_in_monday,
        "Tuesday": birthday_in_tuesday,
        "Wednesday": birthday_in_wednesday,
        "Thursday": birthday_in_thursday,
        "Friday": birthday_in_friday,
    }
    current_datetime = date.today()
    current_day_of_week = current_datetime.weekday()
    if current_day_of_week == 0:
        days_interval = timedelta(days=4)
    elif current_day_of_week == 6:
        days_interval = timedelta(days=5)
    else:
        days_interval = timedelta(days=6)
    end_datetime = current_datetime + days_interval
    for user in users:
        year, month, day = user['birthday'].year, user['birthday'].month, user['birthday'].day
        year = current_datetime.year if month >= current_datetime.month else end_datetime.year
        new_date = datetime(day=day, month=month, year=year).date()
        if current_datetime <= new_date <= end_datetime:
            days_name[new_date.weekday()].append(user['name'])
    users = users_dict.copy()
    for name, value in users_dict.items():
        if not bool(value):
            del_day = users.pop(name)
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print('result:')
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
