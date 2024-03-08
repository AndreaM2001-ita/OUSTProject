#-------------------------------------------------------------
#   Group Assignment for Distributed Systems
#   OUST eligibility to honours for student and outside individuals
#   - this code prints out the different scores reported by student
#   - calculates the average values of the scores stored in a dictionary
#   - calculates the avergae of the best 8 scores reported by the student
#   - determines eleigbility for honours
#
#   authors:
#   Andrea Marcosano 10541054
#   Maryam Saqib 10661276
#-------------------------------------------------------------
#function to print out the dictionary of the unitcode and correspective scores in order
def printUnitScores(unitScores):
    for unit_code, score in unitScores.items():
        print(unit_code , " : " , str(score))

#function to calculate the avergae of the scores in the dictionary 
def calculateAvg(unitScores):
    sum=0;
    count=0
    for unit_code, score in unitScores.items():
        sum=sum+score;
        count=count+1
    average=sum/count;  #average calculation
    return average


    
#function to sort by selection the list of scores
def selectionSort(scoresList):
 # Sort the list of scores in discending order
    for scoreIndex in range(len(scoresList)):
        largest = scoreIndex    #set first value to the largest
        for component in range(scoreIndex + 1, len(scoresList)): #check the rest of the List
            if scoresList[component] > scoresList[largest]:  # Compare for largest
                largest = component
        if largest != scoreIndex:
            # Swap the elements in the list in case a new larger was found
            scoresList[scoreIndex], scoresList[largest] = scoresList[largest], scoresList[scoreIndex]

#function to calulate the average of the first 8 grades
def averageEight(scoreList):
    sum=0
    count=0
    for score in scoreList[:8]:  #take first 8 values
        sum=sum+score;
        count=count+1
    avgEight=sum/count;  #average calculation
    return avgEight
            
#function to find the 8 best scores in the dictionary     
def selectEightScores(unitScores):
    #convert my scores into a list so that it can be sorted
    scoresList = list(unitScores.values())
    
    #sort the values in discending order
    selectionSort(scoresList)
    
    #average of the first 8 values
    avgEight=averageEight(scoresList)
    
    #print result
    print("The average of the best 8 scores is: ",avgEight);
    

if __name__ == '__main__':
   #dictionary of unit scores
    unitScores = {
        "unit000": 16.3,
        "unit001": 52.7,
        "unit002": 45.8,
        "unit003": 23.7,
        "unit004": 50.0,
        "unit005": 82.0,
        "unit006": 94.0,
        "unit007": 37.8,
        "unit008": 65.2,
        "unit009": 75.4,
        "unit010": 89.5,
        "unit011": 43.6,
        "unit012": 61.9,
        "unit013": 30.2,
        "unit014": 55.1,
        "unit015": 78.3,
        "unit016": 49.6,
        "unit017": 87.2,
        "unit018": 22.5,
        "unit019": 68.9,
        "unit020": 91.7,
        "unit021": 34.8,
        "unit022": 57.4,
        "unit023": 70.3,
        "unit024": 83.6,
        "unit025": 47.9,
        "unit026": 66.8,
        "unit027": 40.5,
        "unit028": 73.1,
        "unit029": 97.4
    }

    printUnitScores(unitScores); #print the cores in order
    average=calculateAvg(unitScores);#TODO--pass student id to show on screen
    print("the average of the student is: ", round(average, 2));

    selectEightScores(unitScores)
    #TODO-- implpement eligibility criteria
    
