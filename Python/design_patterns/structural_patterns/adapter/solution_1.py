from typing import List


class WordsList:
    def __init__(self, words: List[str] = None) -> None:
        if isinstance(words, list):
            self._words = words

    def reverse_list(self) -> List[str]:
        return [word[::-1] for word in self._words]


class WordsString:
    def __init__(self, words: str) -> None:
        if isinstance(words, str):
            self._words: str = words

    def reverse_string(self) -> List[str]:
        return [word[::-1] for word in self._words.split(",")]


class WordsAdapter:
    """This changes the generic method name to individualized method names"""

    def __init__(self, adaptee, **kwargs):
        self._adaptee = adaptee

        self.__dict__.update(kwargs)

    def __getattr__(self, attr):
        return getattr(self._adaptee, attr)


ukrainian_string = WordsString(words="Luck,Mom,Light,Success")
ukrainian_list = WordsList(words=["Luck", "Mom", "Light", "Success"])

object_list = []
object_list.append(
    WordsAdapter(adaptee=ukrainian_string, reverse=ukrainian_string.reverse_string)
)
object_list.append(
    WordsAdapter(adaptee=ukrainian_list, reverse=ukrainian_list.reverse_list)
)

for obj in object_list:
    print(obj.reverse())
