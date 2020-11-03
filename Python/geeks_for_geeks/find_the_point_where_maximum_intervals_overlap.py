# Consider a big party where a log register for guest’s entry and exit
# times is maintained. Find the time at which there are maximum guests
# in the party. Note that entries in register are not in any order.
#
# Example :
#
# Input: [(1, 4), (2, 5), (9, 12), (5, 9), (5, 12)]
#
# First guest in array arrives at 1 and leaves at 4,
# second guest arrives at 2 and leaves at 5, and so on.
#
# Output: 5
# There are maximum 3 guests at time 5.

guests = [(1, 4), (2, 5), (9, 12), (5, 9), (5, 12)]

arrivals = [_[0] for _ in guests]
exits = [_[1] for _ in guests]

# Sort arrival and exit arrays
arrivals.sort()
exits.sort()

# guests_in indicates number of
# guests at a time
guests_in = 0
max_guests = 0
time = 0
i = 0
j = 0

# Similar to merge in merge sort to
# process all events in sorted order
while i < len(guests) and j < len(guests):

    # If next event in sorted order is
    # arrival, increment count of guests
    if arrivals[i] <= exits[j]:
        guests_in = guests_in + 1

        # Update max_guests if needed
        if guests_in > max_guests:
            max_guests = guests_in
            time = arrivals[i]

        # increment index of arrival array
        i = i + 1

    else:
        guests_in = guests_in - 1
        j = j + 1

print("Maximum Number of Guests =", max_guests, "at time", time)
