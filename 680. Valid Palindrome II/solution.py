""" #pointers #recursion #TC O(n)  #SC O(1)

l'idee est simple :  un mot est un palindrome si il a une symetrie centrale cad que si on part des deux extremitees du mot et on compare les extremites a chaque fois 
en s'avanceant vers le milieu alors les paires de lettres qu'on obtient sont identique . 
ex: 'abcdcba'   a==a , b==b,  c==c et d==d  donc c'est un palindrome. 

l'algo va donc comparer les extremites et si deux lettres (current extremites) ne corresponde pas alors on a deux possibilite soit de supprimer la lettre a gauche soit de supprimer la 
lettre a droite il faut donc essayer les deux possibilites (voir exemple pq il faut essayer les deux ) . ex: si on 'abbca' alors a==a c'est bon mais ensuite on a b!=c donc ou soit on 
supprime b et il nous reste a comparer 'bc' soit on supprime 'c' et il nous reste a comparer 'bb'. si on prend le choix de supprimer 'b'  ensuite on va avoir 'bc' est donc comme b!=c il
va falloir faire encore une modif donc false car plus de 1 modification en tout . si on prend le choix de supprimer 'c' alors il nous reste 'bb' et comme b==b il ya pas de modif a faire
donc on aura en tout que une modif donc le mot est un palindrome apres max un delete (c'est pour cela qu'il faut essayer les deux choix car un choix rendra False alors que l'autre rendra True). 


 
analyse TC : 

verify peut s'appeler recursivement qu'une fois car l'appel recursive se passe en cas de modification , donc comme on peut faire qu'une modif donc apres une modif si il faut en faire 
une autre alors verify va rendre False (il ne va pas s'appeler recursivement). donc au pire verify va passer sur une partie des lettres et faire un appel recursive qui va lui passer
sur le reste des lettres donc en tout on va passer sur tout les lettres au pire cad O(n) .



petite remarque : cette algo marche avec valid palindrom III ,la bas on peut faire k modif donc il va falloir faire la meme chose sauf que on doit ecrire 'if counter == k: return false' 
a la place de 'if counter == 1: return False' (l'analyse du TC la bas doit etre interessante : la bas il va avoir k apppel recursif alors qu'ici il ya que un appel recursif  )
( dans le cas general ou on aura droit a k changement alors verify coute au mieu O(n) si il ya pas recursion (le while va couter O(n)) et au pire verify s'appel recursivement 2 fois 
sur n-1 a chaque appel recursive et dans ce cas verify lui meme coute O(1) car a chaque premiere iteration de while il y'a l'appel recursif (donc while a que une iteration il
coute O(1)) et donc la relation de recurence de verify est T(n)=2T(n-1)+c et donc TC=O(2^n) . Donc le TC du cas generale est O(2^n) (on poura utiliser @lru_cache pour economiser 
les recurrence deja calculer) ). (dans ce cas SC va aussi etre O(2^n))
 

"""

class Solution(object):
    def validPalindrome(self, s):
        
        def verify(s, left, right, counter=0): #counter nous dit le nombre de modif faite 
            
            while left <= right:   
                
                if s[left] != s[right]: # alors on doit supprimer un caractere 
                    
                    if counter == 1:   # si on a deja fait une modif alors la ca va etre la deuxieme modif donc return false car une modif autorise.
                        return False
                    
                    else:     # si on a pas fait de modif alors on on peut faire une modif donc faire la modif  :                        
                        # il faut essayer les deux possibilites soit supprimer la lettre a gauche soit la lettre a droite (comme expliquer en haut)
                        return verify(s, left+1, right, counter+1) or verify(s, left, right-1, counter+1) 
                    
                else: # si les extremites sont egale alors passer au extremites plus interieur 
                    left += 1
                    right -= 1
                    
            return True
        
        return verify(s, 0, len(s)-1)
