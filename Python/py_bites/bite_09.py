# In this Bite you learn how to lookup values from a dictionary or in Python: dict.
#
# You are presented with WORKOUT_SCHEDULE dict (constant) with keys = days and
# values = workouts (or rest up). Complete get_workout_motd that receives a day
# string, title case it so the function can receive case insensitive days, look
# it up in the dict and do two things:
#
# If the day (key) is not in the dictionary, return INVALID_DAY, we don't want
# this function to continue.
# If the key is in the dictionary, return CHILL_OUT or TRAIN depending if it's
# a REST day or not. The latter you will need to string-interpolate using format.
#
# Also check out the docstring and tests. Have fun and keep calm and code in Python!
#
# Update 25th of Nov 2019: previously this Bite required re-raising the KeyError,
# but as that's already the default behavior of a missing key in a dict, we changed
# the requirements to return a value instead.

import pytest

WORKOUT_SCHEDULE = {
    "Friday": "Shoulders",
    "Monday": "Chest+biceps",
    "Saturday": "Rest",
    "Sunday": "Rest",
    "Thursday": "Legs",
    "Tuesday": "Back+triceps",
    "Wednesday": "Core",
}
REST, CHILL_OUT, TRAIN = "Rest", "Chill out!", "Go train {}"
INVALID_DAY = "Not a valid day"


def get_workout_motd(day):
    """First title case the passed in day argument
    (so monday or MONDAY both result in Monday).

    If day is not in WORKOUT_SCHEDULE, return INVALID_DAY

    If day is in WORKOUT_SCHEDULE retrieve the value (workout)
    and return the following:
    - weekday, return TRAIN with the workout value interpolated
    - weekend day (value 'Rest'), return CHILL_OUT

    Examples:
    - if day is Monday -> function returns 'Go train Chest+biceps'
    - if day is Thursday -> function returns 'Go train Legs'
    - if day is Saturday -> function returns 'Chill out!'
    - if day is nonsense -> function returns 'Not a valid day'

    Trivia: /etc/motd is a file on Unix-like systems that contains
    a 'message of the day'
    """
    workout = WORKOUT_SCHEDULE.get(day.title())
    if workout is None:
        return INVALID_DAY
    return CHILL_OUT if workout == REST else TRAIN.format(workout)


# About parametrize: https://pybit.es/pytest-coding-100-tests.html
@pytest.mark.parametrize(
    "day, expected",
    [
        ("Monday", "Go train Chest+biceps"),
        ("monday", "Go train Chest+biceps"),
        ("Tuesday", "Go train Back+triceps"),
        ("TuEsdAy", "Go train Back+triceps"),
        ("Wednesday", "Go train Core"),
        ("wednesdaY", "Go train Core"),
        ("Thursday", "Go train Legs"),
        ("Friday", "Go train Shoulders"),
        ("Saturday", CHILL_OUT),
        ("Sunday", CHILL_OUT),
        ("sundAy", CHILL_OUT),
        ("nonsense", INVALID_DAY),
        ("monday2", INVALID_DAY),
    ],
)
def test_get_workout_valid_case_insensitive_dict_lookups(day, expected):
    assert get_workout_motd(day) == expected
