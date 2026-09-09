from collections import defaultdict
import json

class Solution:
    """
    [ "hi", "hel#lo", "hello;world", "hi==again--", "edge[case]", "{curly}edge{case}" ]
    [ ["h", "i"], ["h", "e", "l", "#", "l", "]"], "hello;world", "hi==again--", "edge[case]", "{curly}edge{case}" ]
    [ { h:[0], i:[1] }, { h:[0], e:[1], l:[2, 4] #:[3], "l": [5], "]": [6] }, ... ]

    "___l_l___________"

    edge case: can json handle those weird chars as strings?

    PLAN:
    ENCODE:
    - Create a map for each string in input list
      - Letters are keys, list of indexes where that letter appears are the values
      - e.g., { "h": [0], "i": [1, 2, 3] }
    - Serialize that into JSON
    - return JSON
    DECODE:
    - Deserialize JSON
    - For each object in list, rebuild the decoded string and add to result list
      - Loop through map to find the largest index "N"
      - Initialize a list/str with size N
      - Loop through the map and insert char into the indexes specified by the value list
      - Add to result list
    - return result list
    """

    def encode(self, strs: List[str]) -> str:
        encodedStrings = list()

        for string in strs:
            stringMap = defaultdict(list)
            for idx, char in enumerate(string):
                stringMap[char].append(idx)
            encodedStrings.append(stringMap)

        return json.dumps(encodedStrings)

    def decode(self, s: str) -> List[str]:
        encodedStrings = json.loads(s)
        decodedStrings = list()
 
        for stringMap in encodedStrings:
            stringSize = 0
            for charKey, indexes in stringMap.items():
                stringSize += len(indexes)
            
            stringList = [""] * stringSize

            for charKey, indexes in stringMap.items():
                for idx in indexes:
                    stringList[idx] = charKey
 
            decodedStrings.append("".join(stringList))

        return decodedStrings
