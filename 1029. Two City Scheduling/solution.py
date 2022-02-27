"""#greedy  # TC O(nlogn) pour le sort #SC O(1) pour python 
on veut savoir quelle est le cout minimal tel que n personnes voyagent vers la ville A et n personnes voyagent vers la ville B. Pour cela on fait la difference entre le cout du voyage vers A et le cout du voyage vers B.
ex : costs=[[10,20],[30,10],[20,50],[40,50]] la difference costs[0]-costs[1] ca donne diff= [-10,20,-30,10]  , prenons par exemple -10 cela veut dire que en voyageant a la ville A au lieu de la ville B on economise 10 et
donc si on va vers B on va payer 10 de plus, si on prend la valeur 20 ca veut dire que en choisissant la ville A a la place de B on va faire un surplus de 20 et si on va vers B on economisera 20 . donc on a interet a
prendre les n plus petit de diff car se sont les plus grandes economies qu'on peut faire ex si diff = [-10,20,-30,10] on trie diff ca donne diff=[-30,-10,10,20] donc si n voyages vers A et n voyage vers B on devrait 
choisir -30 et -10 vers A car dans ce cas on fait une econmie de 40 (si on voyage vers b dans ce cas ca nous coutera 40 de plus) , et on devrait choisir 10 et 20 vers B (si on va a la place vers A ca nous coutera 30 de
plus ) .
enfait quand on range d'apres l'ordre croissant de A-B alors ca range d'apres l'ordre decroissant de B-A cad que donc es n premier sont les meilleur pour A et les n dernier sont les meilleurs pour B . (c'est logique car si A-B donne par ex : [-10 -5 15 45] alors le B-A donne[-45 -15 5 10] donc le 45 de A-B et le meilleur de B-A etc...)"""


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort by a gain which company has 
        # by sending a person to city A and not to city B
        costs.sort(key = lambda x : x[0] - x[1])  # le sort by key va nous donner cost trier par rapport a la diference de chaque paire  
        total = 0
        n = len(costs) // 2
        # To optimize the company expenses,
        # send the first n persons to the city A
        # and the others to the city B
        for i in range(n):
            total += costs[i][0] + costs[n+i][1]  #cost[i][0] va selectionner les n premier de A et costs[n+i] va selectionner les n autres de B
        return total
