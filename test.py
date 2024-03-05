class Patch:
    def __init__(self,survTime,irriTime,priority):
        self.survTime = survTime
        self.irriTime = irriTime
        self.priority = priority

#schedule = [0,1,4,2,3]
#schedule = [2,1,4,3,0]
def calculateIrriStart(ranch, schedule):
    timings = [0] * len(ranch)
    time = 0
    for patch in schedule:
        timings[patch] = time
        time += int(ranch[patch].irriTime)
    return(timings)
def calculateCost(ranch, timings):
    cost = 0
    i = 0
    for patch in ranch:
        if (int(patch.survTime) - int(patch.irriTime)) > timings[i]:
            cost += int(patch.survTime) - (int(patch.irriTime) + timings[i])
        else:
            cost += int(patch.priority) * ((timings[i] + int(patch.irriTime)) - int(patch.survTime))
        #print(cost)
        i+=1
    return cost

#Calcular el promedio de irriTime  de ranch
def calculateAvg(ranch):
    avg = 0
    for patch in ranch:
        avg += int(patch.irriTime)
    return avg/len(ranch)

def calc_Schedule(ranch, average_it):
    schedule = []
    for patch in ranch:
        if int(patch.survTime) > average_it:
            schedule.append(ranch.index(patch))
    for patch in ranch:
        if int(patch.survTime) <= average_it:
            schedule.append(ranch.index(patch))
    return schedule



with open ('Input.txt') as input:
    ranch = []
    input = input.readlines()[1:]
    for line in input:
        data = line.split(",")
        ranch.append(Patch(data[0],data[1],data[2]))

average_it = calculateAvg(ranch)
schedule = calc_Schedule(ranch, average_it)
print(schedule)
    
#with open ('Output.txt', 'w') as output:
#    for answer in answers:
#        output.write(answer+'\n')

#ranch = [Patch(10, 3, 4), Patch(5, 3, 3), Patch(2, 2, 1), Patch(8, 1, 1), Patch(6, 4, 2)]


#schedule = [0,3,10,12,6]


timings = calculateIrriStart(ranch,schedule)
print(calculateCost(ranch,timings))