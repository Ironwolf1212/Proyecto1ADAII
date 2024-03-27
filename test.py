import copy

class Patch:
    def __init__(self,survTime,irriTime,priority):
        self.survTime = survTime
        self.irriTime = irriTime
        self.priority = priority
    def __repr__(self):
        return f'Patch({self.survTime}, {self.irriTime}, {self.priority})'

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
#print(schedule)
    
#with open ('Output.txt', 'w') as output:
#    for answer in answers:
#        output.write(answer+'\n')

#ranch = [Patch(10, 3, 4), Patch(5, 3, 3), Patch(2, 2, 1), Patch(8, 1, 1), Patch(6, 4, 2)]


schedule = [4,1,0,2,3]
print(schedule)

timings = calculateIrriStart(ranch,schedule)
print(calculateCost(ranch,timings))



def calculateOrder(ranch):
    calculatedPatches = 0
    patchChosen = [None, -100]
    foundSolution = False
    for patch in ranch:
        if patch == None:
            calculatedPatches += 1
            print("nah")
        else:
            foundSolution = True
            time = 0
            toBeCalculated = []
            possiblePenalty = int(patch.priority) * ((1 + int(patch.irriTime))-int(patch.survTime))
            tempRanch = copy.deepcopy(ranch)
            tempRanch.pop(ranch.index(patch))
            for otherPatch in tempRanch:
                if otherPatch == None:
                    #Donothing
                    print("yas")
                else:
                    if (int(patch.irriTime) + time) > int(otherPatch.survTime):
                        toBeCalculated.append(patch)
                skippedPenalty = 0
                for skippedPatch in toBeCalculated:
                    skippedPenalty += int(skippedPatch.priority) * ((1 + int(skippedPatch.irriTime))- int(skippedPatch.survTime))
                penaltyQuotient = possiblePenalty - skippedPenalty
                if (penaltyQuotient > patchChosen[1]):
                    patchChosen = [patch, penaltyQuotient]
        if calculatedPatches >= 5:
            print(calculatedPatches)
            return schedule
    ranch[ranch.index(patch)] = None
    if foundSolution == False:
        return schedule
    else:
        foundSolution = False
        schedule = [ranch.index(patchChosen[0])].append(calculateOrder(ranch))
    
def calculateOrderNonRec(ranch):
    schedule = [None,None,None,None,None]
    patchChosen = [None, -100]
    counter = 0
    time = 0
    for i in range(len(schedule)):
        for patch in ranch:
            
            #print(ranch)
            if patch == None:
                #print("ranch: ",ranch)
                continue
            else:
                
                toBeCalculated = []
                possiblePenalty = int(patch.priority) * ((1 + int(patch.irriTime))-int(patch.survTime))
                tempRanch = copy.deepcopy(ranch)
                tempRanch.pop(ranch.index(patch))
                for otherPatch in tempRanch:
                    if otherPatch == None:
                        #Donothing
                        #print("tempranch: ",tempRanch)
                        continue
                    else:
                        if (int(patch.irriTime) + time) > int(otherPatch.survTime):
                            toBeCalculated.append(patch)
                skippedPenalty = 0
                for skippedPatch in toBeCalculated:
                    skippedPenalty += int(skippedPatch.priority) * ((time+1 + int(skippedPatch.irriTime))- int(skippedPatch.survTime))
                penaltyQuotient = 0 - skippedPenalty
                print(skippedPenalty)
                print(penaltyQuotient)
                print(patchChosen[1])
                if (penaltyQuotient > patchChosen[1]):
                    patchChosen = [patch, penaltyQuotient]
        for patch in ranch:
            if patchChosen[0]==patch:
                time += int(patch.irriTime)
                schedule[ranch.index(patch)] = counter
                ranch[ranch.index(patch)] = None
        #ranch[ranch.index(patchChosen[0])] = None
        print(schedule)
        patchChosen = [None, -100]
        counter +=1
    print(schedule)
    return repr(patchChosen)
        
#print(calculateOrderNonRec(ranch))
ranch = [Patch(10, 3, 4), Patch(5, 3, 3), Patch(2, 2, 1), Patch(8, 1, 1), Patch(6, 4, 2)]
timings = [2,1,0,3,4]
print("El costo es: ",calculateCost(ranch,timings))