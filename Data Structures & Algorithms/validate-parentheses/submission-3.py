class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        if len(s_list)%2 == 1:
            return False
        stack = []
        for i in s_list:
            if i == '(' or i =='{' or i=='[':
                stack.append(i)
            else:
                if stack == []:
                    return False
                if i==')':
                    if stack[-1]=='(':
                        stack.remove('(')
                    else:
                        return False
                
                if i == '}':
                    if stack[-1]=='{':
                        stack.remove('{')
                    else:
                        return False
                if i == ']':
                    if stack[-1]=='[':
                        stack.remove('[')
                    else:
                        return False
        if stack==[]:
            return True
        else:
            return False



                