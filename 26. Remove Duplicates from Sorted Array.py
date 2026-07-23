class Solution(object):
    def removeDuplicates(self, nums):
        # nums = list(set(nums))
        # print(nums)
        # return len(nums)
        # OH STUPID PROBLEM

        # num_list = []
        # for number in nums:
        #     if number not in num_list:
        #         nums.remove(number)
        #         nums.insert(len(num_list), number)
        #         num_list.append(number)
        # return len(num_list)

        i = 0
        for j in range (len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
