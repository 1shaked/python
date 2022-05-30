def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = 1
    N = int(N)
    for i in range(N):
        numberStr = '6431923912'
        try:
            number = int(numberStr)
            numberStrLen = len(numberStr)
            isStartGood = numberStr[0] in ['6','7','8']
            if (isStartGood and numberStrLen == 10):
                print("YES")
            else:
                print("NO")
        except:
            print("NO")
    return 0

if __name__ == '__main__':
    main()