func addStrings(num1 string, num2 string) string {
	bigIntNum1, _ := new(big.Int).SetString(num1, 10)
	bigIntNum2, _ := new(big.Int).SetString(num2, 10)

	sum := new(big.Int).Add(bigIntNum1, bigIntNum2)

	return sum.String()
}