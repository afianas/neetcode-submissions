class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps=temperatures
        n=len(temperatures)
        answer=[0]*n
        stack=[]

        for i,t in enumerate(temperatures):
            while stack and stack[-1][1]<t:
                stack_index,stack_temperature=stack.pop()
                answer[stack_index]=i-stack_index
            stack.append((i,t))
        
        return answer     