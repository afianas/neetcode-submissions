class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        store=[]
        time=[]
        for i in range(0,len(speed)):
            store.append((position[i],speed[i]))
        store.sort(reverse=True)
        for pos,sp in store:
            t=((target-pos)/sp)    
            time.append(t)
        maxtime=0
        fleet=0
        for i in range(len(speed)):
            if time[i]>maxtime:
                fleet+=1
                maxtime=time[i]
            else:
                continue
        return fleet