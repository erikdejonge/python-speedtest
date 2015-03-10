# coding=utf-8
"""
simple speedtest
"""

import sys
import numpy as np


def main():
    """
    main
    """
    cnt = 0
    remainders = np.remainder(range(10000000), 1000000)
    while cnt < 10000000:


        if remainders[cnt] == 0:
            sys.stdout.write(str(cnt // 1000000) + " ")
            sys.stdout.flush()
        cnt += 1
    print()


if __name__ == "__main__":
    main()
