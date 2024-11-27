import math as m

def coordinates(point_num):

    x = float(input(f"Please enter x coordinate for {point_num}, point: "))
    y = float(input(f"Please enter y coordinate for {point_num}, point: "))

    return(x, y)

    
def distance(x1, y1, x2, y2):
    return m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def main():
    num_points = int(input("Please enter the number of points: "))
    points = [coordinates(point + 1) for point in range(num_points)]

    min_dist = float("inf")
    close_pair = (0, 0)

    for i in range(len(points)):
        for j in range(i + 1, len(points)):

            xi, yi = points[i]
            xj, yj = points[j]

            dist = distance(xi, yi, xj, yj)

            if dist < min_dist:
                min_dist = dist
                close_pair = (i + 1, j + 1)

    print(f"Points {close_pair[0]} and {close_pair[1]} are the closest to each other.")



main()
