class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingred = set()
        res = []
        flag_add = True

        for i in supplies:
            ingred.add(i)
        
        while flag_add == True:
            init_len = len(res)
            for r, i in zip(recipes, ingredients):
                flag_ingred = True
                for j in i:
                    if j not in ingred:
                        flag_ingred = False
                        break
                if flag_ingred == True and r not in res:
                    ingred.add(r)
                    res.append(r)
            if len(res) == init_len:
                flag_add = False
        
        return res


            
            


        