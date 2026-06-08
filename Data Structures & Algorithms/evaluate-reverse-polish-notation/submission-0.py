class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(0,len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                res1=stack.pop()
                res2=stack.pop()
                if tokens[i]=="+":
                    res=res2+res1
                if tokens[i]=="-":
                    res=res2-res1
                if tokens[i]=="*":
                    res=res2*res1
                if tokens[i]=="/":
                    res=int(res2/res1)
                stack.append(res)
        return int(stack[0])

        