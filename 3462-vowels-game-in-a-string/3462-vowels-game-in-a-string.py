class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # they will take the longest available string each time
        turn = 0 # keep track of who's turn it is 
        string = list(s)
        volwels = {"a", "e", "i", "o", "u"}
        volwels_list = []

        for i in range(len(string)):
            if string[i] in volwels:
                volwels_list.append(i)

        if len(volwels_list) == 0:
            return False
        else:
            return True
            
        # while volwels_list or (turn == 1 and len(volwels_list) % 2 == 0):
        #     cur = 0
        #     if turn == 0: # Alice
        #         if len(volwels_list) % 2 != 0:
        #             return True
        #         else:

        #     else:








        




