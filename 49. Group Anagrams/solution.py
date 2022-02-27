"""#hashmap  #TC O(n*m) avec n mot dans strs et le mot le plus long de taille m (voir explication en bas) #SC O() (voir explication)
un anagram et donc un mot qui a les meme lettre qu'un autre mais dans un ordre different , donc on pourra trouver les differents groupes d'anagram d'apres la frequence des lettres de chaque mot .
pour cela on utilisera un hashmap (un dict) de la facon suivante : 
la key va etre une list de taille 26 chaque index de la list represente le nombre de fois qu'une lettre est presente dans le mot l'index 0 represente la frequence des a ,l'idx 1 des b , ... , l'index 25 des z.
La valeur de cette key sera une liste de mot qui on la meme key cad qui on les exactement les memes lettres.
ex : {[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:["abc","bca","cab"],
      [2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]:["acza","aazc"]}
      apres avoir construit le dict on retourne tout simplement ses valeurs
      
->TC explication : 
soit strs de taille n cad il ya n mot en tout , et m la taille du mot le plus long .
la boucle exterieur passe sur chaque mot donc coute O(n) et la boucle interieur passe sur chaque letrre du mot soit O(m) donc on a O(n*m)

->SC explication : 
on a dict qui peut contenir n key differente si aucun mot est un anagram et dans ce cas la valeur va etre que un mot pour chaque key . un mot occupe contrairement a un nombre un espace en fonction du nombre de lettre 
qu'il a (un nombre a un espace fixe alors que un mot ca depend du nombre de charactere qu'il a ) donc si m est la taille du mot le plus long un mot occupe un espace O(m) . donc puisque on peut avoir n key different 
que chaqu'une a un mot de taill m au max on occupe donc un espace O(n*m). une key contient 26 nombre donc occupe un espace O(26) donc comme on a n key diferent donc on a O(n*26) et comme chaque valeur a un taille de m 
au max alors on a O(n*(26+m)) . or comme O(n*(26+m)) = O(n*m)
donc on a SC egale O(n*m)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list) # cad par default la valeur est une list vide : []
        for s in strs:
            count = [0] * 26 # la key du dict
            for c in s:
                 # ord(c) - ord('a') pour que la valeur soit entre 0 et 25 or 'a' a une valeur ascii 97 et 'z' 122 donc pour avoir de 0 a 25 on fait ascii(char)-ascii('a')
                count[ord(c) - ord('a')] += 1  #ord(c) - ord('a') est l'idx donc count[ord(c) - ord('a')]+=1 cad on increment count de 1 a l'idx ord(c) - ord('a')
            # on ajoute au dict le mot dans la key qui lui correspond
            ans[tuple(count)].append(s) # la key d'un dict doit etre immutable donc on doit convertir la list qui est mutable en tuple qui est immutable 
        return ans.values()
