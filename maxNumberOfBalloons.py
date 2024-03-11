def maxNumberOfBalloons(self, text):
        d = {}
        for char in text:
            d[char] = d.get(char, 0) + 1
        
        b_count = d.get('b', 0)
        a_count = d.get('a', 0)
        l_count = d.get('l', 0) // 2
        o_count = d.get('o', 0) // 2
        n_count = d.get('n', 0)
        
        return min(b_count, a_count, l_count, o_count, n_count)
