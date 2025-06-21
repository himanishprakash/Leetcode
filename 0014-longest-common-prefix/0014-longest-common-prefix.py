class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]

        
        
        length = len(min(strs, key = len))
        first_word = strs[0][:length]

        for i in strs[1:]:
        
            while first_word != i[:length]:
                first_word = first_word[:(length -1)]
                length -= 1


                if length == 0:
                    return ""


        return first_word

            
