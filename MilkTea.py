def string2list(s):
    lis = []
    for i in range(len(s)):
        lis.append(int(s[i]))
    return lis


def generate_change_set(distance, choice):
    change_set = set()
    add_distance = 0
    i = 0
    while choice > 0:
        if choice % 2 == 1:
            change_set.add(distance[i][1])
            add_distance += distance[i][0]
        i += 1
        choice /= 2
    return change_set, add_distance


def generate_new_optimal(optimal, change_set):
    opt = ""
    for i in range(len(optimal)):
        if i not in change_set:
            opt += optimal[i]
        else:
            if optimal[i] == '1':
                opt += '0'
            else:
                opt += '1'
    return opt


def main():
    t = int(raw_input())

    for t in range(t):
        # Read n, k
        n, m, p = [int(s) for s in raw_input().split(" ")]
        friends = []
        for i in range(n):
            s = raw_input()
            friends.append(string2list(s))
        forbidden = set()
        for i in range(m):
            s = raw_input()
            forbidden.add(s)

        optimal = ""
        distance = []
        optimal_distance = 0

        for i in range(p):
            ones = sum([friends[j][i] for j in range(n)])
            if ones > n - ones:
                optimal += '1'
                distance.append([ones - n + ones, i])
                optimal_distance += n - ones
            else:
                optimal += '0'
                distance.append([n - ones - ones, i])
                optimal_distance += ones

        distance = sorted(distance, key=lambda s: s[0])

        min_complicants = 99999999999999

        for choice in range(min(120, pow(2, len(distance)))):
            change_set, add_distance = generate_change_set(distance, choice)
            # print(distance)
            # print(choice)
            # print(change_set)
            # print(add_distance)
            if optimal_distance + add_distance >= min_complicants: continue

            new_optimal = generate_new_optimal(optimal, change_set)
            if new_optimal in forbidden: continue

            min_complicants = optimal_distance + add_distance

        print("Case #" + str(t + 1) + ": " + str(min_complicants))


if __name__ == '__main__':
    main()
    # print distance(9,12)
    # print generate_new_optimal('010101', [0, 5])
