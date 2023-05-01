class Solution:
    def average(self, salary: List[int]) -> float:
        length = len(salary)-2
        salary.sort()
        return sum(salary[1:-1])/length
