class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # ingred = set()
        # res = []
        # flag_add = True

        # for i in supplies:
        #     ingred.add(i)
        
        # while flag_add == True:
        #     init_len = len(res)
        #     for r, i in zip(recipes, ingredients):
        #         flag_ingred = True
        #         for j in i:
        #             if j not in ingred:
        #                 flag_ingred = False
        #                 break
        #         if flag_ingred == True and r not in res:
        #             ingred.add(r)
        #             res.append(r)
        #     if len(res) == init_len:
        #         flag_add = False
        
        # return res

        supplies = set(supplies)
        dic = {recipes[i] : ingredients[i] for i in range(len(ingredients))}
        to_add, res = [], []

        start = True
        while to_add or start:
            start = False

            # Update the supply and take away recipes we alr made
            for i in to_add:
                del dic[i]
                supplies.add(i)
                res.append(i)

            # See which recipes can be made with current supplies
            to_add = []
            for key, val in dic.items():
                can_make = True
                for i in val:
                    if i not in supplies:
                        can_make = False
                        break
                if can_make:
                    to_add.append(key)
        return res

            
            


        