class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xffffff
        while(b!=0):
            sumNoCarry=a^b
            carry=(a&b)<<1

            a=sumNoCarry&mask
            b=carry&mask

            
        if a>mask//2:
            return ~(a^mask)
        else:
            return a

        