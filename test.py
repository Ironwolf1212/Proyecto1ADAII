class Patch:
    def __init__(self,survTime,irriTime,priority):
        self.survTime = survTime
        self.irriTime = irriTime
        self.priority = priority

def calculateIrriStart(ranch, schedule):
    timings = [None,None,None,None,None]
    time = 0
    for patch in schedule:
        timings[patch] = time
        time += ranch[patch].irriTime
    return(timings)
def calculateCost(ranch, timings):
    cost = 0
    i = 0
    for patch in ranch:
        if (patch.survTime - patch.irriTime) > timings[i]:
            cost += patch.survTime - (patch.irriTime + timings[i])
        else:
            cost += patch.priority * ((timings[i] + patch.irriTime) - patch.survTime)
        #print(cost)
        i+=1
    return cost

with open ('Input.txt') as input:
    problems = input.readlines()
    print(problems)
    for line in problems:
        ranch = line[0]
        schedule = line[1]
        #print(ranch)
        #print (schedule)
        timings = calculateIrriStart(ranch,schedule)
        answers.append(calculateCost(ranch,timings))
        #print(calculateCost(ranch,timings))

with open ('Output.txt', 'w') as output:
    for answer in answers:
        output.write(answer+'\n')

#ranch = [Patch(10, 3, 4), Patch(5, 3, 3), Patch(2, 2, 1), Patch(8, 1, 1), Patch(6, 4, 2)]

#schedule = [0,1,4,2,3]
#schedule = [0,3,10,12,6]


#timings = calculateIrriStart(ranch,schedule)
#print(calculateCost(ranch,timings))