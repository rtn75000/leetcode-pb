"""#TC O(1) #SC O(n)
le code est de la solution(premium)
d'apres la solution du probleme les consignes sont les suivantes : le stack doit etre capable juste de montrer le min sans le retirer du stack . tout le reste c'est comme un stack normal on fait pop sur le dernier 
element cad on le retourne et on le supprime ; push met un element en haut de la stack  et top retourne l'element qui est au sommet de la stack sans le supprimer.
quand on veut avoir le min d'un array on fait tout simplement une loop qui gardera dans une variable le min qu'il rencontre a chaque fois puis a la fin on aura le min de tout le stack . ici on va utiliser un stack
qui a chaque fois qu'on fait une entre le compare au min et a chaque etape on garde le nouveau min comme ca si on fait pop on a meme les min precedent. dans le stack on introduira 2 valeur : la valeur a introduire et 
le min obtenue jusqu'a present.
"""
class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        
        # If the stack is empty, then the min value
        # must just be the first value we add
        if not self.stack:
            self.stack.append((x, x))
            return

        current_min = self.stack[-1][1]
        self.stack.append((x, min(x, current_min))) #on compare toujour la valeur actuelle avec le min obtenue jusqu'a present 
        
        
    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
