know_english = ["Vasya", "Jimmy", "Max", "Peter", "Eric", "Zoi", "Felix"]
sportsmen = ["Don", "Peter", "Eric", "Jimmy", "Mark"]
more_than_20_years = ["Peter", "Julie", "Jimmy", "Mark", "Max"]


def find_athlets():
    english = set(know_english)
    sport = set(sportsmen)
    good_age = set(more_than_20_years)
    return english & sport & good_age


print(find_athlets())
