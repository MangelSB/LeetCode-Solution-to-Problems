class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []
        sumCandy = 0
        maxCandies = max(candies)
        
        for i in candies:
            sumCandy = i + extraCandies
            if sumCandy >= maxCandies:
                results.append(True)
            else:
                results.append(False)    

        return results