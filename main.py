from datetime import datetime, timedelta
import random
import re

# Task 1 - Calculate the number of days between two dates


def get_days_from_today(date_str):
    today = datetime.today()
    given_date = datetime.strptime(date_str, "%Y-%m-%d")
    return (today - given_date).days


# Task 2 - Generate a list of random numbers


def get_numbers_ticket(min, max, quantity):
    if not (1 <= min < max <= 1000 and min <= quantity <= max):
        return []

    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)


# Task 3 - Normalize phone number


def normalize_phone(phone_number):
    cleaned_number = re.sub(r"[^0-9+]", "", phone_number)

    if cleaned_number.startswith("380"):
        return "+" + cleaned_number

    if cleaned_number.startswith("0"):
        return "+38" + cleaned_number

    if cleaned_number.startswith("+"):
        return cleaned_number

    return "+38" + cleaned_number


# Task 4 - Find upcoming birthdays


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() >= 5:
                congratulation_date += timedelta(
                    days=(7 - congratulation_date.weekday())
                )

            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return upcoming_birthdays
