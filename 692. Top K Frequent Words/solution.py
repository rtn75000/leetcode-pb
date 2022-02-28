""" #ma solution #TC O(n+klogn)  #SC O(n)
l'idee est simplement de compter la frequence de chaque lettre ensuite on cree un array qui contient (-freq,words) ensuite on transforme cette array en heap puis on prend les k premier valeurs """


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count =  Counter(words)  # TC SC O(n)  {word:freq}
        
        heap = [(-freq,word) for word,freq in count.items()]  # TC SC O(n) #-freq to get equivalent of max heap 
        
        # create heap, si la premiere valeur du tuple est egale alors heapify regarde sur le deuxieme element du tuple donc c'est pour ca que ca va etre dans l'odre alphabetique  
        heapq.heapify(heap) #TC O(n)
        
        res=[]
        while k>0 :  
            res.append(heapq.heappop(heap)[1])    #log(n) car le heap de taille n  
            k-=1 
        #la boucle coute donc O(klogn) 
        
        return res
    
#TC O(n+klogn)  
    
    
"""l'ennoncer demande O(nlogk) mais j ene vais pas m'attarder dessus les solution sont trop longue a comprendre  """
            
