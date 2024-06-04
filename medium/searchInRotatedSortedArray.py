class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        begin = 0
        end = len(nums) - 1

        while begin <= end:
            startNum = nums[begin]
            endNum = nums[end]

            if target == startNum:
                return begin
            if target == endNum:
                return end

            mid = begin + (end - begin)//2

            if nums[mid] == target:
                return mid

            elif target < endNum:
                if nums[mid] <= endNum:
                    if nums[mid] > target:
                        end = mid - 1
                    else:
                        begin = mid + 1

                else:
                    begin = mid + 1

            else:
                if nums[mid] >= endNum:
                    if nums[mid] > target:
                        end = mid - 1
                    else:
                        begin = mid + 1

                else:
                    end = mid - 1

        return -1