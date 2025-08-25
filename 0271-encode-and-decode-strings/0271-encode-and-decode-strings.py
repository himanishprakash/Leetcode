class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        string = ""
        for i in strs:
            n = len(i)
            string += str(n) + "#" + i

        return string
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            number = int(s[i:j])
            i = j + 1
            j = i + number
            result.append(s[i:j])
            i = j

        return result


            
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))