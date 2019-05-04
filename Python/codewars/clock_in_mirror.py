"""
Peter can see a clock in the mirror from the place he sits in the office.

When he saw the clock shows 12:22
He knows that the time is 11:38

in the same manner:
05:25 --> 06:35
01:50 --> 10:10
11:58 --> 12:02
12:01 --> 11:59

Please complete the function WhatIsTheTime(timeInMirror),
where timeInMirror is the mirrored time (what Peter sees) as string.

Return the real time as a string.

Consider hours to be between 1 <= hour < 13.
So there is no 00:20, instead it is 12:20.
There is no 13:20, instead it is 01:20.
"""


def what_is_the_time(time_in_mirror):
    hours, minutes = map(int, time_in_mirror.split(':'))

    hours = 12 - hours

    if minutes > 0:
        hours -= 1

    minutes = 60 - minutes

    if hours == 0:
        hours = 12
    elif hours < 0:
        hours = 12 + hours
    elif hours < 10:
        hours = '0' + str(hours)

    if minutes == 60:
        minutes = '00'
    elif minutes < 10:
        minutes = '0' + str(minutes)

    return str(hours) + ':' + str(minutes)


def what_is_the_time_extra(time_in_mirror):
    hours, minutes = map(int, time_in_mirror.split(':'))
    hours += int(minutes != 0)

    return '{:02}:{:02}'.format(-hours % 12 or 12, -minutes % 60)


print('Run the "what_is_the_time" function', end='\n')
print(what_is_the_time("06:35"))

print('Run the "what_is_the_time" function', end='\n')
print(what_is_the_time_extra("12:02"))
