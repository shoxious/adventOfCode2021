
def main():
    hori, dep = 0,0
    file = open("day2Input.txt", "r")
    input = file.read()
    inplist = input.split('\n')

    for val in inplist:
        if val.startswith("forward"):
            hori += int(val.split(" ")[1])
        elif val.startswith("down"):
            dep -= int(val.split(" ")[1])
        elif val.startswith("up"):
            dep += int(val.split(" ")[1])

    print("Horizontal: " + str(hori))
    print("Depth: " + str(dep))
    print("Solution: " + str(dep * hori))

if __name__ == '__main__':
    main()