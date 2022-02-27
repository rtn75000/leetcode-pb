"""# my sol #TC O(n) #SC O(1) car on utilise un extra space constant (O(26) pour freq)
l'idee est d'utiliser un dict qui va compter la frquence de chaque lettre ensuite mettre toute les frequences qui sont les valeurs de dict (i yen a max 26) dans la list freq puis trier cette liste dans l'ordre decroissant
(cout O(26log26) cad O(1)) . on veut pas de valeur double donc pour cela il faut que la list des frequence soit strictement decroissante , si on a par exemple freq=[5,5,5,5,4,4] alors la list n'est pas strictement 
decroissante , pour qu'une list soit strictement decroissante il faut que l'element i soit sup a l'element i+1 donc si cette condition n'est pas respecter cad freq[i]<=freq[i+1] alors la list n'est pas strictement 
decroissante. pour que la list soit strictement decroissante il faut que ds le cas ou freq[i]<=freq[i+1] on devra changer freq[i+1] afinn qu'il soit inf a freq[i] donc on ferra : freq[i+1]=freq[i]-1  ainsi freq[i]
<=freq[i+1]. la consigne demande de retourner le nombre d'element retirer pour que la frequence soit unique cad pour que freq soit strictement ecroissant donc a chaque fois qu'on modifie freq[i+1] il faut garder le nombre
retirer a freq[i+1] , ce nombre est egale a la difference entre l'ancien freq[i+1] et le nouveau freq[i+1] qui est egale a freq[i]-1 apres la modif donc on rajoute a output :   (freq[i+1]-(freq[i]-1)). remarque: si la 
frequence de freq[i] est egale a 0 alors ca veut dire que la frequence de tout les elements a venir doit etre egale a 0, et donc on peut rajouter la somme des element qui nous reste a output car on doit tous les effacer.


app:  s="edddcccfbbbaaa"
->on creer un dict des frequences cout TC O(n) car on passe sur s , SC O(26)=O(1) car il ya que 26 lettres au max : d={e:1,d:3,c:3,f:1,b:3,a:3}
->on creer une list des frequence a l'aide de d en prenant simplement les valeur de d  : freq=[1,3,3,1,3,3]
->on tris la liste des frequence dans l'ordre decroissant ,TC O(26log26)=O(1) (pas nlogn car il ya max 26 frequence car max 26 lettres): freq=[3,3,3,3,1,1]
->on corrige la list afin qu'on puisse avoir un ordre strictement decroissant :
   freq=[3,3,3,3,1,1]   freq[i+1]>=freq[i] donc pas strictement decroissant donc freq[i+1]=freq[i]-1 cad freq[i+1]=2. pour savoir cbm d'element on etait retirer a freq[i+1] on calcule la distance
         ^              entre l'ancien freq[i+1] et le nouveau freq[i+1] cad on calcule freq[i+1]-(freq[i]-1) cad 3-2 cad 1 donc on a retirer 1 nombre dc output+=1 (output == 1)
         i
   freq=[3,2,3,3,1,1]   freq[i+1](3)>=freq[i](2) donc pas strictement decroissant donc freq[i+1]=freq[i]-1 cad freq[i+1]=2-1=1. pour savoir cbm d'element on etait retirer a freq[i+1] on calcule 
           ^            freq[i+1]-(freq[i]-1) cad 3-1 cad 2 donc on a retirer 2 nombres dc output+=2 (output == 3)
           i
   freq=[3,2,1,3,1,1]   freq[i+1](3)>=freq[i](1) donc pas strictement decroissant donc freq[i+1]=freq[i]-1 cad freq[i+1]=1-1=0. pour savoir cbm d'element on etait retirer a freq[i+1] on calcule 
             ^          freq[i+1]-(freq[i]-1) cad 3-0 cad 3 donc on a retirer 3 nombres dc output+=3 (output == 6)
             i
   freq=[3,2,1,0,1,1]   ici on peut pas continuer avec la meme logique car ca va faire freq[i+1]=-1 et apres on va faire output+=freq[i+1]-(freq[i]-1) cad output+=(1-(0-1)) cad output+=2 ce qui  
               ^        est faux,l'erreur viens car on calcule la distance entre 1 et -1 une frequence ne peut etre negative, ca va faire comme ci on enleve des lettres qui n'existe pas
               i        donc a partir que freq[i] egale 0 alors tout le reste doit etre egale a 0 et donc on retire tout les lettres qui nous reste donc on fait output+=sum(freq[i+1:len(freq)])
                        cad output+=2 (output==8) et on a fini l'algo on peut faire return
"""

class Solution:
    def minDeletions(self, s: str) -> int:
        d=defaultdict(int)
        freq=[]  #SC O(26)
        output=0
        for char in s :
            d[char]+=1
        for val in d.values() :   #O(26)
            freq.append(val)
        freq.sort(reverse=True)  # sort in decreasing order 
        for i in range (len(freq)-1): # O(26)
            if freq[i+1]>=freq[i]:
                if freq[i] == 0 :
                    output+=sum(freq[i+1:len(freq)])
                    return output
                else:
                    output+=(freq[i+1]-(freq[i]-1))
                    freq[i+1]=freq[i]-1       
        return output
    
    
""" autre solution plus courte avec TC et SC les memes que la sol precedente .
l'idee est de creer un dictionnaire de frequence comme dans la solution precedente (sout TC O(n) SC O(26) car 26 lettres de l'alphabet) , ensuite on passe sur ce dictionnaire (de taille 26 au max) et on rentre la 
frequence qu'on lit , dans un set

app:  s="edddcccfbbbaaa"
->on creer un dict des frequences cout TC O(n) car on passe sur s , SC O(26)=O(1) car il ya que 26 lettres au max : d={e:1,d:3,c:3,f:1,b:3,a:3}
-> on traverse les valeur de dict cad les frequence , et on verifie si cette frequence a deja etait vu ,pour cela on utilise une list: used, qui garde les frequences vu.
    -d.val == 1 comme 1 est pas dans used alors on l'ajoute : used=[1], next val : 
    -d.val == 3 comme 3 est pas dans used alors on l'ajoute : used=[1,3], next val : 
    -d.val == 3 comme 3 est dans used alors d.val-=1 ainsi que res+=1 car on a retirer un char (res==1). donc d.val=2 comme 2 n'est pas dans used on l'ajoute: used=[1,3,2], next val :
    -d.val == 1 comme 1 est dans used alors d.val-=1 (d.val==0) et res+=1 (res==2) . comme on a 0 alors on a pas besoin de verifier si il est dans used on peut le rajouter directement 
     (car plusieur 0 ca veut pas dire qu'il ya des lettres qui on la meme frequence car 0 veut dire que cette lettre n'existe pas):used=[1,3,2,0] , next val :
    -d.val == 3 comme 3 est dans used alors d.val-=1 (d.val==2) et res+=1 (res==3) . comme 2 est dans used alors d.val-=1 (d.val==1) et res+=1 (res==4). comme 1 est dans used alors 
     d.val-=1 (d.val==0) et res+=1 (res==5). comme on a 0 on l'ajoute sans besoin de verifier: used=[1,3,2,0,0] next val :
    -d.val == 3 comme 3 est dans used alors d.val-=1 (d.val==2) et res+=1 (res==6) . comme 2 est dans used alors d.val-=1 (d.val==1) et res+=1 (res==7). comme 1 est dans used alors 
     d.val-=1 (d.val==0) et res+=1 (res==8). comme on a 0 on l'ajoute sans besoin de verifier: used=[1,3,2,0,0,0] . 
     
     on a fini car on est passer sur toutes les val de d donc on return res cad 8.
"""

class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = collections.Counter(s)
        res = 0
        used = [] # remarque : on aurait peu utiliser un set ici a la place et ecrire used=set() l'interet est qu'un set est implementer a l'aide d'un hashtable et donc les actions search/insert/delete coute O(1) en average (si le load factor du hash table est elever c'est O(n)), alors qu'un array ca lui coute O(n) ces actions. mais ici comme used peut etre de taille max 26 car il ya max 26 frquence donc meme si apres on utilise "freq in used" dans le while cad on fait un search de freq dans used cela coute O(1) en moyenne si used est un set , on prefere ici que used soit une list caar le search ds notre cas coute O(26) cad il ya pas un n elever donc ca vaut pas le cout que used soit un set car c'est plus long a implementer.
        for freq in cnt.values():
            #tant que la freq est sup a 0 et qu'on a deja rencontrer cette frequence car elle est deja dans used (si elle est egale a 0 meme si elle est deja dans le used c'est pas
            #grave car freq==0 ca veut dire que la lettre n'est plus dans s donc on peut avoir autant de freq==0 ) alors on fait freq-=1 et donc on fait res+=1 car on a retirer une lettre 
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.append(freq) #remarque: si on utilise un set on doit faire used.add(freq)
        return res
