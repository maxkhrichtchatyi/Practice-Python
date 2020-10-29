# Write a generator that returns the following "special" dates
# (datetime objects) for PyBites:
#
# - Our birthday! What is the date every year going forward from the
# PYBITES_BORN date (datetime.datetime(2017, 12, 19, 0, 0),
# datetime.datetime(2018, 12, 19, 0, 0), ...)?
#
# - Return every 100th day counting forward from the PYBITES_BORN
# date (datetime(2017, 3, 29, 0, 0), datetime(2017, 7, 7, 0, 0), ...)

from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    cur_bd = PYBITES_BORN
    new_100_days = PYBITES_BORN

    while True:
        new_100_days += timedelta(days=100)

        if new_100_days > cur_bd.replace(year=cur_bd.year + 1):
            cur_bd = cur_bd.replace(year=cur_bd.year + 1)
            yield cur_bd
        yield new_100_days
