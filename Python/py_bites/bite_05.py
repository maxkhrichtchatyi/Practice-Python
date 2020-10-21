# In this bite you will work with a list of names.
#
# First you will write a function to take out duplicates and title case them.
#
# Then you will sort the list in alphabetical descending order by surname and
# lastly determine what the shortest first name is. For this exercise you can
# assume there is always one name and one surname.

from typing import List

NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names: List[str]) -> List[str]:
    """Should return a list of title cased names, each name appears only once"""
    return list({name.title() for name in names})


def sort_by_surname_desc(names: List[str]) -> List[str]:
    """Returns names list sorted desc by surname"""
    case_names: List[str] = dedup_and_title_case_names(names)
    return sorted(case_names, key=lambda name: name.split()[1], reverse=True)


def shortest_first_name(names: List[str]) -> str:
    """Returns the shortest first name (str). You can assume there is only one shortest name."""
    case_names: List[str] = dedup_and_title_case_names(names)
    fist_names: List[str] = [name.split()[0] for name in case_names]
    return min(fist_names, key=len)
