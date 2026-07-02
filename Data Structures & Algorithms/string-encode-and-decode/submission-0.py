class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i))+"#"+i
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while (i<len(s)):
            num = ''
            str_n = ''
            if s[i].isdigit():
                while(s[i]!='#'):
                    num += s[i]
                    i+=1
                i+=1
            int_num = int(num)
            while int_num!=0:
                str_n += s[i]
                i+=1
                int_num-=1
            res.append(str_n)
        return res



    