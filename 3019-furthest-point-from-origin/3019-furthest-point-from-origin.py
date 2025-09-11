class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        movements = Counter(moves)
        return max(movements['L'], movements['R']) + movements['_'] - min(movements['L'], movements['R'])