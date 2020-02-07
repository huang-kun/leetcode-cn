#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        results = []
        for i in range(1, n+1):
            t3 = (i % 3 == 0)
            t5 = (i % 5 == 0)
            if t3 and t5:
                results.append("FizzBuzz")
            elif t3:
                results.append("Fizz")
            elif t5:
                results.append("Buzz")
            else:
                results.append(str(i))
        
        return results
        
# @lc code=end

