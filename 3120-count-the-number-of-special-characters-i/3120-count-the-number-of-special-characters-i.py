class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lst=[]
        s=[]
        c=0
        for i in word:
            if i.isupper():
                if i.lower() in lst and i.upper() not in s:
                    c+=1
                    s.append(i.lower())
                    s.append(i.upper())
                lst.append(i)
            if i.islower():
                if i.upper() in lst and i.lower() not in s:
                    c+=1
                    s.append(i.upper())
                    s.append(i.lower())
                lst.append(i)


            

            # else:
            #     lst.append(i)
        return c
        