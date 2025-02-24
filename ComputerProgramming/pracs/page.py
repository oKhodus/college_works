class Paginator:
    def __init__(self, list, page_size):
        self.ls = iter(list)
        self.n = page_size
        self.curr = 0

    def __iter__(self):
        return self

    def __next__(self):
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
