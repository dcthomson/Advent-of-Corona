import sys

largest = 0

array = []

with open(sys.argv[1]) as f:
    nums = list(map(int, f.readline().split()))
    nums = list(set(nums))
    nums.sort()
    for i in nums:
        if not array:
            array.append(i)
        else:
            if i > array[-1]:
                if array[-1] % 2 and not i % 2:
                    array.append(i)
                elif not array[-1] % 2 and i % 2:
                    array.append(i)

print(len(array))