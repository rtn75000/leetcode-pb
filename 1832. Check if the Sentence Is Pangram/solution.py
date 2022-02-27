class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hash={} 
        for i in range (0,26):
            hash[i]=0
        for i in sentence :
            hash[ord(i)%97]+=1  
        for i in range (0,26):
            if hash[i]==0:
                return False
        return True    
# l'idee c'est de cree un tableau de key 0 a 26 puis d'incrementer a chaque fois que on a une lettre , a=0...z=26 (prendre la valeur ascii de a(97)et faire modulo 97)
# on peut faire la meme chose avec un array de 0 a 26
""" solution sans hash table:

        def checkIfPangram(self, sentence: str) -> bool:
            for i in range(97,123):
                if chr(i) not in sentence:
                    return False
            return True               """
   
