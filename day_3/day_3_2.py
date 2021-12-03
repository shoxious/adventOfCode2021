# def main():
#     co = 0
#     countArray = [0,0,0,0,0,0,0,0,0,0,0,0]
#     filterArray = []
#     file = open("day3Input.txt", "r")
#     input = file.read()
#     inplist = input.split('\n')
#     co2list = input.split('\n')
#     oxygenList = input.split('\n')
#
#     for val in inplist:
#         for i in range(len(val)):
#             if int(val[i]) == 1:
#                 countArray[i] += 1
#
#     print(countArray)
#
#     for i in range(len(countArray)):
#         if countArray[i] >= (len(inplist) / 2):
#             countArray[i] = 1
#         else:
#             countArray[i] = 0
#
#     print(countArray)
#
#     for i in range(len(countArray)):
#         if len(inplist) == 1:
#             break
#         for val in inplist:
#             new = str(val).split()
#             if new[0][i] is not countArray[i]:
#                 inplist.remove(val)
#                 continue
#
#     for i in range(len(countArray)):
#         if len(co2list) == 1:
#             break
#         for co2 in co2list:
#             if co2[i] is countArray[i]:
#                 co2list.remove(co2)
#                 continue
#
#     print(int(inplist[0],2))
#     print(int(co2list[0],2))
#
#
# if __name__ == '__main__':
#     main()

from collections import Counter
from functools import reduce


def get_data():
    return [ln.strip() for ln in open("day3Input.txt")]


def part1(data):
    data = [Counter(map(lambda ln: ln[pos], data))
            for pos in range(0, len(data[0]))]
    gamma = reduce(lambda a, b: a + b.most_common()[0][0], data, "")
    epsilon = reduce(lambda a, b: a + b.most_common()[-1][0], data, "")
    return int(gamma, 2) * int(epsilon, 2)


def part2(data, mode):
    for pos in range(0, len(data[0])):
        if len(data) == 1:
            break

        c = Counter(map(lambda i: i[pos], data))

        char = "0" if mode == "co2" else "1"
        if c.most_common()[0][1] != c.most_common()[-1][1]:
            char = c.most_common()[-1 if mode == "co2" else 0][0]

        data = list(filter(lambda i: i[pos] == char, data))

    return int(data[0], 2)


print(part1(get_data()))
print(part2(get_data(), "oxygen") * part2(get_data(), "co2"))