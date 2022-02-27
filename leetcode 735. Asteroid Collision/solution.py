"""explication de la consigne : tout les asteroides se trouve sur une meme ligne, dans l'exemple 4 on a : asteroids = [-2,-1,1,2] . les 2 premiers asteroides se deplacent vers la gauche les 2 autres se deplacent vers la droite donc il vont jamais se rencontrer """

""" pour que il y'ai une collision il faut avoir right-> puis left<- mais si on a left<- puis right-> il ya pas de colision.
l'idee est d'utiliser un stack ou on verifie que le top est right puis on veut ajouter left dans ce cas il y'aura collision.
"""
"""Time Complexity: O(N), where N is the number of asteroids. Our stack pushes and pops each asteroid at most once (donc max 2N cad O(N)).
Space Complexity: O(N). We use a stack to keep track of the intermediate results."""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range (len(asteroids)):
            if asteroids[i]<0:  
                    while stack and stack[-1]>0 and abs(asteroids[i])>stack[-1]:  #tant que les asteroides a gauche se deplace vers la droite et celui qui se trouve a droite se deplace vers la gauche et que ceux dernier et plus gran alors on doit retirer les asteroides qui se trouve a gauche 
                        stack.pop()        
                    if stack and abs(asteroids[i])<stack[-1]:   # si l'asteroide qui se trouve a gauche qui se deplace vers la droite est superieur a celui de droite qui se deplace vers la gauche on fait rien cad on rajoute pas celui de droite au stack on continue vers la prochaine iteration  (  si l'asteroide de droite est neg et celui de gauche est neg alors abs(asteroids[i]) sera pos donc pas superieur a stack[-1])
                        continue 
                    elif stack and abs(asteroids[i])==stack[-1]: # si l'asteroide de droite est neg et celui de gauche est neg alors abs(asteroids[i]) sera pos donc pas egale a stack[-1]
                        stack.pop() 
                        continue
            stack.append(asteroids[i])
        return stack
