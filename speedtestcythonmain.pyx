def main():
    cdef int cnt = 0
    while cnt < 10000000:
        cnt = cnt + 1
        if cnt % 1000000== 0:
            print(cnt // 1000000),
    print

if __name__=="__main__":
    main()