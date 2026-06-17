#Solved by ma

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        emp=[]
        
        
        l=s.split()
        n=len(l)
        for i in range(n):
            emp.append("".join(reversed(str(l[i]))))
            
            
        return " ".join(emp)

        
