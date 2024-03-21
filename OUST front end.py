from datetime import datetime

# Function to validate date of birth
def isValidDOB(dob_str):
    try:
        # Convert dob str to datetime object
        dob = datetime.strptime(dob_str, '%d/%m/%Y')
        # Check if dob is after 1900
        if dob.year >= 1900:
            return True
        else:
            print("Birth year should begin after 1900, please try again.")
            return False
    except ValueError:
        print("Seems like your format might be invalid. Try again using DD/MM/YYYY")
        return False

# Function to validate email
def isValidEmail(email):
    # Basic email format validation
    if "@" in email and "." in email and len(email) <= 40:
        return True
    else:
        print("Error... That looks incorrect, please try again!")
        return False

# Function to validate first and last name
def isValidName(name):
    # Check if the name only contains alphabets and is within limits
    if name.isalpha() and len(name) <= 20:
        return True
    else:
        print("Looks like you've either exceeded your character limit or typed it incorrectly. Try again!")
        return False

# Function to validate unit code
def isValidUnitCode(unit_code):
    # Check if the unit code is 7 characters or less
    if len(unit_code) <= 7:
        return True
    else:
        print("Error... Unit code should be 7 characters or less. Please try again!.")
        return False

# Function to validate Mark
def isValidMark(mark):
    try:
        mark = float(mark)
        # Check if mark is between 0.0 and 100.0
        if 0.0 >= mark and mark <= 100.0:
            return True
        else:
            print("Error... Try inputting your marks between 0.00 and 100.00.")
            return False
    except ValueError:
        print("Slow down! Your answer seems incorrect. Try again!")
        return False

# Function to get input from user
def get_student_input():
    while True:
        try:
            student_id = int(input("Enter your student ID: "))
            # Check if student ID is 8 digits or less
            if len(str(student_id)) <= 8:
                break
            else:
                print("Looks like you've exceed the word count. Try again bud!")
        except ValueError:
            print("Oopsies! Wrong student ID number. Try again! ")

    while True:
        name = input("Enter your name: ")
        # Validate name
        if isValidName(name):
            break

    while True:
        last_name = input("Enter your last name ")
        # Validate last name
        if isValidName(last_name):
            break

    while True:
        email = input("Enter your personal email address  ")
        # Validate email
        if isValidEmail(email):
            break

    while True:
        dob = input("Enter your date of birth (DD/MM/YYYY): ")
        # Validate dob
        if isValidDOB(dob):
            break
    
    unit_scores = {}
    while True:
        try:
            num_units = int(input("Enter the number of units taken: "))
            break
        except ValueError:
            print("Looks like you put in the wrong number, try again!")

    for i in range(num_units):
        while True:
            unit_code = input(f"Enter unit code for unit {i + 1}: ")
            # Validate unit code
            if isValidUnitCode(unit_code):
                break

            mark = input(f"Enter marks for unit {unit_code}: ")
            # Validate mark
            if isValidMark(mark):
                mark = float(mark)
                unit_scores[unit_code] = mark
                break

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

if __name__ == "__main__":
    main()
