class Solution:
    def maximum69Number (self, num: int) -> int:
        flag = 0
        res = []
        num = str(num)

        for i in range(len(num)):
            if num[i] != '9':
                res.append('9')
                flag = 1
            
            if flag == 1:
                res.append(num[i+1:])
                break
            
            else:
                res.append('9')
        
        return int("".join(res))


        
                
                
                
                

            