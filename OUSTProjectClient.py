#-------------------------------------------------------------
#   Group Assignment for Distributed Systems
#   OUST eligibility to honours for student and outside individuals
#   - this code takes and verify all inputs asked to user  
#   - studentID name lastname 
#  -makes requests to serverfor students
#
#   authors:
#   Andrea Marcosano 10541054
#-------------------------------------------------------------
import ClientSocket

#function to welcome user
def welcome():
    print("Welcome to the OUST Honours Enrolling systems!")
    print("before proceeding with your enrollement we would like to verify your eligibility")
    print("----------------------------------------------------------------")
#multiuse function to ask user for any request with an answer that requires to be y or n
def yesOrNo(question):
    while True:
        try:
            print(question)
            answer = input("Enter Y/N for Yes/No: ")
            answer=answer.lower()#make it lower case to avoid issues with upper case
            if answer=='y' or answer=='n':
                break
            else:
                print("Looks like you've entered an unrecognised character, try again")
        except ValueError:
            print("Error... wrong input, try again... ")
    return answer

# Function to verify correct input of name and last name
def verifyString(name):
    # Check if the name only contains letters and it is within boundaries of length
    if name.isalpha() and len(name) <= 20:
        return True
    else:
        print("Looks like you've either exceeded your character limit (20) or typed it incorrectly. Try again!")
        return False
    
# Function to verifty the correctness of email entered
def isValidEmail(email):
    # Basic email format validation
    if "@" in email and "." in email and len(email) <= 40:
        return True
    else:
        print("ERROR... email format is incorrect, try again...")
        return False
    
def getId(identity):
    while True:
        try: #student or person ID
            studentId = input(f"Enter your {identity} ID: ") #use identity variable to make fucnction reusable in both settings 
            # Check if student ID is 8 digits 
            if len(str(studentId)) == 8:
                break
            else:
                print("The user ID has to be 8 numbers long, try again...")
        except ValueError:
            print("ERROR... wrong user ID ")
    return studentId

#fucntion to get user details as input
def getStudentDetails():
    
    student_id=getId("Student")
    while True:
        name = input("Enter your name: ")
        # Validate name
        if verifyString(name):
            break

    while True:
        last_name = input("Enter your last name: ")
        # Validate last name
        if verifyString(last_name):
            break
    
    while True:
        email = input("Enter your personal email address:  ")
        # Validate email
        if isValidEmail(email):
            break
    return student_id, name,last_name,email
# Function to validate unit code
def isValidUnitCode(unit):
    while True:
        unit_code=input(f"Enter unit code for unit {unit + 1}: " )
        # Check if the unit code is 7 characters or less
        if len(unit_code) <= 7:  #length on assignment script
            return unit_code
        else:
            print("Error... Unit code should be 7 characters or less. Please try again!.")

# Function to validate Mark
def isValidMark(unit_code,addition):
    while True:
        try:
             #adding addition string to reuse function for all cases of input
            mark = input(f"Enter your {addition} mark for unit {unit_code}: ") 
            mark = float(mark)
            # Check if mark is between 0.0 and 100.0
            if 0.0 <= mark <= 100.0:
                return mark
            else:
                print("Error... mark has to be between 0.0 and 100.0")
        except ValueError:
            print("ERROR...Your answer seems incorrect. Try again!")
#output in case of missed eligibitlity check
def missedEligibility():
    print("!!!-----------------------------------------------------------------------")
    print("Unfortuantely you will not be eligible for Honours, as you presented wrongful information")
    print("!!!-----------------------------------------------------------------------")
#handling of fails in grades
def handleFailures(mark, unit_code, unit_scores, fails):
    iterations=0
    new_unit_code = f"{unit_code}_{iterations + 1}"  # Append iteration number to unit code
    unit_scores[new_unit_code] = mark
    while iterations<fails:
        iterations+=1
        #if it the last unit the program should ask for a passing score 
        #otherwise th eonly other case is interting a second fail score
        mark = isValidMark(unit_code, "passing" if iterations==(fails) else "second")
        if mark<50.0 and iterations==fails: #case in which user is trying to enter 3 fails, whilst only admitting 2
            missedEligibility()
            return -1
        new_unit_code = f"{unit_code}_{iterations + 1}"  # Append iteration number to unit code
        unit_scores[new_unit_code] = mark
#function to ask user how many times they have failed unit if score is less than 50
def askFailedTimes(unit_code):
    fails=1
    while True: #to avoid that user syas that they did not fail
        try:
            fails=int(input(f"How many times have you failed unit {unit_code}?: "))  #report failures
            if fails!=0: 
                break
        except ValueError:
            print("ERROR...Your answer seems incorrect. Try again!")
    return fails

#function to check if the grade was a fail and if it was how many times it was repeated    
def checkFail(mark, unit_code,unit_scores):
    while True:
        try:
            if mark<50.0: #grade is a fail
                fails=askFailedTimes(unit_code)#ask how many times has class been failed
                if fails >2 or fails < 0: 
                    missedEligibility()
                    return -1
                elif fails>0 and fails<=2:
                    if handleFailures(mark, unit_code, unit_scores, fails)==-1:
                        return -1
                    break
            else:
                unit_scores[unit_code] = mark
        except ValueError:
            print("ERROR...Your answer seems incorrect. Try again!")

#get details on person(if not student)
#For example, OUST doesn’t allow the students do any unit more than three times. 
def getPersonDetails(student):
    person_id = getId("Person" if student == 'n' else "Student")
    print("Please enter your unit codes and marks...")
    print("--------------------------------------------------------------------------")
    unit_scores = {}
    while True:
        try:
            num_units = int(input("Enter the number of units taken: "))
            #checking that number of units is apporpriate
            if num_units <16 or num_units >30:
                print("ERROR... number of units has to be within 16 and 30")
            else:
                break
        except ValueError:
            print("Error... wrong value")
    #insert unit scores 
    for unit in range(num_units):
        unit_code = isValidUnitCode(unit)
        mark=isValidMark(unit_code,"")
        if checkFail(mark, unit_code,unit_scores)==-1:
            return person_id,None  #if theere is a class that user failed more than 3 times program will return non eligibile
    return person_id, unit_scores
#main
if __name__ == "__main__":
    while True:
        welcome()
        
        # Get input from the user
        student=yesOrNo("Are you a current student of OUST?")  #ask if it is a student
        #if user is student ask if they want to insert their own scores or they want ot make a request to database
        if student=='y': request=yesOrNo("Would you like to insert your own unit scores?")
        if student=='y' and request=='n':
            userId, name, last_name, email= getStudentDetails()
            unit_scores={}  #no need to ask for scores, ask database
        else:
            name=""  #initialising empty variables
            last_name=""
            email=""
            while True:
                userId, unit_scores=getPersonDetails(student)
                try:
                    if unit_scores is None:
                        raise ValueError("your scores are not eligible. Enter your details again...")
                    else:
                        break
                except ValueError as e:
                    print("Error: ", e)

        print(userId)
        print()
        print("--------------------------------------------------------------------------")
        print("Thank you for providing your correct details...")
        """
        userId=12345678
        name=""
        last_name=""
        email=""
        unit_scores={}
        unit_scores["abc"]=23.0
        unit_scores["def"]=25.3
        """
        try:
            socket=ClientSocket.connectSocket()

            while True:
                message=ClientSocket.messageHandler(userId,unit_scores, name, last_name,email)


                ClientSocket.sendMessage(message,socket)

                responce=ClientSocket.decodeData(socket)
                print("--------------------------------")
                print(responce)
                print("--------------------------------")
                break
        finally:
            ClientSocket.closeSocket(socket)
        
        if yesOrNo("Would you like to verify the eligibility of another user?")=='n':
            print("Program is closing")
            break
    
    
