func twoSum(nums []int, target int) []int {
    m:= make(map[int]int)
    for i, num := range nums {
        if x, ok := m[target-num]; ok {
            return []int{x,i}
        }
        m[num] = i
    }
    return []int{}
}
