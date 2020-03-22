import sys

largest = 0

array = []

with open(sys.argv[1]) as f:
    nums = f.readline().split()
    for i in nums:
        i = int(i)
        if array:
            if i > array[-1]:
                if array[-1] % 2 and not i % 2:
                    array.append(i)
                elif not array[-1] % 2 and i % 2:
                    array.append(i)
                else:
                    if len(array) > largest:
                        largest = len(array)
                    array = []
            else:
                if len(array) > largest:
                    largest = len(array)
                array = []
        else:
            array.append(i)
print(largest)