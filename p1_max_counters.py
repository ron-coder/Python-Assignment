# Problem 1 Max Counters
def max_counters(N, A):
    counters = [0] * N
    base = 0  #the floor value after max counter
    current_max = 0
    for k in range(len(A)):
        op = A[k]
        if op == N+1:
            base = current_max  # set all counter to max (later)
        else:
            i = op - 1  # index start from 0
            if counters[i] < base:
                counters[i] = base
            counters[i] = counters[i]+1
            if counters[i] > current_max:
                current_max = counters[i]
    result = []
    for i in range(N):
        if counters[i]<base:
            result.append(base)
        else:
            result.append(counters[i])
    return result


print(max_counters(5, [3, 4, 4, 6, 1, 4, 4]))  # [3, 2, 2, 4, 2]
