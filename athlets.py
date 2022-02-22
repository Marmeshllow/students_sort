know_english = ["Vasya", "Jimmy", "Max", "Peter", "Eric", "Zoi", "Felix"]
sportsmen = ["Don", "Peter", "Eric", "Jimmy", "Mark"]
more_than_20_years = ["Peter", "Julie", "Jimmy", "Mark", "Max"]


def find_athlets(lst1, lst2, lst3):
    result = list(set(lst1) & set(lst2) & set(lst3))
    return result
