func intersection(nums1 []int, nums2 []int) []int {
    var lst []int
    m := make(map[int]int)

    for _, num := range nums1 {
        m[num] = 1
    }
    for _, num := range nums2 {
        if m[num] == 1 {
            lst = append(lst, num)
            m[num] = 2
        }
    }
    return lst
}