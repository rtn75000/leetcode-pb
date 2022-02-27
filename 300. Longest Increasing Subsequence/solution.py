"""il y'a deux solution une solution qui utilise seulement le dynamic programming qui a un TC O(n^2) et SC O(n) elle est la plus intuitive j'ai reussi a la trouver seul . la deuxieme solution utilise un binary
search qui n'est pas evident a trouver, cette solution a un TC O(nlogn) et un SC O(n)."""

""" # ma solution (le code est pas le mien)  # TC O(n^2) # SC O(n)
l'idee est de commence par la fin de nums et de garder le resultat de la plus longue subsequence coissante pour chaque index exemple : 
nums = [10,9,2,5,3,7,101,18]  alors on garde la taille de la plus grande subsequence croissante de chaque element dans la list LIS=[1,1,1,1,1,1,1,1]:
-> 18 a pour LIS(Longest Increasing Subsequence) [18] donc on touche pas a LIS (car l'index qui correspond est deja egale a 1)
-> 101 a pour LIS(Longest Increasing Subsequence) [101] donc on touche pas a LIS 
-> 7 a pour LIS: LIS[idx de 7]+LIS[idx de 101] (remarque LIS[7]==1 car on la pas encore modifier) ou LIS[idx de 7]+LIS[idx de 18] cad 2 donc LIS=[1,1,1,1,1,2,1,1]
-> 3 a pour LIS: LIS[idx de 3]+LIS[idx de 7] ou LIS[idx de 3]+LIS[idx de 101] ou LIS[idx de 3]+LIS[idx de 18] on a max 3 (LIS[idx de 3]+LIS[idx de 7]) donc LIS=[1,1,1,1,3,2,1,1]
->5 a pour LIS: (il ya pas LIS[idx de 5]+LIS[idx de 3] car 5>3 donc on rajoute que quand l'element qui vient est superieur ) LIS[idx de 5]+LIS[idx de idx de 7] ou LIS[idx de idx de idx de 5]+LIS[idx de 101] ou  
LIS[idx de 5]+LIS[idx de 18]  , on a max 3 donc LIS=[1,1,1,3,3,2,1,1] 
etc .. 
donc en faite on rajoute a LIS[i] tout les LIS[j] pour tout idx j sup a l'index i tel que nums[j]>nums[j] on mettra dans LIS[i] le max obtenue : 
exemple pour le 5 en haut on a fait 1(pour le 5)+LIS[idx de 7] car l'index de 7 vien apres idx de 5 et que 5<7 ,ce qui egale a 3 donc LIS[idx de 5]==3 puis on fait aussi 1+LIS[idx de 101] car l'index de 101 vien apres 
idx de 5 et que 5<101 ce qui vaut 2 et comme LIS[idx de5]==3 donc on ne change pas LIS[idx de 5] on continue avec 1+LIS[idx de 18] car idx 18 >idx de 5 et 5<18 mais comme ca vaut 2 donc on change pas LIS[idx de 5]

le TC est n^2 car chaque element de nums reparcours la liste jusqu'a la fin cad on a n+(n-1)+(n-2)+...+1 interaction qui est egale a n^2 (car la somme est egale a (n(n+1))/2)
leSC est O(n) pour la list LIS
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        LIS = [1]*n   
        for i in range (n-1,-1,-1) :  # va de la fin au debut         
            for j in range (i+1,n) :  # va de i+1 a la fin
                if nums[i]<nums[j]:   # que si la valeur est superieur alors on peut rajouter son LIS
                    LIS[i]=max(LIS[i],1+LIS[j])
        return max(LIS)  #coute O(n)
    
    
"""deuxieme solution TC O(nlogn) SC O(n) : 
code et explication : https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)
explication a l'aide d'un exemple : 

nums = [2, 6, 8, 3, 4, 5, 1] 
->prenons le premier element ans=[2]
-> 6 > 2 (cad nouveau nbr>nbr precedent) donc on peut l'ajouter , ans = [2, 6]
-> 8 > 6 donc on peut l'ajouter ans = [2, 6, 8]
-> 3 < 8  donc on peut pas l'ajouter.on va remplacer le nombre superieur le plus proche de 3 par 3 .Ici le nombre sup le plus proche de 3 est 6 donc on remplace 6 par 3 ce qui donne ans = [2,3,8]
-> 4 < 8 donc on peut pas l'ajouter.on va remplacer le nombre superieur le plus proche de 4 par 4 , donc on remplace 8 ce qui donne ans = [2, 3, 4].
-> 5 > 4 donc on peut l'ajouter ans = [2, 3, 4, 5].
-> 1 < 5 donc on peut pas l'ajouter.on va remplacer le nombre superieur le plus proche de 1 par 1 , donc on remplace 2 ce qui donne ans = [1, 3, 4, 5].
Finally, length of longest increase subsequence = len(ans) = 4.

donc l'idee est toujours de verifier si on peut rajouter l'element qu'on lit , pour que cette element soit ajouter il faut qu'il soit superieur au dernier element ajouter. mais ici si l'elemnt qu'on lit est inferieur 
au dernier element alors dans ce cas on va faire un binary schearch sur la liste de elements ajouter pour trouver l'element superieure le plus proche puis on remplacera cette element par l'element qu'on lit . puisqu'on 
passe sur tout les elements de n est que on peut faire un binary search sur c'est element ca coute O (n log n) en TC, et en SC ca coute O(n) pour ans .
"""
class Solution:  
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        for x in nums:
            if len(ans) == 0 or ans[-1] < x:    #on ajoute si sup au dernier element
                ans.append(x)
            else:
                idx = bisect_left(ans, x)     # Find the index of the smallest number >= x  #bisect_left(ans,x) fait un binary search pour trouver l'index le plus a gauche ou x peut etre introduit ca va etre forcement l'index de l'element qui est juste au dessus de lui
                ans[idx] = x  # Replace that number with x
        return len(ans)
    
    
"""ce que bisect_left(ans,x) fait : 

        def binarySearch(sub, val):
            lo, hi = 0, len(sub)-1
            while(lo <= hi):
                mid = lo + (hi - lo)//2
                if sub[mid] < val:
                    lo = mid + 1
                elif val < sub[mid]:
                    hi = mid - 1
                else:
                    return mid
            return lo   """
