# Given the provided cars dictionary:
#
# Get all Jeeps
# Get the first car of every manufacturer.
# Get all vehicles containing the string Trail in their names (should work for
# other grep too)
# Sort the models (values) alphabetically
#
# See the docstrings and tests for more details. Have fun!
#
# Update 18th of Sept 2018: as concluded in the forum it is better to pass the cars
# dict into each function to make its scope local.

import unittest
from itertools import chain

cars = {
    "Ford": ["Falcon", "Focus", "Festiva", "Fairlane"],
    "Holden": ["Commodore", "Captiva", "Barina", "Trailblazer"],
    "Nissan": ["Maxima", "Pulsar", "350Z", "Navara"],
    "Honda": ["Civic", "Accord", "Odyssey", "Jazz"],
    "Jeep": ["Grand Cherokee", "Cherokee", "Trailhawk", "Trackhawk"],
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
    (original order)"""
    return ", ".join(cars.get("Jeep", ""))


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [manufacturer[0] for manufacturer in cars.values()]


def get_all_matching_models(cars=cars, grep="trail"):
    """return a list of all models containing the case insensitive
    'grep' string which defaults to 'trail' for this exercise,
    sort the resulting sequence alphabetically"""
    models = list(chain.from_iterable(cars.values()))
    return sorted([model for model in models if grep.lower() in model.lower()])


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
    sorted alphabetically"""
    return {manufacturer: sorted(models) for manufacturer, models in cars.items()}


class Test(unittest.TestCase):
    def test_get_all_jeeps(self):
        expected = "Grand Cherokee, Cherokee, Trailhawk, Trackhawk"
        actual = get_all_jeeps()
        assert type(actual) == str
        assert actual == expected

    def test_get_first_model_each_manufacturer(self):
        actual = get_first_model_each_manufacturer()
        expected = ["Falcon", "Commodore", "Maxima", "Civic", "Grand Cherokee"]
        assert actual == expected

    def test_get_all_matching_models_default_grep(self):
        expected = ["Trailblazer", "Trailhawk"]
        assert get_all_matching_models() == expected

    def test_get_all_matching_models_different_grep(self):
        expected = ["Accord", "Commodore", "Falcon"]
        assert get_all_matching_models(grep="CO") == expected

    def test_sort_dict_alphabetically(self):
        actual = sort_car_models()
        # Order of keys should not matter, two dicts are equal if they have the
        # same keys and the same values.
        # The car models (values) need to be sorted here though
        expected = {
            "Ford": ["Fairlane", "Falcon", "Festiva", "Focus"],
            "Holden": ["Barina", "Captiva", "Commodore", "Trailblazer"],
            "Honda": ["Accord", "Civic", "Jazz", "Odyssey"],
            "Jeep": ["Cherokee", "Grand Cherokee", "Trackhawk", "Trailhawk"],
            "Nissan": ["350Z", "Maxima", "Navara", "Pulsar"],
        }
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
