l = [4,0,5,-5,3,3,0,-4,-5]

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums = sorted(nums)

        tracker = sum(nums[0:3])

        for i in range(len(nums)-2):
            one = nums[i]
            two = i+1
            three = len(nums)-1
            while True:
                temp = one+nums[two]+nums[three]
                if two >= three:
                    break
                if temp < target:
                    if abs(target-temp) < abs(target-tracker):
                        tracker = temp
                    two += 1
                elif temp > target:
                    if abs(target-temp) < abs(target-tracker):
                        tracker = temp
                    three -= 1
                else:
                    return temp
        return tracker

x = Solution()
print(x.threeSumClosest(l,-2))