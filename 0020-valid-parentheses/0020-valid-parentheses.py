class Solution:
    def isValid(self, s: str) -> bool:
        
        stored = {']':'[', '}':'{', ')':'('}

        stack = []

        for i in s:
            if i not in stored:
                stack.append(i)
                
            else:
                if not stack:
                    return False
                else:
                    value = stack.pop()
                    
                    if value != stored[i]:
                        return False


        return not stack