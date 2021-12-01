
def main():
    f = open("day1Input.txt", "r")
    input = f.read()
    inplist = input.split('\n')
    inplist = [int(i) for i in inplist]
    count = 0
    last = inplist[0]
    for val in inplist:
        if val > last:
            count += 1
        last = val
    print(count)

if __name__ == '__main__':
    main()
