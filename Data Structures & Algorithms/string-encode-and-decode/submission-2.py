class Solution:
    """
    Encode:
    - take count of each string - "14#" - prefix
    - concat all strings with their prefixes and return

    Decode:
    - iterate through string 
    - go until first "#" - prev chars are your count, N
    - the next N chars are the string. iterate & build string, then add to result list
    - when you get to N, that is the start of the next number, followed by "#". loop starts over

    "5 # h e l l o 5 # w o r l d"
     i j k
    """

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            size = len(string)
            encodedString += f"{size}#{string}"
        return encodedString

    def decode(self, s: str) -> List[str]:
        result = list()
        decodedString = ""
        i = 0
        while i < len(s):

            lengthStr = ""

            j = i
            while s[j] != "#":
                lengthStr += s[j]
                j += 1
            
            # At this point, J is on "#", and I -> J is the length
            length = int(lengthStr)

            # Iterate through length, adding each char to string, stopping at next number
            string = ""
            k = j + 1
            endIdx = k + length
            while k < endIdx: # off by 1 here?
                string += s[k]
                k += 1

            # Add string to result list
            result.append(string)
            i = k
 
        return result
