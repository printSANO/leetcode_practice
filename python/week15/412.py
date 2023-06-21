class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst = ["1"]*n
        for i in range(1,n+1):
            lst[i-1] = str(i)
        for i in range(2,n,3):
            lst[i] = "Fizz"
        for i in range(4,n,5):
            if lst[i] == str(i+1):
                lst[i] = "Buzz"
            else:
                lst[i] += "Buzz"
        return lst