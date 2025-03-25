class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        ver_rectangles = sorted(rectangles, key=lambda x:x[0])
        hor_rectangles = sorted(rectangles, key=lambda x:x[1])

        ver_merged = [[ver_rectangles[0][0], ver_rectangles[0][2]]]
        hor_merged = [[hor_rectangles[0][1], hor_rectangles[0][3]]]

        def is_valid(rectangles, merged, t):
            for r in rectangles[1:]:
                cur = merged[-1]
                if t == 'v':
                    start = r[0]
                    end = r[2]
                else:
                    start = r[1]
                    end = r[3]
                
                if start < cur[1]:
                    merged[-1][1] = max(merged[-1][1], end)
                else:
                    merged.append([start, end])
                
                if len(merged) >= 3:
                    return True
            return False

        return is_valid(ver_rectangles, ver_merged, 'v') or is_valid(hor_rectangles, hor_merged, 'h')

        # for r in rectangles[1:]:
        #     v_cur = ver_merged[-1]
        #     h_cur = hor_merged[-1]
        #     print(hor_merged)

        #     ver_start = r[0]
        #     ver_end = r[2]
        #     hor_start = r[1]
        #     hor_end = r[3]

        #     # check vertical
        #     if ver_start < v_cur[1]:
        #         ver_merged[-1][1] = max(v_cur[1], ver_end)
        #     else:
        #         ver_merged.append([ver_start, ver_end])
            
        #     # check horizontal
        #     if hor_start < h_cur[1]:
        #         hor_merged[-1][1] = max(h_cur[1], hor_end)
        #     else:
        #         hor_merged.append([hor_start, hor_end])
            
        #     if len(hor_merged) >= 3 or len(ver_merged) >= 3:
        #         return True

        # return False
            




            
