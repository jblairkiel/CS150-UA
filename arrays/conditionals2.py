def main():
    Brian = float(input("Enter a score for Brian "))
    John = float(input("Enter a score for John "))
    Mary = float(input("Enter a score for Mary "))

    ExamAvg = (Brian + John + Mary) / 3

    print("The raw score for the class is:", ExamAvg)

    Grade = getLetterGrade(ExamAvg)

    print("The class letter grade is:", Grade)

    if (Brian > John and Brian > Mary):
        print("Congratulations Brian for making a grade of:", getLetterGrade(Brian))
    elif(John > Mary):
        print("Congratulations John for making a grade of:", getLetterGrade(John))
    else:
        print("Congratulations Mary for making a grade of:", getLetterGrade(Mary))

def getLetterGrade(score):
    if (score>= 90):
        return 'A'
    elif (score>= 80):
        return 'B'
    elif (score>= 70):
        return 'C'
    elif (score>= 60):
        return 'D'
    else:
        return 'F'

main()
