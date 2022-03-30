""" #my sol #logic #TC O(n+m) where n and m are lengths of numbers # SC O(max(m,n)) because result will have this length

l'idee est de simplement additionner les bit en commenceant par la droite et en prennant en compte la retenue (carry) ,il ya plusieur possibiliter :
carry = 0 :
    - 0+0 = 0 et carry = 0
    - 0+1 = 1 et carry = 0
    - 1+1 = 1 et carry = 1 
carry = 1 :
    - 0+0 = 1 et carry = 0
    - 0+1 = 0 et carry = 1
    - 1+1 = 1 et carry = 1
    """
class Solution:
    def addBinary(self,a: str, b: str) -> str:
        
        retenu = 0
        size_b = len(b)
        size_a = len(a)
        res = ['0'] * (size_a + 1) if size_a > size_b else ['0'] * (size_b + 1)  # le resultat et de la taille du nombre le plus grand
        size_res = len(res)
        
        # size_1 va etre la taille du nombre le plus petit et size_2 le plus grand 
        if size_a < size_b:  
            size_1=size_a
            size_2=size_b
        else : 
            size_1=size_b
            size_2=size_a
            
        for i in range(size_1): #on parcours le plus petit nombre 
            
            if int(b[size_b - 1 - i]) + int(a[size_a - 1 - i]) == 0 and retenu == 0: 
                res[size_res-1 - i] = "0"
                
            elif (int(b[size_b - 1 - i]) + int(a[size_a - 1 - i]) == 1 and retenu == 0) or (int(b[size_b - 1 - i]) + int(a[size_a - 1 - i]) == 0 and retenu == 1) :
                retenu = 0
                res[size_res-1 - i] = "1"
                
            elif (int(b[size_b - 1 - i]) + int(a[size_a - 1 - i]) == 2 and retenu == 0) or (int(b[size_b - 1 - i]) + int(a[size_a - 1 - i]) == 1 and retenu == 1):
                retenu = 1
                res[size_res-1 - i] = "0"
                
            elif int(b[size_b - 1 - i]) + int(a[size_a - 1 - i]) == 2 and retenu == 1:
                retenu = 1
                res[size_res-1 - i] = "1"
                
        greatest = b if size_a < size_b else a
        
        for i in range(size_1 , size_2): # on parcours le reste du grand nombre 
            
            if retenu:
                if int(greatest[size_2 - 1 - i]) + retenu == 2:
                    retenu = 1
                    res[size_res-1 - i] = '0'
                elif int(greatest[size_2 - 1 - i]) + retenu == 1:
                    retenu = 0
                    res[size_res-1 - i] = '1'              
                if i == size_2-1 and retenu == 1:
                    res[0]='1'
                    break
            else:
                res[size_res-1-i] = greatest[size_2 - 1 - i]
                
                
        res[0] = '1' if retenu else '0'
        output = ''.join(res)
        return output[1:] if output[0]=='0' else output 

    
""" pas ma sol # bcp plus simple #TC O(n+m) where n and m are lengths of numbers # SC O(max(m,n)) because result will have this length 
sol d'ici : https://leetcode.com/problems/add-binary/discuss/743698/Python-8-Lines-neat-solution-Explained"""


class Solution:
    def addBinary(self, a, b):
        i, j, summ, carry = len(a) - 1, len(b) - 1, [], 0
        while i >= 0 or j >= 0 or carry:
            d1 = int(a[i]) if i >= 0 else 0
            d2 = int(b[j]) if j >= 0 else 0
            summ += [str((d1 + d2 + carry) % 2)]
            carry = (d1 + d2 + carry) // 2
            i, j = i-1, j-1 
        return "".join(summ[::-1])
    
    
 
