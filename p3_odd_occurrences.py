# Problem 3 Odd Occurrences
def odd_occurrences(A):
    counts = {}
    for x in A:
        if x in counts:
            counts[x] = counts[x] + 1
        else:
            counts[x]=1
    for key in counts.keys():
        if counts[key] % 2 == 1:  # odd mean it dont have pair
            return key


print(odd_occurrences([9, 3, 9, 3, 9, 7, 9]))  # 7
