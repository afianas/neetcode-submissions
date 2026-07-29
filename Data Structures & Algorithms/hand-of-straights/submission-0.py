from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False

        count=Counter(hand)
        hand=set(hand)
        
        for num in sorted(hand):
            freq=count[num]

            if freq==0:
                continue
            for numNext in range(num,num+groupSize):
                if count[numNext]<freq:
                    return False
                count[numNext]-=freq
        return True


        
                
            
                

