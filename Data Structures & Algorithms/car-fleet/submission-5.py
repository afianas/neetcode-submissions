class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=[]
        store=[]
        for i in range(len(position)):
            store.append((position[i],speed[i]))
        store.sort(reverse=True)
        print(position)
        count=0
        for i,t in store:
            time.append((target-i)/t)
        maxtime=0
        fleet=0
        for t in time:
            if t>maxtime:
                fleet+=1
                maxtime=t
        return fleet

