package main

import "strconv"

func double(n int, index int) (bool, int) {
	str := strconv.Itoa(n)
	amount := 0
	for i := index; i < len(str); i++ {
		if str[i] == str[index] {
			amount++
		}
	}
	if amount == 2 {
		return true, amount
	}
	return false, amount
}

func main() {
	var test int = 111122
	doubl := false
	for j := 0; j < len(strconv.Itoa(test)); j++ {
		test, amount := double(test, j)
		if test {
			doubl = true
			break
		} else {
			println(j, amount)
			j += amount - 1
		}
	}
	println(doubl)
	return
}
