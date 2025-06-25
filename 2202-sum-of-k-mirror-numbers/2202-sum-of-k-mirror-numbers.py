class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_base_k_palindrome(num: int, k: int) -> bool:
            
            original = num
            reversed_num = 0
            while num > 0:
                reversed_num = reversed_num * k + num % k
                num //= k
            return original == reversed_num

        def create_palindrome(half: int, odd: bool) -> int:
            
            pal = half
            if odd:
                half //= 10  
            while half > 0:
                pal = pal * 10 + half % 10
                half //= 10
            return pal

        sum_ = 0    
        found = 0     
        length = 1    

       
        while found < n:
            start = 10 ** ((length - 1) // 2)
            end = 10 ** ((length + 1) // 2)

          
            for half in range(start, end):  
                pal = create_palindrome(half, length % 2 == 1)
                
                if is_base_k_palindrome(pal, k):  
                    
                    sum_ += pal        
                    found += 1
                    
                    if found == n:     
                        return sum_
            
            length += 1  

        return sum_