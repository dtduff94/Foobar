def solution(x, y):
    y_diff = y - 1
    height = x + y_diff
    id = height * (height + 1) // 2
    id -= y_diff
    return str(id)
