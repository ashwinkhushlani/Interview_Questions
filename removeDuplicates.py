# // [1,14,13,1,2,25,2,14]
# // [1,14,13,2,25]
from typing import List

class Solution:
    def removeDuplicates(self,arr: List[int]) -> List[int]:
        resultArray = []
        for i in arr:
            # print(i)
            if len(resultArray) < 1:
                resultArray.append(i)
            else:
                for j in resultArray:
                    flag = 0
                    if i == j:
                        flag =1
                        break
                if flag == 0:
                    resultArray.append(i)
        return resultArray

# Below line read inputs from user using map() function  
arr = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
# arr = [1,14,13,1,2,25,2,14]
objects = Solution()
ans = objects.removeDuplicates(arr)
print(ans)