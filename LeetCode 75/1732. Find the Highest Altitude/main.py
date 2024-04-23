class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = []
        alt.append(0)
        x = 0
        largest = 0

        for i in gain:
            alt.append(alt[x] + i)
            
            if largest < (alt[x] + i):
                  largest = alt[x] + i
            
            x = x + 1
        
        return(largest)