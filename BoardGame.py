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


def generate_error(three_score):
    average = sum(three_score) / 3.0
    error = 0
    for score in three_score:
        error += (average - score) ** 2
    return error


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

    for t in range(t):
        # Read n, k
        n = int(raw_input())
        A = [int(s) for s in raw_input().split(" ")]
        B = [int(s) for s in raw_input().split(" ")]

        min_error = 999999999999999
        best_policy = None
        best_three_score = None
        for policy in three_battle:
            three_score = [0, 0, 0]
            for i in range(len(policy)):
                three_score[policy[i]] += A[i]
            error = generate_error(three_score)
            if error < min_error:
                min_error = error
                best_policy = policy
                best_three_score = three_score

        # print(best_three_score)
        count = 0.0
        win = 0.0

        for policy in three_battle:
            count += 1
            three_score = [0, 0, 0]
            for i in range(len(policy)):
                three_score[policy[i]] += B[i]
            # print(policy, three_score)
            if compete(three_score, best_three_score):
                # print(policy,three_score,best_three_score)
                win += 1
        print("Case #%s: %.9f" % (t + 1, win / count))


if __name__ == '__main__':
    main()
    # generate_three_battle([], [3, 3, 3])
    # print(three_battle)
