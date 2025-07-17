def spiral(n):
    res = [[0] * n for _ in range(n)]
    num = 1
    left, right = 0, len(res) - 1
    top, bottom = 0 , len(res) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            res[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            res[i][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, - 1):
                res[bottom][i] = num
                num += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                res[i][left] = num
                num += 1
            left += 1
    return res

n = 5
for row in spiral(n):
    print(row)