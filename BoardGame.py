three_battle = []


def generate_three_battle(now, count):
    if len(now) == 9:
        three_battle.append(now)
        return None
    for i in range(3):
        if count[i] > 0:
            count[i] -= 1
            generate_three_battle(now + [i], count)
            count[i] += 1


def compete(A, B):
    count = 0
    for i in range(3):
        if B[i] > A[i]:
            count += 1
    if count > 1:
        return True
    return False


def main():
    t = int(raw_input())

    generate_three_battle([], [3, 3, 3])
    # print(len(three_battle))

    for t in range(t):
        # Read n, k
        n = int(raw_input())
        A = [int(s) for s in raw_input().split(" ")]
        B = [int(s) for s in raw_input().split(" ")]

        best = 0
        for policyA in three_battle:
            three_score_A = [0, 0, 0]
            for i in range(len(policyA)):
                three_score_A[policyA[i]] += A[i]
            count = 0.0
            win = 0.0
            for policyB in three_battle:
                three_score_B = [0, 0, 0]
                for i in range(len(policyB)):
                    three_score_B[policyB[i]] += B[i]
                count += 1
                if compete(three_score_B, three_score_A):
                    win += 1
            if win / count > best:
                best = win / count

        print("Case #%s: %.9f" % (t + 1, best))


if __name__ == '__main__':
    main()
    # generate_three_battle([], [3, 3, 3])
    # print(three_battle)
