class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        if len(s_list)%2 == 1:
            return False
        stack = []
        for i in s_list:
            if i == '('  :
                stack.append(')')
            elif i =='{':
                stack.append('}')
            elif i=='[':
                stack.append(']')
            else:
                if stack==[]:
                    return False
                if i != stack.pop():
                    return False
        if stack==[]:
            return True
        else:
            return False



                