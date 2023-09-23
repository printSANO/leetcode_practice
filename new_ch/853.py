class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted([(position[i], speed[i]) for i in range(len(position))], reverse=True)
        ans = []
        zero = ps.pop(0)
        ans.append((target - zero[0]) / zero[1])
        if len(ps) > 0:
            for p , s in ps:
                time = (target - p) / s
                if time > ans[-1]:
                    ans.append(time)
        return len(ans) 
        