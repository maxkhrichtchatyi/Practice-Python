def find_platform(arrival, departure):
    """
    Finds the minimum number of platforms required for a railway Station
    :param arrival: A list of arrival Timing
    :param departure: A list of departure Timing
    :return: Minimum number of platforms required for a railway Station
    """

    arrival_index = 0
    departure_index = 0
    max_index = len(arrival)
    total_number_of_platforms_required = 0
    minimum_number_of_platforms_required = 0

    while arrival_index < max_index and departure_index < max_index:
        if arrival[arrival_index] < departure[departure_index]:
            total_number_of_platforms_required += 1
            arrival_index += 1
        else:
            total_number_of_platforms_required -= 1
            departure_index += 1

        if minimum_number_of_platforms_required < total_number_of_platforms_required:
            minimum_number_of_platforms_required = total_number_of_platforms_required

    return minimum_number_of_platforms_required


if __name__ == "__main__":
    arrival = [900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]

    print(find_platform(arrival, departure))

    arrival = [200, 210, 300, 320, 350, 500]
    departure = [230, 240, 320, 430, 400, 520]

    print(find_platform(arrival, departure))

    arrival = [1100, 1500, 1800, 900, 940, 950]
    departure = [1130, 1900, 2000, 910, 1200, 1120]

    print(find_platform(arrival, departure))
