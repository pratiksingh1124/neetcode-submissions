class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[': #start charcater
                stack.append(ch) #adds current

            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()

                if ch == ')' and top != '(':
                    return False
                if ch == '}' and top != '{':
                    return False
                if ch == ']' and top != '[':
                    return False

        return len(stack) == 0 #t or f acc to append and pop