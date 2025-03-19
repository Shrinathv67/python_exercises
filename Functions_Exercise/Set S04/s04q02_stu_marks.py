""" What does this program do ?
This program is for calculating the total percentage marks and ranks the student as per the given conditionss:
First Class if score is more than or equal to 90%
Second Class if score is more than or equal to 75%
Average if student has not failed
Failed if score is less than or equal to 35 %
"""

def student_rank(average):
    if average >= 90:
        print("First Class")
    elif average >= 75 and average < 90:
        print("Second Class")
    elif average > 35 and average < 75:
        print('Average. Student has not failed.')
    else:
        print('Student has failed.')

   
def get_student_marks():
    eng_marks = int(input("Please enter the english marks: "))
    math_marks = int(input("Please enter mathematics marks: "))
    science_marks = int(input("Please enter the science marks: "))
    return eng_marks,math_marks,science_marks

def perc_calculation(english_marks,maths_marks,science_marks):
    perc_english = (english_marks/80)*100
    perc_maths = (maths_marks/80)*100
    perc_science = (science_marks/80)*100
    total_perc = (perc_maths + perc_maths + perc_science)/3
    return total_perc

# Main starts from here
def main():
    eng_mks,math_mks,science_mks = get_student_marks() 
    total_perc = perc_calculation(eng_mks,math_mks,science_mks)
    student_rank(total_perc)

if __name__ == "__main__":
    main()