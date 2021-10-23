import random

same_count = 0 
sample_size = 1000000 # Takes 10 seconds to run, set smaller if you wish 
for i in list(range(sample_size)): 
# Consider A,B,C as cars, and we take two random numbers between // 0-11 without replacement. We only care about you two, no one else 
# even matters so we don't bother. 
# 0-3 -> increment A, 4-7 increment B, 8-11 increment C A = 0 B = 0 C = 0
    randlist = random.sample(range(12), 2)
    A = 0
    B = 0
    C = 0
    for x in randlist:
        if x < 4:
            A = A+1
        elif x < 8:
            B = B+1
        else:
            C = C+1
    
        # check if any car has both you and your friend in it
    if A == 2 or B == 2 or C == 2: #since person a is 1, if you add one than you know its the same car
        same_count = same_count + 1
print("Same count: "+str(same_count)+"\nSample size: " + str(sample_size)+"\nProbability: "+str(same_count/sample_size))
