""" #queue iplementation with stack #TC voir chaque fonction #SC O(n) du au 2 list/array de taille O(n)
l'idee c'est d'avoir deux stack qui ici seront implementer a l'aide de 2 list : il y'aura un stack (input) ou on fait rentrer les elements que l'on veut faire rentrer dans la queue et 
un autre stack (output) d'ou on retirera les elements qu'on veut retirer de la queue (visualisation: voir solution approche num 2  ou  app) .
a chaque fois que le stack output est vide (car si il est pas vide alors le premier element rentrer se trouve au top de ce stack) et qu'on veux faire pop ou peek il va falloir
faire passer tout les elements de input vers output . 
app: 
initialisation :    
                   |  |         |  |
                   |  |         |  |
                   |  |         |  |
                   |  |         |  |
                   |  |         |  |
                   ^^^^         ^^^^
               input stack   output stack

push(1),push(2),push(3)

                   |   |         |   |
                   |   |         |   |
                   | 3 |         |   |
                   | 2 |         |   |
                   | 1 |         |   |
                   ^^^^^         ^^^^^
               input stack   output stack
               
pop()    :  fait passer tout les element de input vers output et fait pop :

                   |   |         |   |                                      |   |         |   |
                   |   |         |   |                                      |   |         |   |            
                   |   |         | 1 |              puis fait pop donc      |   |         |   |       la valeur 1 est retourne
                   |   |         | 2 |                                      |   |         | 2 |
                   |   |         | 3 |                                      |   |         | 3 |
                   ^^^^^         ^^^^^                                      ^^^^^         ^^^^^
               input stack   output stack                                 input stack   output stack
               
remarque importante :quand on implemente le stack avec une list il faut que la list se comporte comme un stack cad que on retire que le dernier qui est rentrer et que on rentre
toujours au dernier index
"""
class MyQueue:

    def __init__(self):
        self.input=[]
        self.output=[]

    def push(self, x: int) -> None:   #O(1)
        self.input.append(x)      # The newly arrived element is always added on top of stack 
 
    def pop(self) -> int:   # O(n) worst case , average O(1)
        self.peek()
        return self.output.pop()  #pop() remove the last idx of a list

    def peek(self) -> int:   #O(n) worst case (dans le cas ou on doit faire passer n element de input vers output) , average O(1)
        # faire passer les element de input vers output que si input est vide 
        if not self.output:  # if output empty
            while self.input:  # put all input elements in output
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:     #O(1)
        return not self.input and not self.output


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
