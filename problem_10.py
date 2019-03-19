class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #import pdb;pdb.set_trace()
        #s = list(s)
        #p = list(p)
        #print('s: '+str(s)+ '   p:' +str(p)+'\n' )

        if 0 == len(p):
            return len(s) == 0
        if 1 == len(p):
            return len(s) == 1 and (s[0] == p[0] or p[0] == '.')

        if p[1] != '*':
            if 0 == len(s):
                return False
            else:
                return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:],  p[1:])

        while(0 != len(s) and (s[0] == p[0] or p[0] == '.')):
            if self.isMatch(s, p[2:]):
                return True
            s = s[1:]

        return self.isMatch(s, p[2:])



######################
def REM():
    #s = "ppi"
    #p = "p*."
    s = 'ab'
    p = '.*c'
    solution = Solution()
    aa = solution.isMatch(s,p)
    #import pdb;pdb.set_trace()
    print(aa)


#############################################
if (__name__ == "__main__"):
    REM()