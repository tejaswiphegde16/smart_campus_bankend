def sorting_searching_demo():

    ids = [105, 102, 110, 108, 101]

    print("Original IDs:", ids)

    n = len(ids)

    for i in range(n):
        for j in range(0, n-i-1):

            if ids[j] > ids[j+1]:
                ids[j], ids[j+1] = ids[j+1], ids[j]

    print("Sorted IDs:", ids)

    target = int(input("Enter ID to search: "))

    found = False

    for i in range(len(ids)):

        if ids[i] == target:
            print("ID found at index", i)
            found = True
            break

    if not found:
        print("ID not found")