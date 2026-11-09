# Problem 4 Passing Cars
def passing_cars(A):
    east = 0
    pairs = 0
    for i in range(len(A)):
        if A[i] == 0:
            east = east + 1
        elif A[i]==1:
            pairs = pairs + east  # every east car before it pass this one
    if pairs > 1000000000:
        return -1
    return pairs


print(passing_cars([0, 1, 0, 1, 1]))  # 5
