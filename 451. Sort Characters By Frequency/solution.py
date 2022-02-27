"""premiere solution :  #hashmap  #built-in sort  #TC O(n+62log62)  #SC O(n)     # n=len(s)
l'idee est de simplement compter la frequence de chaque charactere puis trier dans l'ordre decroissant par rapport au frequence puis on append chaque lettre*frequence dans l'ordre du trie
remarque : un char ici peut etre un chiffre , une lettre majuscule ou minisucle donc en tout 26+26+10=62 possibilites .  """

class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)  # TC O(n) SC O(62)
        arr = [[freq, c] for c, freq in cnt.items()]  # TC SC O(62) car max 62 items dans cnt 
        arr.sort(key=lambda x:x[0],reverse=True)  # sort in decreasing order by frequency (chaque element x qui est [freq,c] est trier par rapport a x[0] cad par rapport a freq) #TC O(62log62)
        ans = []  # va etre de la taille de la reponse qui sera composer de tout les char de s donc SC O(n)
        for freq, c in arr:    # voir remarque en bas pk on append de la sorte  #TC O(62)
            ans.append(freq * c)
        return "".join(ans)

"""remarque tres importante : si on utilise pas un array pour la reponse est qu'on fait tout simplement ans='' puis dans le for qui vient apres on fait ans+(freq * c) et tout ca pour economiser la taille du array et 
avoir en tout SC O(62) et pas O(n) ca va couter bcp plus cher en TC . car le '+' de la concatenation de 2 string dans python marche de la facon suivante : string object en python sont immutable cad on ne peut modifier 
une string donc si on fait str1+str2 python ne peut copier str2 dans str1 car on ne peut modifier une string donc ce que python fait c'est qu'il cree un nouveau string object ou il va copier lettre par lettre les lettres
de str1 et de str2 ca va donc coute O(len(str1)+len(str2)). 
si on veut append n lettre a une string vide ca va coute O(n^2),
explication : disons qu'on veut ajouter a s="" les lettres 'abcd' une par une ca va donner :
''+'a' -> 1 iterations
'a'+ 'b' -> 2 iteration car python cree une copie et append une lettre par lettre
'ab' + 'c' -> 3 iterations ( on append a la nouvelle copie a puis b puis c)
'abc' + 'd'  -> 4 iterations
donc au total on a 1+2+3+4 iterations cad on a une suite dont la somme est O(n^2) (car la somme est egale a (n(n+1))/2)

pour append une string en python en general on cree un array au quel on va append les n lettres ce qui coute O(1)*n puis on va faire "".join(array) ce qui coute O(n) donc en tout on va avoir O(2n) cad TC O(n) , 
SC est egale a O(n) car on utilise un array en plus 

sources : 
https://www.quora.com/How-fast-is-string-concatenation-in-Python  
https://python.plainenglish.io/concatenating-strings-efficiently-in-python-9bfc8e8d6f6e
"""    



"""2 eme solution : #bucket sort #TC/SC O(n) 
la frequence est entre 0 et len(s) cad entre 0 et n donc on va utiliser un bucket sort cad on va simplement creer des bucket(array d'element) de 0 a n et on va mettre les characteres dans le 
bucket qui correspond a la frequence de chacun. 
on va ensuite simplement parcourir les buckets en commencant par la fin car elle represente la plus grande frequence , puis on va append les different caracteres qui sont present dans chaque bucket fois la frequence.
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)  # TC O(n)  SC O(62)
        n = len(s)
        bucket = [[] for _ in range(n+1)] # TC O(n) SC O(n)
        for c, freq in cnt.items(): # TC O(62)
            bucket[freq].append(c)
        
        ans = [] # a la fin SC O(n)  
        for freq in range(n, -1, -1): # O(n)
            for c in bucket[freq]: # parcours tout un meme bucket 
                ans.append(c * freq)
        return "".join(ans)


    
"""solutions d'ici : https://leetcode.com/problems/sort-characters-by-frequency/discuss/1503201/C%2B%2BPython-3-solutions%3A-Sorting-Bucket-Sort-O(N)-Clean-and-Concise"""
