class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def formatting(s: str) -> int:
            s = list(s)
            res = []
            temp = []
            leading_zero = True

            for i in range(len(s)):
                if s[i] == '.':
                    leading_zero = True
                    temp = "".join(temp)
                    if temp != '':
                        res.append(int(temp))
                    else:
                        res.append(0)
                    temp = []
                    continue

                elif s[i] == '0' and leading_zero == True:
                    continue
                
                else:
                    leading_zero = False
                    temp.append(s[i])

            if "".join(temp) != '':
                temp = "".join(temp)
                if int(temp) != 0:
                    res.append(int(temp))
                else:
                    res.append(0)
        
            return res
        
        version1 = formatting(version1)
        version2 = formatting(version2)

        for i in range(min(len(version1), len(version2))):
            if version1[i] < version2[i]:
                return -1
            elif version1[i] > version2[i]:
                return 1

        if len(version1) < len(version2) and (set(version2[len(version1):]) != {0}):
            return -1
        
        elif len(version1) > len(version2) and (set(version1[len(version2):]) != {0}):
            return 1
        
        return 0



        
