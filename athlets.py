know_english = ["Vasya", "Jimmy", "Max", "Peter", "Eric", "Zoi", "Felix"]
sportsmen = ["Don", "Peter", "Eric", "Jimmy", "Mark"]
more_than_20_years = ["Peter", "Julie", "Jimmy", "Mark", "Max"]


def find_athlets(know_english, sportsmen, more_than_20_years):
    result = list(set(know_english) & set(sportsmen) & set(more_than_20_years))
    return result
