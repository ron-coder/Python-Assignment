# Problem 2 Missing Integer
def missing_integer(A):
    A = sorted(A)  # sort it first so its easier
    ans = 1
    for x in A:
        if x == ans:
            ans = ans + 1
        elif x > ans:
            break  # found a gap so ans is missing
    return ans


print(missing_integer([1, 3, 6, 4, 1, 2]))  # 5
print(missing_integer([1,2,3]))  # 4
print(missing_integer([-1, -3]))  # 1
