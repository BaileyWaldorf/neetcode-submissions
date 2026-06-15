class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = "%"
        encoded_string = ""

        for s in strs:
            encoded_string += f"{len(s)}{delimiter}{s}"
        
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        string_len = 0
        words = []
        idx = 0

        while idx < len(s):
            print("working on = ", s[idx])
            if s[idx] == "%":
                idx += 1
                if string_len == 0:
                    words.append("")
                else:
                    words.append(s[idx:idx+string_len])
                    idx += string_len
                    string_len = 0
            elif s[idx].isdigit():
                    string_len *= 10
                    string_len += int(s[idx])
                    idx += 1
            else:
                idx += 1

        return words
