from collections import deque


def find_platform(arrival, departure):
    """
    Finds the minimum number of platforms required for a railway Station
    :param arrival: A list of arrival Timing
    :param departure: A list of departure Timing
    :return: Minimum number of platforms required for a railway Station
    """

    platforms = deque()
    minimum_number_of_platforms_required = 0

    arrival.sort()
    departure.sort()

    for index in range(len(arrival)):
        if len(platforms) == 0:
            platforms.append(departure[index])
        elif platforms[0] <= arrival[index]:
            platforms.popleft()
            platforms.append(departure[index])
        else:
            platforms.append(departure[index])

        if len(platforms) > minimum_number_of_platforms_required:
            minimum_number_of_platforms_required = len(platforms)

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
