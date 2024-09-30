class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = math.floor(len(nums) // 2) + 1
        
        while True:
            i = random.randint(0, len(nums) - 1)
            count = 0

            for n in nums:
                if n == nums[i]:
                    count += 1

                if count >= majority:
                    return n