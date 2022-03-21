"""#hashmap #TC O(n) #SC O(n)
cette question est tres simple ..."""
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = defaultdict(int)
        for domain in cpdomains:
            count, domain = domain.split(' ')
            count = int(count)
            subdomains = domain.split('.')  
            for i in range(len(subdomains)):
                dic[".".join(subdomains[i:])] += count #cad ici le join au debut joins tout les subdomaines puis ensuite i avance de un donc join joins un sub en moins etc...
        return [" ".join([str(val), key]) for key,val in dic.items()]   # join recoit une list et la joins en une string 
            
