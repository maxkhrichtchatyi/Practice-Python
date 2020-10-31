# Write a simple Promo class. Its constructor receives two variables:
# name (which must be a string) and expires (which must be a datetime
# object).
#
# Add a property called expired which returns a boolean value indicating
# whether the promo has expired or not.

from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name: str, expires: datetime) -> None:
        self.name = name
        self.expires = expires

    @property
    def expired(self) -> bool:
        return self.expires < NOW
