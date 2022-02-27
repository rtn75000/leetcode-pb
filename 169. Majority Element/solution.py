"""il existe des solutions faciles :

1- trier nums puis return nums[len(nums)//2] #TC O(nlogn) #SC O(1) :

    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
        
2- utiliser un hashtable ou on compte l'apparition de chaque val de nums puis on return la valeur la plus frequente de la hashtable donc TC et SC O(n)  :

    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
        
mais ici on recherche TC O(n) et SC O(1), pour cela on utiliseranun algo appeler Boyer-Moore Voting Algorithm :
cette algo marche car il ya forcement un majority element , l'algo utilise 2 variables count et candidates, candidates est le num qui represente a la fin le majority element. l'algo lit un num si count == 0 alors
candidate = num si count > 0 et donc cad qu'il ya deja un candidate alors on fait count-=1 si num!=candidate et count+=1 si num==candidate .
ex : rappel il ya forcement un nombre qui a une frequence n\\2
[2 2 1 1 3 2 2]  count == 0 et num==2 donc candidat = 2  , count += 1 cad count=1
 ^
[2 2 1 1 3 2 2]  count == 1 candidat ==2 et num==2 donc count+=1  cad count = 2
   ^
[2 2 1 1 3 2 2]  count == 2 candidat ==2 et num==1 donc count-=1  cad count = 1
     ^
[2 2 1 1 3 2 2]  count == 1 candidat ==2 et num==1 donc count-=1  cad count = 0
       ^
[2 2 1 1 3 2 2]  count == 0 et num==3 donc candidat ==3 et count+=1  cad count = 1
         ^
[2 2 1 1 3 2 2]  count == 1  candidat ==3 et num==2 donc count-=1  cad count = 0
           ^         
[2 2 1 1 3 2 2]  count == 0  et num==2 donc candidat = 2  , count += 1 cad count=1
             ^  
return candidat # cad 2

remarque: cette algo est logique car on a un element qui se repete plus de la moitier de n donc forcement qu'il sera sup au autre element en frequence est onc au finale ca va etre lui le candidat (l'idee de genie est 
que des que count == 0 on change de candidat) 
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
