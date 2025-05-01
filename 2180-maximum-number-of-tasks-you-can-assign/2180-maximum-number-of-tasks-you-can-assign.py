class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks = sorted(tasks)
        workers = sorted(workers)

        def helper(target):
            tasks_copy = tasks[:target]
            workers_copy = workers.copy()
            pills_copy = pills 
            strength_copy = strength

            if pills == 0:
                strength_copy = 0
                
            for i in range(target-1, -1, -1):
                if workers_copy[-1] + strength_copy < tasks_copy[i]:
                    return False

                if workers_copy[-1] >= tasks_copy[i]:
                    workers_copy.pop()
                else:
                    # find the smallest worker that can do the task with pill
                    left = 0 
                    right = len(workers_copy)
                    while left <= right:
                        mid = (right+left) // 2
                        if workers_copy[mid] + strength_copy >= tasks_copy[i]:
                            right = mid - 1
                        else:
                            left = mid + 1
                    if workers_copy[left] + strength_copy >= tasks_copy[i]:
                        workers_copy.pop(left)
                    else:
                        return False
                    pills_copy -= 1
                    if pills_copy == 0:
                        strength_copy = 0

            return True 

        right = min(len(tasks), len(workers))
        left = 0

        while left <= right:
            mid = (right+left+1) // 2

            if helper(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right