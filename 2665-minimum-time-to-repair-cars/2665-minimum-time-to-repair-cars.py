class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_valid(num):
            c = 0
            for i in ranks:
                c += int(math.sqrt(num // i))
                if c >= cars:
                    return True

            return False

        left = 0
        max_car = cars // len(ranks) + 1
        right = (max_car ** 2) * max(ranks)

        while left <= right:
            mid = (left + right) // 2

            if is_valid(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left

            
        