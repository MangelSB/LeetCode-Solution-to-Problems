class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        x = n
        l = len(flowerbed)

        if x == 0:
            return True

        if (l == 1 and x == 1 and flowerbed[0] == 1):
            return False

        for i in range(l):
            if x == 0:
                return True

            if i not in (0, l - 1):

                if ((flowerbed[i - 1] == 0) and (flowerbed[i] == 0) and (flowerbed[i + 1] == 0)):

                    flowerbed[i] = 1
                    x -= 1

            elif i == 0:

                if l != 1:

                    if ((flowerbed[i] == 0) and (flowerbed[i + 1] == 0)):

                        flowerbed[i] = 1
                        x = x - 1

                else:
                    return bool(x == 1)

            else:
                if (flowerbed[i - 1] == 0) and (flowerbed[i] == 0):

                    flowerbed[i] = 1
                    x = x - 1

        if x != 0 :
            return False

        return True
