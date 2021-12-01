import requests


def first():
    value = -1
    oldValue = -1
    big = 0
    low = 0
    noValue = 0
    same = 0

    file = open("day1Input.txt", "r")
    for line in file:
        value = int(line)
        if oldValue == -1:
            noValue += 1
        elif value > oldValue:
            big += 1
        elif value > oldValue:
            low += 1
        elif value == oldValue:
            same += 1
        oldValue = value

    print('*** Bigger: ' + str(big))
    print('*** Lower: ' + str(low))


def second():

    sum = 0
    sumArray = []
    count = 0
    big = 0
    low = 0
    same = 0
    newValue = 0
    oldValue = 0

    suma = 0
    sumb = 0
    sumc = 0
    sumd = 0

    file = open("day1Input.txt", "r")
    for line in file:
        sum += int(line)
        count += 1

        if count == 3:
            sumArray.append(sum)
            sum = 0
            count = 0



    for idx, val in enumerate(sumArray):
        if count == 0:
            suma += val
        elif count == 1:
            suma += val
            sumb += val
        elif count == 2:
            suma += val
            sumb += val
            sumc += val
        elif count == 3:



    if count == 3:
        count = 0




    print('*** Bigger: ' + str(big))
    print('*** Lower: ' + str(low))
    print('*** Equal: ' + str(same))


if __name__ == '__main__':
    second()
