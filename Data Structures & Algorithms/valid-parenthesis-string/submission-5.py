class Solution:
    def checkValidString(self, s: str) -> bool:
        opening_paren = []
        stars = []

        for i in range(len(s)):
            if s[i] == '(':
                opening_paren.append(i)
            elif s[i] == ")":
                if len(opening_paren) > 0:
                    opening_paren.pop()
                elif len(stars) > 0:
                    stars.pop()
                else:
                    return False
            else:
                stars.append(i)
        print(opening_paren, stars)
        for i in range(len(opening_paren)):
            if stars:
                if stars[-1] > opening_paren[-1]:
                    stars.pop()
                    opening_paren.pop()
                else:
                    stars.pop()
            else:
                return False
            print(opening_paren, stars)
    
        print(opening_paren, stars)
        if opening_paren:
            return False

        print(opening_paren, stars)

        return True

