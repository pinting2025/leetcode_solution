class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # zero index set 
        languages_set = [set(l) for l in languages]

        wait_list = set()

        # list of people who cannot talk to each other
        for u, v in friendships:
            u -= 1
            v -= 1
            # don't share same language
            if languages_set[u].isdisjoint(languages_set[v]):
                wait_list.add(u)
                wait_list.add(v)
            
        if len(wait_list) == 0:
            return 0
        
        language_counter = Counter()
        for person in wait_list:
            for l in languages_set[person]:
                language_counter[l] += 1
        
        most_common_language = max(language_counter.values()) if language_counter else 0

        return len(wait_list) - most_common_language




        








