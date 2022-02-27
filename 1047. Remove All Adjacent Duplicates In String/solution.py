"""#stack #TC O(n) #SC O(n) for the stack
l'idee est simple on met un char a chaque fois dans le stack en comparrant si le top du stack est egal a la lettre qu'on veut mettre si oui alors on retir la lettre qui est 
dans le stack et on s'avance , si non alors on rajoute le nouveau char 
(j'ai ecrit ce code moi meme, c'est le meme que les meilleurs reponse officiel)"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        s=list(s)
        ans=[]
        for idx in range(len(s)):
            if ans and ans[-1]==s[idx]:
                ans.pop()
            else:
                ans.append(s[idx])
        return ''.join(ans)
