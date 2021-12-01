def main():
    f = open("day1Input.txt", "r")
    input = f.read()
    inplist = input.split('\n')
    inplist = [int(i) for i in inplist]
    count = 0
    current,next = 0,0
    for i in range(len(inplist)-3):
        current = inplist[i]+inplist[i+1]+inplist[i+2]
        next = inplist[i+1]+inplist[i+2]+inplist[i+3]
        if next > current:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
