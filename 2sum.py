class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            j=i+1
            
            if target==0 or nums[i]!=target:
                for j in range(j,len(nums)):
                    if nums[j]+nums[i]==target:
                        x= [i,j]
                        return x
                        break 
                    else: pass
            else:
                y=[i]
                return y
                break
