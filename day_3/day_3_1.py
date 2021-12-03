def main():
    gamma, epsilon = "",""
    countArray = [0,0,0,0,0,0,0,0,0,0,0,0]
    file = open("day3Input.txt", "r")
    input = file.read()
    inplist = input.split('\n')

    for val in inplist:
        for i in range(len(val)):
            if int(val[i]) == 1:
                countArray[i] += 1

    for i in range(len(countArray)):
        if countArray[i] > (len(inplist) / 2):
            gamma += "1"
        else:
            gamma += "0"

    for i in range(len(gamma)):
        if gamma[i] == "1":
            epsilon += "0"
        else:
            epsilon += "1"

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    print(int(gamma) * int(epsilon))

if __name__ == '__main__':
    main()
