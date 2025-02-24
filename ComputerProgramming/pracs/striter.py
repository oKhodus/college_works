class WordIterator:
    def __init__(self, s):
        """Initializing WordIterator with iterable string

        Args:
            s (str): string which will be split to words
        """
        self.s = s.split()
        self.index = 0

    def __iter__(self):
        """Returns the iterator itself"""
        return self

    def __next__(self):
        """Returns the next word in the sequence

        Raises:
            StopIteration: Raised when all words have been iterated over
        """
        if self.index >= len(self.s):
            raise StopIteration
        word = self.s[self.index]
        self.index += 1
        return word


text = "Python is   awesome!"
it = WordIterator(text)
print(list(it))
# Output: ['Python', 'is', 'awesome!']

text2 = "Hello DUDE!"
it2 = WordIterator(text2)
print(list(it2))

"""
Testing modules - to test type [ pytest striter.py ]
"""

def test_text1():
    text = "Python is   awesome!"
    it = WordIterator(text)
    assert list(it) == ["Python", "is", "awesome!"]


def test_text2():
    text2 = "Hello DUDE!"
    it2 = WordIterator(text2)
    assert list(it2) == ["Hello", "DUDE!"]


def test_empty_string():
    assert list(WordIterator("")) == []
