class Solution:
    def factorial(self,ans: int,n: int) -> int:
        if n == 1:
            return ans
        else :
            ans = ans * (n-1)
            return self.factorial(ans,n-1)


n = int(input("Enter a number to find factorial "))
objects = Solution()
ans = objects.factorial(n,n)
print("Answer = ",ans)