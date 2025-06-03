class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        visited = set()
        available_box = [i for i in initialBoxes if status[i] == 1]
        unavailable_box = {i for i in initialBoxes if status[i] == 0}
        res = 0

        while available_box:
            current_id = available_box.pop()
            if current_id in visited:
                continue
            res += candies[current_id]
            visited.add(current_id)

            # get boxes
            for box_id in containedBoxes[current_id]:
                if status[box_id] == 1 and box_id not in visited:
                    available_box.append(box_id)
                else:
                    unavailable_box.add(box_id)
            
            # get keys
            if len(keys[current_id]) >= 1:
                for key_id in keys[current_id]:
                    status[key_id] = 1
                    if key_id in unavailable_box and key_id not in visited:
                        available_box.append(key_id)
        
        return res
        

