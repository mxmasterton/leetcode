class Solution:

    def encode(self, strings: List[str]) -> str:
        output = ""

        for string in strings:
            output += str(len(string))
            output += "x"
            output += string
        
        return output

    def decode(self, string: str) -> List[str]:
        output = []
        i = 0

        while i < len(string):
            j = i
            while string[j] != "x":
                j += 1

            length = int(string[i:j])

            i = j + length + 1
            output.append(string[j + 1:i])

        return output