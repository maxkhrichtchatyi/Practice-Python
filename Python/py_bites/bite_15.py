# Iterate over the given names and countries lists, printing them
# prepending the number of the loop (starting at 1). Here is the
# output you need to deliver:
#
# 1. Julian     Australia
# 2. Bob        Spain
# 3. PyBites    Global
# 4. Dante      Argentina
# 5. Martin     USA
# 6. Rodolfo    Mexico
#
# Notice that the 2nd column should have a fixed width of 11 chars,
# so between Julian and Australia there are 5 spaces, between Bob and
# Spain, there are 8. This column should also be aligned to the left.
#
# Ideally you use only one for loop, but that is not a requirement.

names = "Julian Bob PyBites Dante Martin Rodolfo".split()
countries = "Australia Spain Global Argentina USA Mexico".split()


def enumerate_names_countries() -> None:
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    for id_, (name, country) in enumerate(zip(names, countries), 1):
        mess: str = "{id_:2d}. {name:10s} {country}".format(
            id_=id_, name=name, country=country
        )
        print(mess)
