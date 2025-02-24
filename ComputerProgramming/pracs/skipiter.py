class SkippingIterator:
    def __init__(self, iter, step):
        """Initializing SkippingIterator with iterable and step

        Args:
            iter (list, tuple, str): sequence which will be used
            step (int): value of space between elements
        """
        self.iter = iter
        self.step = step
        self.index = 0

    def __iter__(self):
        """Returns the iterator itself"""
        return self

    def __next__(self):
        """Returns the next element in the sequence, skipping elements as per step

        Raises:
            StopIteration: will be raised when index come to final element 
            or easier - when sequence is exhausted

        Returns:
            The next element in the iterable using the skipping step
        """
        if self.index >= len(self.iter):
            raise StopIteration

        elem = self.iter[self.index]
    
        self.index += self.step + 1
        return elem


seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
it = SkippingIterator(seq, 2)
print(list(it))  # Output: [1, 4, 7]

text = "abcdefghi"
it = SkippingIterator(text, 2)
print("".join(it))  # Output: "adg"


"""
Testing modules - to test type [ pytest skipiter.py ]
"""

def test_ls():
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    it = SkippingIterator(ls, 2)
    it_step3 = SkippingIterator(ls, 3)

    assert list(it) == [1, 4, 7]
    assert list(it_step3) == [1, 5, 9]


def test_text():
    text = "abcdefghi"
    it2 = SkippingIterator(text, 2)

    assert "".join(it2) == "adg"


def test_tuple():
    var_tuple = (0, 9, 19, 29, 39, 49)
    it3 = SkippingIterator(var_tuple, 2)

    assert tuple(it3) == (0, 29)
