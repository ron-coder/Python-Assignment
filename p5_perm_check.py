# Problem 5 Perm Check
def perm_check(A):
    N = len(A)
    B = sorted(A)
    for i in range(N):
        if B[i] != i+1:  #should be 1,2,3...N
            return 0
    return 1


print(perm_check([4, 1, 3, 2]))  # 1
print(perm_check([4,1,3]))  # 0
