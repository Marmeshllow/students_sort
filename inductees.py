names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo"]
birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001]
genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]


def get_inductees(names, birthday_years, genders):
    to_army = []
    clarify = []
    for i in range(len(names)):
        if birthday_years[i] is not None:
            age = 2021 - birthday_years[i]
            if 18 <= age <= 30 and genders[i] == "Male":
                to_army.append(names[i])
            elif 18 <= age <= 30 and genders[i] is None:
                clarify.append(names[i])
        elif birthday_years[i] is None and genders[i] in ('Male', None):
            clarify.append(names[i])
    return to_army, clarify
