class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prod_zero = 1
        zeros = 0
        for i in nums:
            product *= i
            if i == 0:
                zeros += 1
                continue
            prod_zero *= i
            
        
        li = []
        for i in nums:
            if zeros > 1:
                li.append(0)
                continue
            if i == 0:
                li.append(prod_zero)
                continue
            li.append(int(product/i))
        return li