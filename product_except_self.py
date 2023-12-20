# Time Complexity: O(n)
# Space Complexity: O(1)
class ProductExceptSelf(object):

    def productExceptSelf(self, nums):

        if (nums == None or len(nums) == 0):
            return []

        rProd = 1
        result = [1]

        for i in range(1, len(nums)):
            rProd = nums[i - 1] * result[i - 1]
            result.append(rProd)

        lProd = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] = lProd * result[i]
            lProd *= nums[i]

        return result
