list = [1, 17, 22, 24, 26, 29, 31, 32, 37, 39, 40, 43, 45, 46, 48, 57, 58, 59, 64, 66, 67, 75, 79, 81, 84, 86, 87, 90, 91, 98]

number = int(input("type a number: "))

min = 0
max = len(list) - 1

while min <= max:
    mid = (min + max) // 2
    if number > list[mid]:
        min = mid + 1
    elif number < list[mid]:
        max = mid - 1
    else:
        print("number index is", mid)
        break
else:
    print("the list does not contain this number")