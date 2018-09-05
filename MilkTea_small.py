def string2int(s):
    d = 0
    for i in range(len(s)):
        d = d * 2 + int(s[i])
    return d


def distance(x, y):
    xor = x ^ y
    xor_num = 0
    while xor > 0:
        if xor % 2 == 1: xor_num += 1
        xor /= 2
    return xor_num


def main():
    t = int(raw_input())

    for t in range(t):
        # Read n, k
        n, m, p = [int(s) for s in raw_input().split(" ")]
        friends = []
        for i in range(n):
            s = raw_input()
            friends.append(string2int(s))
        forbidden = []
        for i in range(m):
            s = raw_input()
            forbidden.append(string2int(s))
        forbidden = set(forbidden)

        min_complicants = 99999999999999
        for choice in range(pow(2, p)):
            if choice in forbidden: continue
            complicants = 0
            for i in range(len(friends)):
                complicants += distance(friends[i], choice)
            if complicants < min_complicants:
                min_complicants = complicants
        print("Case #" + str(t + 1) + ": " + str(min_complicants))


if __name__ == '__main__':
    main()
    # print distance(9,12)
