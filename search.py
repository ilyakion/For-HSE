def f(data, target, count):

    if count <= 0:
        return []
    if len(data) <= count:
        return data

    low = 0
    top = len(data) - 1

    while top - low >1 :
        if target <= data[low + (top - low)//2]:
            top = low + (top - low)//2
        else:
            low = low + (top - low)//2

    ans =[]

    while len(ans) < count:
        if low == -1:
            ans.append(data[top])
            top +=1
        elif top == len(data):
            ans = [data[low]] + ans
            low -= 1
        elif target - data[low] <= data[top] - target:
            ans = [data[low]] + ans
            low -= 1
        else:
            ans.append(data[top])
            top +=1

    return ans
