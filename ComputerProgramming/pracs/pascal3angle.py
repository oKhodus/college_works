def pascals_triangle():
    """Make the infinite pascals_triangle of a given range

    Yields:
        list[int]: List of elements which consists integeres
    """
    row = [1]
    while True:
        yield row
        new_row = [1]
        for index in range(len(row) - 1):
            new_row.append(row[index] + row[index + 1])
        new_row.append(1)
        row = new_row

gen = pascals_triangle()
for _ in range(5):
    print(next(gen))