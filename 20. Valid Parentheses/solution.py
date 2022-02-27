
"""introduction stack : 
rappel une stack est une structure de donnees LIFO donc les actions elementaire tel que push et pop sont O(1). en python elle peut etre implementer avec une list  dans ce cas le push ce fait a l'aide de append et pop 
a l'aide de pop() mais le cout de ces actions est de O(n).elle peut etre aussi implementer a l'aide de deque (qui est une list a double sense donc l'entre et  sortie d'elements de la tete et de la fin est O(1)) ici 
aussi push ce fait a l'aide de append et pop a l'aide de pop() mais la differences est que ces actions sont O(1). (voir article : https://www.geeksforgeeks.org/stack-in-python/)
"""
"""# TC: O(n) because we simply traverse the given string one character at a time and push and pop operations on a stack take O(1)O(1) time.
# SC :O(n) as we push all opening brackets onto the stack and in the worst case, we will end up pushing all the brackets onto the stack. ex: ((((((((((
l'idee est de push tout les opening brackets dans la stack et si on rencontre un closing bracket on verifie l'element qui est au top de la stack si c'est un opening bracket du meme type alors on le pop et on continue
l'algo si ce n'est pas le cas (ou si le stack est vide) alors on l'expression est invalide.si on a a la fin un stack qui lui reste des elements cad que on a pas trouver toute les paires alors l'epression est invalide  """

class Solution(object):
    def isValid(self, s):
 
        # The stack to keep track of opening brackets.
        stack = deque()

        # Hash map for keeping track of mappings. T
        dictio = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:    
            
                # if we have an opening bracket, simply push it onto the stack.
                if char in dictio.values():
                    stack.append(char)
                # If the character is an closing bracket (key of the dictionnary)    
                elif char in dictio.keys():
                    # if stack empty or the top element of the stack is not the corresponding opening bracket then Pop the topmost element from the stack
                    if not stack or dictio[char] != stack.pop():
                        return False
                else :
                    return False

        # In the end, if the stack is empty, then we have a valid expression .
        # The stack won't be empty for cases like ((()
        return not stack    
