package main

import "fmt"

func main() {
	var arr = [6]int{1, 2, 3, 4, 5, 6}
	for i := 0; i < 6; i++ {
		fmt.Println(arr[i])
	}
	fmt.Println("-------------------");
        var a, b = 0, 10
	for a < b {
		fmt.Println(a)
		a++
	}

	fmt.Println("-------------------");
	for x, y := range arr {
		fmt.Printf("index: %d, value: %d\n", x, y)
	}

	if x := multiply(arr[0], arr[1]); x > 10 {
		fmt.Println("hello")
	} else {
		fmt.Println("world")
	}

	j := 0
	Here:
	j++
	fmt.Printf("%d ", j)
	if j < 10 {
		goto Here
	}
	fmt.Println("goto end")

	i := 0
	for {
		if i > 10 {
			break
		}
		i++
	}
	fmt.Println("end for i=", i)

	switch i {
	case 11 : fmt.Println("case 11") 
	fallthrough
	case 12 : fmt.Println("case 11 fallthrough")
	case 13 : fmt.Println("case 12")
	}
}

func multiply(a int, b int) int {
	return a * b
}
