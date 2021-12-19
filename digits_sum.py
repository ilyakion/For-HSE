def min_digits_sum(data):
    data.sort()
    x = 0
    y = 0
    for i in range(len(data)):
        if data[i] != 0 and x<=y:
            x = x*10 + data[i]
        else:
            y = y*10 + data[i]
    return x+y
