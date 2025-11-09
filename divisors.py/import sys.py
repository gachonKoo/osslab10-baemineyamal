import sys

def main():
    # 채점기는 input() 대신 명령행 인자를 줌
    if len(sys.argv) >= 2:
        n = int(sys.argv[1])
    else:
        # 혹시 몰라 stdin 한 줄 입력 대비
        n = int(sys.stdin.readline().strip())

    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(str(i))

    # 출력은 공백 한 줄! (엔터 여러 번 X)
    print(" ".join(result))

if __name__ == "__main__":
    main()
