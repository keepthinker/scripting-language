package myutil

func CountCharacter(str string, ch int32) int {
	var sum int
	for _, v := range str {
		if v == ch {
			sum++
		}
	}
	return sum
}
