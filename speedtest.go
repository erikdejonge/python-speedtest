package main

/*
def main():
    cnt = 0
    while cnt < 10000000:
        cnt = cnt + 1
        if cnt % 1000000== 0:
            print(cnt / 10000000),
    print
 */
import (
	"fmt"
	"strconv"
)

func main() {

	for cnt := 0; cnt < 10000000; cnt++ {
		if (cnt % 1000000== 0) {
			res := int64(cnt / 1000000)
			fmt.Print(strconv.FormatInt(res, 10)+" ")
		}
	}
	fmt.Println()
}
