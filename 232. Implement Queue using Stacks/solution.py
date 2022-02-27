"""l'idee c'est d'avoir deux stack qui ici seront implementer a l'aide de 2 list : il y'aura un stack (input) ou on fait rentrer les elements que l'on veut faire rentrer dans la queue et un autre stack (output) d'ou on retirera les elments qu'on veut retirer de la queue (visualisation: voir solution approche num 2 )
a chaque fois que output et vide et que on veux faire pop ou peek il va falloir faire passer les elements de input vers output.
(quand on implemente le stack avec une list il faut que la list se comporte comme un stack cad que on retire que le dernier qui est rentrer et que on rentre toujours au dernier index)
"""
class MyQueue:

    def __init__(self):
        self.input=[]
        self.output=[]

    def push(self, x: int) -> None:   #O(1)
        self.input.append(x)

    def pop(self) -> int:   #O(n) worst case , average O(1)
        self.peek()
        return self.output.pop()  #pop() remove the last idx of a list

    def peek(self) -> int:
        if not self.output:  # if output empty
            while self.input:  #put all input elements in output
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
