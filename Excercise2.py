def highesteven(li):
    highest = 0
    for i in li:
        if i%2 == 0 and highest < i:
            highest = i;

    return highest


print(highesteven([10,2,3,4,8,11]))

total = 0


def count(total):
    total += 1
    return total


print(count(total))
print(total)
