class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        res=0
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                a=stack.pop()
                b=stack.pop()
                if tokens[i]=="+":
                    res=a+b
                elif tokens[i]=="-":
                    res=b-a
                elif tokens[i]=="*":
                    res=a*b
                else:
                    res=int(b/a)
                stack.append(res)
        return int(stack[0])