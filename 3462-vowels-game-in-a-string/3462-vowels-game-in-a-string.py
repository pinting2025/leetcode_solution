class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # they will take the longest available string each time
        volwels = {"a", "e", "i", "o", "u"}
        s = set(s)
        return False if volwels.isdisjoint(s) else True  




        # volwels_list = []

        # for i in range(len(string)):
        #     if string[i] in volwels:
        #         volwels_list.append(i)

        # if len(volwels_list) == 0:
        #     return False
        # else:
        #     return True

        # while volwels_list or (turn == 1 and len(volwels_list) % 2 == 0):
        #     cur = 0
        #     if turn == 0: # Alice
        #         if len(volwels_list) % 2 != 0:
        #             return True
        #         else:

        #     else:








        




