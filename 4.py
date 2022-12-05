# Сложность Q(n log n)


def minimumAbsDifference(arr):
    arr = sorted(arr)
    findmin = arr[-1]-arr[0]
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] < findmin: findmin = arr[i+1] - arr[i]
    return [[arr[x],arr[x+1]] for x in range(len(arr)-1) if arr[x+1]-arr[x] == findmin]

print(minimumAbsDifference([4,2,1,3]))

