class Solution:
    def isValid(self, s: str) -> bool:
        
        check = {')':'(', '}': '{', ']':'['}

        stack = []

        for i in s:
            if i not in check:
                stack.append(i)

            else:
                if not stack:
                    return False

                else:
                    value = stack.pop()

                    if value != check[i]:
                        return False

        
        return not stack