class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]

        
        first_letter = strs[0]
        length = len(first_letter)

        for i in strs[1:]:

            while first_letter != i[:length]:
                first_letter = first_letter[:(length -1)]
                length -= 1


                if length == 0:
                    return ""


        return first_letter

            
