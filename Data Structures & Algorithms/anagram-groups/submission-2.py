class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strings:
            key = [0] * 26
            for char in string:
                key[ord(char) - 97] += 1

            groups[tuple(key)].append(string)

        return list(groups.values())

        