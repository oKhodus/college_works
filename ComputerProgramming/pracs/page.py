class Paginator:
    def __init__(self, data, page_size):
        """Paginator for splitting data into pages

        Args:
            data (list): The list of items to paginate
            page_size (int): The number of items per page
        """
        self.ls = iter(data)
        self.n = page_size
        self.curr = 0

    def __iter__(self):
        """Returns the iterator itself"""
        return self

    def __next__(self):
        """Returns the next page of data.

        Raises:
            StopIteration: If all pages have been returned.
        """
        max_size = self.n
        data = []

        if self.curr >= max_size:
            raise StopIteration
        self.curr += 1

        for _ in range(self.n):
            data.append(next(self.ls))

        return f"{dict(page = self.curr, page_max = max_size, data = data)}"


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pager = Paginator(data, 3)

for page in pager:
    print(page)
