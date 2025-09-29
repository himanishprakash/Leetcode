class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        number_of_passenger = [0] * 1001

        for trip in trips:
            number_of_passenger[trip[1]] += trip[0]
            number_of_passenger[trip[2]] -= trip[0]

        
        use_capacity = 0
        for trip in number_of_passenger:
            use_capacity += trip
            
            if use_capacity > capacity:
                return False

        return True


