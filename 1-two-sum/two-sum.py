class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # # ----- 1 -------------- Hash map 
        # Hash_map = {}
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in Hash_map:
        #         return [Hash_map[diff], i]
        #     Hash_map[n]=i

       
        
       # ------- 2 ------  Bruate Force
        
        n = len(nums)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    
     
        
    

        

        


   
        