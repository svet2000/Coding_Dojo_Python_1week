#tail=0, head=1

import random
def coinTossFunc(times):
    sum_heads=0
    sum_tails=0
    for toss in range(0,times):
        cointoss=random.randint(0,1)
        # print cointoss
        if cointoss==0:
            sum_tails+=1
            print "It's a tail! ... Got", sum_heads," head(s) so far and ", sum_tails, "tail(s) so far"
        else:
            sum_heads+=1
            print "It's a head! ... Got", sum_heads," head(s) so far and ", sum_tails, "tail(s) so far"
coinTossFunc(20)
