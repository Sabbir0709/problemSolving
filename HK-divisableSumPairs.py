def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(0,len(ar)):
        for j in range(i, len(ar)):
            if(i < j):
                sum = ar[i]+ar[j]
                if sum % k == 0:
                    count += 1
    return count                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
