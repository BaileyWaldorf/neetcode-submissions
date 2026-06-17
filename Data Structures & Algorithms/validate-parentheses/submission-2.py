class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        stack = []

        for c in s:
            # opening bracket
            if c in pairs.values():
                stack.append(c)
            elif stack:
                # close bracket
                open_bracket = stack.pop()
                if pairs[c] != open_bracket:
                    return False
            else:
                return False
        
        return len(stack) == 0