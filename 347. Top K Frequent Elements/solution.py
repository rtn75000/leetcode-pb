"""#1er solution #la consigne veut un meilleur TC que ca  # ma solution #hash table #max-heap priority queue  #TC O(n+klogn)  #SC O(n)   n==len(nums)
on utilise simplement un max heap qui contiendra des tuples (freq,num) , il sera trier par rapport au frequence . ensuite on fait pop k fois et on prend le nbr et pas la frequence car on veut les k nbrs qui ont la 
plus grandes frequences. 
"""
class Solution:
    def topKFrequent(self, nums, k):
        
        dic = Counter(nums)  #TC / SC O(n)       #   {num:freq...} attention et pas { freq:num }
        print(dic)
        # dic.items return tuples : (key,val) so here (num,freq)  
        # on fait -freq car on veut max heap apres et comme il ya que minheap ds python dc pour que ca revient au meme on fait neg sur les frequence 
        # on fait(-freq,num) et pas (num,-freq) car on veut que le heap soit arranger par rapport a freq donc il faut que freq soit en premier. 
        heap=[(-freq,num) for num,freq in dic.items()]     #TC / SC O(n)  
        heapq.heapify(heap) # O(n)  # heapifyarrange par rapport au premier element de chaque tuple donc arrange par rapport a la frequence. 
        output=[]
        for _ in range (k) :
            output.append(heapq.heappop(heap)[1])    # on veut ds le output les num avec la plus grandes freuences  #O(logn)
        return output 

    
"""#2eme sol #not my sol  #hash-table #bucket sort #TC O(n)  #SC O(n)

solution prise d'ici : https://leetcode.com/problems/top-k-frequent-elements/discuss/1502514/C%2B%2BPython-2-solutions%3A-MaxHeap-Bucket-Sort-Clean-and-Concise

remarque consernant la consigne : 
-la reponse est unique donc on peut pas avoir par ex nums=[1,2] et k=1 car le plus frequent et ou 1 ou 2 donc la reponse est pas unique. (si k=2 c'est bn),donc on va forcement rendre
tout le bucket on ne peut rendre qu'une partie car ca voudrais dire que on aurait peu choisir l'autre donc pas reponse unique.

l'idee c'est d'utiliser le principe de bucket sort cad on a une liste de 1 a n qui represente la frequence et dans chaque case/"bucket" on met dans une 
liste les nombres qui on cette frquence dans le array de base ex: nums=[1,2,1,2,3,4,4,4] ca donne: 
[1]->[3]
[2]->[1,2]
[3]->[4]

ensuite on commence a lire par le dernier bucket le premier element et on rajoute les element a la reponse tant que on a pas trouver tout les k elements les plus frequent.
"""
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt = Counter(nums)   #TC / SC O(n)       #   {num:freq...}
        
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        for num, freq in cnt.items():
            bucket[freq].append(num)
            
        bucketIdx = n
        output = []
        while k > 0:
            while not bucket[bucketIdx]:  # Skip empty bucket
                bucketIdx -= 1            #on va au bucket en dessous 
                
            for num in bucket[bucketIdx]:   
                if k == 0: 
                    break     # on a trouver les k elements les plus frquent donc on a fini 
                output.append(num)           
                k -= 1
                
            bucketIdx -= 1  
            
        return output
    
    
    
"""meme chose que le code precedent juste une version un peu differente  , plus compliquer que la precedente mais je l'ai mit car javais fait deja une remarque sur ce code donc je l'ai garder
meme si apres j'ai trouver la version d'en haut qui est plus simple a comprendre. 

solution prise d'ici : https://leetcode.com/problems/top-k-frequent-elements/discuss/740374/Python-5-lines-O(n)-buckets-solution-explained

l'idee est la meme on va utiliser un bucket sort les bucket vont contenier les nombres qui correspondent a la frequence du bucket 
ex:
nums=[1,2,1,2,3,4,4,4] ca donne: 
[1]->[3]
[2]->[1,2]
[3]->[4]
la difference est que dans cette version : 
on met tout les elements des buckets dans une seule liste en commencant par le premier element du premier bucket et en terminant par le dernier element du dernier bucket . 
donc ici ca donne  ca : [3,1,2,4] . les k nombres les plus frequents sont les k derniers nombres de cette list, si par exemple on veut les 2 nbrs les plus frequents on prend les 2 derniers cad:
4 puis 2 soit [4,2].
"""


class Solution:
    
    def topKFrequent(self, nums, k):
        
        bucket = [[] for _ in range(len(nums) + 1)]  # [[], [] ,..., [], []]
        
        Count = Counter(nums).items()  #counter nous donne un dictionnaire {nbr:freqence} , items() rend une liste de tuple (key,val) : [(k1,v1),(k2,v2)...]
        for num, freq in Count:
            bucket[freq].append(num) 
            
        flat_list = list(chain(*bucket))    #The single star * unpacks the sequence/collection into positional arguments, so you can do this: def sum (a,b) puis a l'appel val=(1,3) puis sum(*val). chain() importe de itertools prends une serie d'iterable est en en fait qu'un iterable ex : a =[1,2] b=[3,4] alors l=list(chain(a,b)) ca veut dire que l==[1,2,3,4] (voir remarque en bas)
        
        return flat_list[::-1][:k] #car si on a par exemple a=[3,2,1] alors a[::-1] ca donne [1,2,3] donc quand on fait a[::-1][:k] c'est comme si on fait [:k] sur [1,2,3] donc si on prend k=2 ca donne [1,2]
    
    
"""  remarque on peut faire flat une liste de liste cad [[]...[]] comme ca aussi :
     flat_list = [item for sublist in t for item in sublist]   
     ca revient a faire ca : 
     flat_list = []
     for sublist in t:  # Given a list of lists t
         for item in sublist: 
             flat_list.append(item)
    """
