""" # double linked list + hashmap  (important concept)  # TC O(1) for get an put  # SC O(capacity)
 
code d'ici : https://www.youtube.com/watch?v=7ABFKPK2hD4&t=641s&ab_channel=NeetCode

On nous demande d'implementer un LRU cache qui store des paires key-value, on doit etre capable d'inserer (si key n'existe pas dans le cache) ou d'update (si la key existe deja dans le cache)
une paire key-val a l'aide de la fct put(key,val) en O(1), si la capacity du cache est pleine alors avant d'inserer la nouvelle paire key-val il faut supprimer le last recently used key-val. 
De plus la fct get(key) nous permetra de voir la value de la paire key-value , si la paire key-val n'existe pas dans le cache alors on return -1.
Un element est considere comme "utiliser" qd on utilse la fct get() ou put() sur cette element. 

Pour garder l'ordre chronologique des elements utilisees on utilisera une linked list, ou les element a gauche seront les 'least recently used' est les element a droite seront les 
'most recently used'.
Pour faciliter l'insertion et la supression d'un node dans la linked list on utilisera un double linked list cad une linked list dont chaque node a deux pointeur un pointeur sur l'element 
qui le precede et un sur l'element qui le suit (en effet pour supprimer un node il faut connaitre son predecesseur pour le faire pointer sur le node qui vient apres le node a supprimer donc
avec une linked list normal il faudre parcourir tout la linked list pour touver le predecesseur ce qui coute O(n) alors qu'avec une double linked list chaque node pointe directement sur le 
predecesseur). 
La double linked list va etre initialiser avec deux pseudo node un head et un tail , le node qui suit le head sera le LRU et le node qui precede le tail va etre le most recently used.

Pour trouver un node en O(1) on utilisera un dictionnary qui va pointer sur les nodes. Les key du dictionnaire vont etre les key des paire key-value du LRU cache et les valeurs du dictionnaire
vont etre un pointeur sur les nodes de la double linked list. (voir photo explication gitHub) . Le dictionnaire va etre de la taille de la capacity du LRU (car il doit avoir au max n=capacity
keys en meme temps )

Remarque : la key de la paire key-value est forcement unique dans le cache (car si on veut put(key) avec key qui existe deja alors ca va update la valeur de la key mais pas rajouter 
un nouvelle paire key-val). la val n'est pas unique 

VOIR SUPER EXPLICATION SUR GITHUB (SCHEMA DE TOUT LES FCT)

"""
#create node class for node in double linked list. 
class Node :
    def __init__(self, key, val) :
        self.key = key    # le key dans la double linked list va nous permettre de retrouver le key dans le dict qui correspond au key qui pointe sur ce node ds la double linked list 
        self.val = val 
        self.next = None  #pointer to next node 
        self.prev = None  #pointer to prev node 

class LRUCache:
    
    #init cache and double linked list
    def __init__(self, capacity: int):
        
        self.capacity =  capacity
        self.cache = {}  # {key:node}
        
        #create double linked list initialised with pseudo head an tail.
        self.head = Node(0,0)   # will point on LRU
        self.tail = Node(0,0)   # will point on MRU 
        #les faires pointer l'un sur l'autre   
        self.head.next = self.tail     # head -> tail
        self.tail.prev = self.head     #      <-
    
    # helper func : remove a node from double linked list
    def remove (self, node) :
        prev = node.prev               # previous node of the node to delete 
        nxt = node.next               # next node of the node to delete 
        # pour effacer le node on fait pointer le node qui le precede sur le node qui suit et vice-versa
        prev.next = nxt  
        nxt.prev = prev
    
    # helper function : insert a node at the end of the double linked list. 
    def insert(self,node):
        node.next=self.tail
        node.prev=self.tail.prev
        self.tail.prev.next = node 
        self.tail.prev = node 
        
        
    # return val if key in cache else -1
    def get(self, key: int) -> int:
        
        if key in self.cache:
            # since we call get we need to change the order of use :
            # delete the node pointed by key and reinsert the node at the end since it is now the MRU
            self.remove(self.cache[key])  # remarque : meme apres avoir supprimer le node le dictionnary pointe sur ce node, car remove() change les pointeurs ds la list mais pas celui du dict.
            self.insert(self.cache[key])
            return self.cache[key].val   # cache[key] is a node 
            
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache :
            # since we call put we need to change the order of use :
            # delete the node pointed by key and reinsert the node at the end since it is now the MRU
            self.remove(self.cache[key])    # remarque : meme apres avoir supprimer le node le dictionnary pointe sur ce node, car remove() change les pointeurs ds la list mais pas celui du dict.
            self.insert(self.cache[key])
            self.cache[key].val = value # update value 
            
        else :  #if key not in cache     
            self.cache[key] = Node(key,value)
            self.insert(self.cache[key]) # insert at the end of the double linked list 
            
            if len(self.cache)  > self.capacity  :  # si le dictionnaire a depasser la capacity on doit retirer le LRU
                
                # remove LRU from the list and delete the LRU from hashmap
                lru = self.head.next
                self.remove(lru)        
                del self.cache[lru.key]   # supprimer la paire key:val du dictionnaire ("del dic[key]" supprime la paire pas que la valeur)
                # (on est obliger d'avoir le key dans le node car on doit pouvoir retrouver ce key dans le dic en partant de la linked list )
            
                
                             
                
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
