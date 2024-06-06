class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        for i in range(int(len(hand)/groupSize)):
            hand.sort()
            for j in range(1,groupSize):
                if hand[0]+j in hand:
                    hand.remove(hand[0]+j)
            hand.remove(hand[0])
        return True if hand == [] else False
