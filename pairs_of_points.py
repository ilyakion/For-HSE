import math

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def closest_pair_of_points(data):
    data.sort()
    mindis = distance(data[1], data[0])
    m1 = data[1]
    m2 = data[0]
    for i in range(len(data)-1):
        r = data[i][0]-data[i+1][0]
        if r<0:
            r *= -1
        if r < mindis:
            for j in range(i, len(data)):
                if i != j:
                    dis = distance(data[i], data[j])
                    if dis < mindis:
                        mindis = dis
                        m1 = data[i]
                        m2 = data[j]
    mindis = round(mindis,8)
    return (mindis, m1, m2)
