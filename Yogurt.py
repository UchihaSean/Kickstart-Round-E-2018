def main():
    t = int(raw_input())

    for t in range(t):
        # Read n, k
        n, k = [int(s) for s in raw_input().split(" ")]
        A = [int(s) for s in raw_input().split(" ")]
        A = sorted(A)
        yogurt = 0
        for i in range(n):
            if yogurt / k+1 <= A[i]:
                yogurt += 1
        print("Case #" + str(t + 1) + ": " + str(yogurt))


if __name__ == '__main__':
    main()
