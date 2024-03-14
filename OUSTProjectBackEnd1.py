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

def get_student_input():
    student_id = int(input("Enter your student ID (8 digits): "))
    name = input("Enter your name (max 20 characters): ")
    last_name = input("Enter your last name (max 20 characters): ")
    email = input("Enter your email (max 40 characters): ")
    dob = input("Enter your date of birth (DD/MM/YYYY): ")
    
    unit_scores = {}
    num_units = int(input("Enter the number of units taken: "))
    for i in range(num_units):
        unit_code = input(f"Enter unit code for unit {i + 1}: ")
        mark = float(input(f"Enter mark for unit {unit_code}: "))
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

