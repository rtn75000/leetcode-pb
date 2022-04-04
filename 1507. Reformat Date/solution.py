""" #TC O(n) #SC O(12) cad O(1)""" 
class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split(" ")  #TC O(n)
        dic = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun" : "06", "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12", }
        #si il ya deux chiffre dans les jours  : 
        if date[0][1].isdigit() : 
            return date[2] + '-' + dic[date[1]] + '-' + date[0][:2]
        else :
            return date[2] + '-' + dic[date[1]] + '-0' + date[0][:1]   # si il ya que un chiffre on dot rajouter un zero avant 
