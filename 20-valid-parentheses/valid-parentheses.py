class Solution:
    def isValid(self, s: str) -> bool:
        
        l = []
        x = True
        for c in s:
            if c in "({[":
                l.append(c)
            elif len(l) > 0:
                if (c == ")" and l[-1] == "(") or (c == "}" and l[-1] == "{") or (c == "]" and l[-1] == "["):
                    l.pop()
                else:
                    x = False
                    break
            else:
                x = False
                break

        return x and len(l) == 0 
