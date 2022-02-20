import datetime
names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo"]
birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001]
genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]


def get_inductees(name_list, b_years, gender_list):
    now = datetime.datetime.now()
    to_army = []
    clarify = []
    for i in range(len(name_list)):
        if b_years[i] is not None:
            age = now.year - b_years[i]
            if 18 <= age <= 30 and gender_list[i] == "Male":
                to_army.append(name_list[i])
            elif 18 <= age <= 30 and gender_list[i] is None:
                clarify.append(name_list[i])
        elif b_years[i] is None and gender_list[i] in ('Male', None):
            clarify.append(name_list[i])
    return to_army, clarify


to_army, clarify = get_inductees(names, birthday_years, genders)
print(to_army, clarify)
