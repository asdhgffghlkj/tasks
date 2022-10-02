def array_maximum(arr):

    if len(arr) == 0:
        return None
    lead = arr[0]
    for elem in arr:
        if (elem>lead):
            lead=elem
    return lead

# for (int i = 0; i < N; i++) {
#     elem = arr[i]
#


assert array_maximum((1, 3, 5)) == 5
assert array_maximum((1, 3, 3)) == 3
assert array_maximum((3, 3, 3)) == 3
assert array_maximum((1,)) == 1
assert array_maximum(tuple()) == None
