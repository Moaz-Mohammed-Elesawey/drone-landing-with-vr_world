from math import sqrt

def euc(a, b):
    distance = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    return distance


if __name__ == '__main__':
    distance = euc((1, 3), (2, 9))
    print(distance)
