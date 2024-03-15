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
def getInput(record):
    while True:
        try:
            Pick=int(input('Guess (enter 1-8): '))    
            if (Pick > 0 and Pick <9) and not record[Pick]:            #check if input is in range[1-8] and if it has already been picked
                return Pick
            elif record[Pick]:
                print('Word already picked, don\'t waste your guesses')
            else:
                print('Error...')
               
        except ValueError:
            print('Error... invalid input, enter a number')    #responce in case input is not a number
        except IndexError:                                      #solve problem of index not existent in list 
             print('Error... Enter a number within range')      #responce in case input is not within range
#DOB check

try:
    dob_str = input("Enter your date of birth (DD/MM/YYYY): ")  
    dob = datetime.strptime(dob_str, '%d/%m/%Y')
        # Assuming a reasonable range for DOB (e.g., between 1900 and current year)
        if 1900 <= dob.year <= datetime.now().year:
            return True
        else:
            return False
    except ValueError:
        print('Error...  Enter valid date of birth'); 
        return False

def get_student_input():
    student_id = int(input("Enter your student ID (8 digits): "))
    name = input("Enter your name (max 20 characters): ")  //check if it is a string + max 20 char
    last_name = input("Enter your last name (max 20 characters): ")//check if it is a string + max 20 char
    email = input("Enter your email (max 40 characters): ") //check if it is a string + max 40 char
    dob = input("Enter your date of birth (DD/MM/YYYY): ")  //dob check format
    
    unit_scores = {}
    num_units = int(input("Enter the number of units taken: "))
    for i in range(num_units):
        unit_code = input(f"Enter unit code for unit {i + 1}: ") //7 char
        mark = float(input(f"Enter mark for unit {unit_code}: ")) //check if it is not a string and uit is within range
        unit_scores[unit_code] = mark
        
    return student_id, name, last_name, email, dob, unit_scores

# Main function
def main():
    # Get input from the user
    student_id, name, last_name, email, dob, unit_scores = get_student_input()
    
    # Call server-side functions
    average = server.calculateAvg(unit_scores)
    avg_eight = server.selectEightScores(unit_scores)
    fails = server.countFails(unit_scores)
    
    # Verify eligibility
    server.verifyEligibility(student_id, name, last_name, email, dob, average, avg_eight, fails)


###^^^^^^^
#define server above by importing

