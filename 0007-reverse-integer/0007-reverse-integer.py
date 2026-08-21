class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0 :
            sign = -1
        else:
            sign = 1

        reverse, number = 0 , abs(x)
        while number:

            number , denom = divmod(number,10)

            reverse = 10 * reverse + denom

            if reverse > 2**31 -1:
                return 0

        return  sign * reverse
            

        