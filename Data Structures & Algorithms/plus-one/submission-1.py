class Solution: 
    def plusOne(self, digits: List[int]) -> List[int]: 
        temp="" 
        out=[]
        temp = "".join(map(str, digits))
        num=int(temp)
        num1=str(num+1)
        for i in range(0,len(num1)): 
            out.append(int(num1[i])) 
        return out