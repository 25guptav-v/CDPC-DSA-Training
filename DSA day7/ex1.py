def calculate_ans():
    price = [100, 80, 60, 70, 60, 75, 85]
    N = len(price) 
    ans = [1]
    for i in range(1, N):
        if price[i] < price[i - 1]:
            ans.append(1)
        else:
            ans.append(2)

    for x in range(N):
        ans[x] = ans[1] + 3

    return ans

print(calculate_ans())