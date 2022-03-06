"""#sort # TC O(nlogn) #SC O(1) in python (use inplace sorting methode)
l'idee est de sort en fonction du start et voir si un meeting se termine apres qu'un autre meeting a commencer ."""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort() # sort en fonction des premier element de chaque array donc sort d'apres le start   # TC O(nlogn) #SC O(1) in python (use inplace sorting methode)
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]: # si le meeting i fini apres le debut du meeting i+1 alors les meetings sont overlaping donc on peut pas participer a tous
                return False
        return True
