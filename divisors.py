import sys

def main():
    # GitHub 채점기는 명령행 인자(argv)를 사용
    if len(sys.argv) >= 2:
        n = int(sys.argv[1])
    else:
        # 혹시 몰라 stdin 한 줄 입력도 대비
        n = int(sys.stdin.readline().strip())

    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(str(i))

    # 한 줄에 공백으로 구분해서 출력 (줄바꿈 X)
    print(" ".join(result))

if __name__ == "__main__":
    main()
