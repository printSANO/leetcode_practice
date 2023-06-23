func maxProfit(prices []int, fee int) int {
    if len(prices) == 1 {
        return 0
    }
    var buy int = -prices[0]
    var sell int = 0
    for i:= 1; i < len(prices); i++ {
        buy = maxInt(buy, sell-prices[i])
        sell = maxInt(sell, prices[i]-fee+buy)
    }
    return sell
}
func maxInt(a int, b int) int {
    if a < b {
        return b
    }
    return a
}