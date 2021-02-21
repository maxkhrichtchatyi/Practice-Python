# In this Bite you are going to decode some Base64 encoded csv data.
#
# This is what the encoded data looks like:
#
# Zmlyc3RfbmFtZSxsYXN0X25hbWUsY3JlZGl0X2NhcmQKS2VlbGJ5LE1hY0NhZmZlcmt5LD
# YzOTM3MTk0MzMzMjk5MjQKTGlubmVsbCxDbGVtbWV0dCwzNTU1NTg0OTI0MDkzOTU0CkVs
# eXNoYSxNZWlnaGFuLDYzODU3OTU3OTM4OTcxMDYKS2F0YWxpbixFdGhlcnRvbiwzNTg0Mj
# MwMDExNjgwNzAwCkZpbmEsUGFzZWssNTEwMDEzNjYzMTY2NDY4NwpBcmRlbGxhLEJyYXpp
# ZXIsMjAxNzEyNjEzNjUzMzc0CkRvcnRoZWEsS2FycGluc2tpLDMwNTAyNjYxMjUxMTcyCl
# Jhbm5hLER1ZmYsMzU3NjM5MzA1NjQ5MzMxMgpDaW5uYW1vbixLYWFzbWFuLDU0NDIwMjgx
# NTA4MDg1NzAKSmFjbGluLFRvbmdlLDM1NDk4NTIxMDQ3MjQ1MjcK
#
# This data would look like this decoded:
#
# first_name,last_name,credit_card
# Keelby,MacCafferky,6393719433329924
# Linnell,Clemmett,3555584924093954
# Elysha,Meighan,6385795793897106
# Katalin,Etherton,3584230011680700
# Fina,Pasek,5100136631664687
# Ardella,Brazier,201712613653374
# Dorthea,Karpinski,30502661251172
# Ranna,Duff,3576393056493312
# Cinnamon,Kaasman,5442028150808570
# Jaclin,Tonge,3549852104724527
#
# Use the base64 module to decode this data and extract the last
# column of (fake) credit card numbers returning it as a list
# (see also the type hints and tests).


import base64
import csv
import pytest
from typing import List  # will remove with 3.9


def get_credit_cards(data: bytes) -> List[str]:
    decoded_data = base64.b64decode(data)
    reader = csv.DictReader(line.decode("utf-8") for line in decoded_data.splitlines())
    return [row["credit_card"] for row in reader]


csv1 = b"""
Zmlyc3RfbmFtZSxsYXN0X25hbWUsY3JlZGl0X2NhcmQKS2VlbGJ5LE1hY0NhZmZlcmt5LD
YzOTM3MTk0MzMzMjk5MjQKTGlubmVsbCxDbGVtbWV0dCwzNTU1NTg0OTI0MDkzOTU0CkVs
eXNoYSxNZWlnaGFuLDYzODU3OTU3OTM4OTcxMDYKS2F0YWxpbixFdGhlcnRvbiwzNTg0Mj
MwMDExNjgwNzAwCkZpbmEsUGFzZWssNTEwMDEzNjYzMTY2NDY4NwpBcmRlbGxhLEJyYXpp
ZXIsMjAxNzEyNjEzNjUzMzc0CkRvcnRoZWEsS2FycGluc2tpLDMwNTAyNjYxMjUxMTcyCl
Jhbm5hLER1ZmYsMzU3NjM5MzA1NjQ5MzMxMgpDaW5uYW1vbixLYWFzbWFuLDU0NDIwMjgx
NTA4MDg1NzAKSmFjbGluLFRvbmdlLDM1NDk4NTIxMDQ3MjQ1MjcK
"""
csv2 = b"""
Zmlyc3RfbmFtZSxsYXN0X25hbWUsY3JlZGl0X2NhcmQKTWVsaXNlbmRhLENyb3NmaWVsZC
wzNTg0MTY2NjgwNjE3MjAzCkxpYW5hLFNlbnRlbiw2NzYyMDgzNDMwNjM3MjU2NwpEZWVy
ZHJlLE1hdGNoYW0sMzU0ODI2OTgzOTkwNDUzMwpDYXNzZXksQmxleW1hbiwzNzQ2MjI3MD
Y3OTU3OTUKRG9kaSxMZXlkb24sMzU3NTkwNDg5MzQyMjc5MgpDb25ub3IsQmVybmFyZG90
dGksMzUyODYwMjY2NDk0NDkxNQpMZXdpc3MsQnJhbnNieSw1MTAwMTM4NTUzNDQ2OTQ1Ck
p1bmllLFRhbXNldHQsMzU3MDUwNDQwNDkzMzMwNgpDb3JpbGxhLEhvZiwzMDI4NzM1NDg2
NTcyNApCb2JiaSxGZnJlbmNoLDM1NjYxMTA3Njc2NTcxNTUK
"""
expected1 = [
    "6393719433329924",
    "3555584924093954",
    "6385795793897106",
    "3584230011680700",
    "5100136631664687",
    "201712613653374",
    "30502661251172",
    "3576393056493312",
    "5442028150808570",
    "3549852104724527",
]
expected2 = [
    "3584166680617203",
    "67620834306372567",
    "3548269839904533",
    "374622706795795",
    "3575904893422792",
    "3528602664944915",
    "5100138553446945",
    "3570504404933306",
    "30287354865724",
    "3566110767657155",
]


@pytest.mark.parametrize("arg, expected", [(csv1, expected1), (csv2, expected2)])
def test_get_credit_cards(arg, expected):
    assert get_credit_cards(arg) == expected
