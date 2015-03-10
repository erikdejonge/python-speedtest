# coding=utf-8
"""
simple speedtest
"""
import sys


def main():
    """
    main
    """
    cnt = 0

    while cnt < 10000000:
        cnt += 1

        if cnt % 1000000== 0:
            sys.stdout.write(str(cnt // 1000000)+" ")
            sys.stdout.flush()

    print()


if __name__ == "__main__":
    main()
