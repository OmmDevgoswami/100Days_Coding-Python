def removeDuplicates(nums):
        # k = 0
        # max = 101
        # slice_val = 1
        # for _ in range(1, len(nums)):
        #     if len(nums) == 0:
        #         k = 0
        #     elif nums[_-1] == nums[_]:
        #         nums[_-1] = max
        #         slice_val += 1
        # nums.sort()
        # nums = nums[:slice_val]
        # k = len(nums)
        # return nums, k
        k = 1
        while k < len(nums):
            if len(nums) == 0:
                k = 0
            elif nums[k-1] == nums[k]:
                nums.pop(k)
            else:
                k += 1
        return nums, k

# Case_1:
nums = [1,1,2]
List, num = removeDuplicates(nums)
print (f"Case 1: {List} : {num}")

#CAse_2:    
nums = [0,0,1,1,1,2,2,3,3,4]
List, num = removeDuplicates(nums)
print (f"Case 2: {List} : {num}")

