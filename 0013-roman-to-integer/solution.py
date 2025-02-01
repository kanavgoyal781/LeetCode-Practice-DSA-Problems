class Solution:
    def romanToInt(self, s: str) -> int:
        m=0

        for k in s:
            if k=='I':
                m=m+ 1
            if k=='V':
                m=m+ 5
            if k=='X':
                m=m+ 10
            if k=='L':
                m=m+ 50
            if k=='C':
                m=m+ 100
            if k=='D':
                m=m+ 500
            if k=='M':
                m=m+ 1000
        
        if s.count('IV') >0:
            m=m-1*s.count('IV')-1
        if s.count('IX') >0:
            m=m-1*s.count('IX')-1
        if s.count('XL') >0:
            m=m-10*s.count('XL')-10
        if s.count('XC') >0:
            m=m-10*s.count('XC')-10
        if s.count('CD') >0:
            m=m-100*s.count('CD')-100
        if s.count('CM') >0:
            m=m-100*s.count('CM')-100






        return m

