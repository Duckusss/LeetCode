def hash_map(string):
            hm = {}
            for i in range(len(string)):
                if string[i] in hm:
                    hm[string[i]] += 1
                else:
                    hm[string[i]] = 1
            return hm
        
        if len(s) != len(t):
            return False
        
        return hash_map(s) == hash_map(t)
