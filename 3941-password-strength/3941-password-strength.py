class Solution:
    def passwordStrength(self, password: str) -> int:
        a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        b=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        c=['0','1','2','3','4','5','6','7','8','9']
        d=['!','@','#','$']
        z=0
        z1=[]
        
        for i in password:
            if i in a and i not in z1 :
                z+=1
                z1.append(i)
            elif i in b and i not in z1:
                z+=2
                z1.append(i)
            elif i in c and i not in z1:
                z+=3
                z1.append(i)
            elif i in d and i not in z1:
                z+=5
                z1.append(i)
        return z
                        
        