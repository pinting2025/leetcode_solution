class Solution:
    def isValid(self, s: str) -> bool:
        left = {'(', '{', '['}
        right = {')', '}', ']'}
        stack = []

        for n in s:
            if n in left:
                stack.append(n)
            else:
                if len(stack) > 0:
                    cur = stack.pop()
                    if cur == '(' and n == ')' or cur == '{' and n == '}' or cur == '[' and n == ']':
                        continue
                    else:
                        return False
                else:
                    return False
        
        return True if len(stack) == 0 else False

