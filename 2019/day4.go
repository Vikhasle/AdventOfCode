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

func ptOne(start, end int) int {
	var validPass []int
	for i := start; i <= end; i++ {
		var double, decr bool = false, true
		for j := 0; j < len(strconv.Itoa(i))-1; j++ {
			if strconv.Itoa(i)[j] > strconv.Itoa(i)[j+1] {
				decr = false
			}
			if strconv.Itoa(i)[j] == strconv.Itoa(i)[j+1] {
				double = true
			}
		}
		if decr && double {
			validPass = append(validPass, i)
		}
	}
	return len(validPass)
}

func ptTwo(start, end int) int {
	var validPass []int
	for i := start; i <= end; i++ {
		var doubl, decr bool = false, true
		for j := 0; j < len(strconv.Itoa(i))-1; j++ {
			if strconv.Itoa(i)[j] > strconv.Itoa(i)[j+1] {
				decr = false
			}
		}

		for j := 0; j < len(strconv.Itoa(i)); j++ {
			test, amount := double(i, j)
			if test {
				doubl = true
				break
			} else {
				j += amount - 1
			}
		}

		if decr && doubl {
			validPass = append(validPass, i)
		}
	}
	return len(validPass)
}

func main() {
	println(ptOne(156218, 652527))
	println(ptTwo(156218, 652527))
	return
}
