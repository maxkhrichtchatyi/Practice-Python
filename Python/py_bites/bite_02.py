# Learn Python regular expressions by writing the following
# 3 functions.
#
# In each function's docstring we show the expected result.
#
# The tests verify these expected results when you hit Save + Verify.
# We will do a more ample regex bite later on.
# Note that for parsing HTML you would use a library of some sort,
# this is just to train your regex skills.

import re

COURSE = (
    "Introduction 1 Lecture 01:47"
    "The Basics 4 Lectures 32:03"
    "Getting Technical!  4 Lectures 41:51"
    "Challenge 2 Lectures 27:48"
    "Afterword 1 Lecture 05:02"
)
TWEET = (
    "New PyBites article: Module of the Week - Requests-cache "
    "for Repeated API Calls - http://pybit.es/requests-cache.html "
    "#python #APIs"
)
HTML = (
    "<p>pybites != greedy</p>"
    "<p>not the same can be said REgarding ...</p>"
)


def extract_course_times(course=COURSE):
    """Return the course timings from the passed in
       course string. Timings are in mm:ss (minutes:seconds)
       format, so taking COURSE above you would extract:
       ['01:47', '32:03', '41:51', '27:48', '05:02']
       Return this list.
    """
    rule = re.compile(r"\d{2}:\d{2}")
    return rule.findall(course)


def get_all_hashtags_and_links(tweet=TWEET):
    """Get all hashtags and links from the tweet text
       that is passed into this function. So for TWEET
       above you need to extract the following list:
       ['http://pybit.es/requests-cache.html',
        '#python',
        '#APIs']
       Return this list.
    """
    rule = re.compile(r"https?://\S+|\#\w+")
    return rule.findall(tweet)


def match_first_paragraph(html=HTML):
    """Extract the first paragraph of the passed in
       html, so for HTML above this would be:
       'pybites != greedy' (= content of first paragraph).
       Return this string.
    """
    rule = re.compile(r"<p>([^<]+)</p>")
    return rule.findall(html)[0]
