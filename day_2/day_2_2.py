
def main():
    hori, dep, aim = 0,0,0
    file = open("day2Input.txt", "r")
    input = file.read()
    inplist = input.split('\n')

    for val in inplist:
        if val.startswith("forward"):
            dep += int(val.split(" ")[1]) * aim
            hori += int(val.split(" ")[1])
        elif val.startswith("down"):
            aim -= int(val.split(" ")[1])
        elif val.startswith("up"):
            aim += int(val.split(" ")[1])

    print("Aim: " + str(aim))
    print("Horizontal: " + str(hori))
    print("Depth: " + str(dep))
    print("Solution: " + str(dep * hori))

if __name__ == '__main__':
    main()