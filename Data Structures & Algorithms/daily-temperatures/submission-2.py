class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps=temperatures
        n=len(temperatures)
        answer=[0]*n
        stk=[]

        for i,t in enumerate(temperatures):
            while stk and stk[-1][1] <t:
                stk_i,stk_t=stk.pop()
                answer[stk_i]=i-stk_i
            stk.append((i,t))
        return answer     