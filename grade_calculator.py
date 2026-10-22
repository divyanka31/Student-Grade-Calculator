
def calculate_grade():
    try:
        subjects = int(input("Enter number of subjects: "))

        if subjects <= 0:
            print("Enter at least one subject.")
            return

        marks = []

        for i in range(subjects):
            score = float(input(f"Enter marks for subject {i + 1}: "))

            if score < 0 or score > 100:
                print("Marks must be between 0 and 100.")
                return

            marks.append(score)

        total = sum(marks)
        percentage = total / subjects

        if any(score < 33 for score in marks):
            grade = "F"
            result = "Fail"
        elif percentage >= 90:
            grade = "A+"
            result = "Pass"
        elif percentage >= 75:
            grade = "A"
            result = "Pass"
        elif percentage >= 60:
            grade = "B"
            result = "Pass"
        elif percentage >= 45:
            grade = "C"
            result = "Pass"
        else:
            grade = "D"
            result = "Pass"

        print("\n--- Student Result ---")
        print(f"Total Marks: {total:.2f}/{subjects * 100}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")
        print(f"Result: {result}")

    except ValueError:
        print("Please enter valid numbers.")


calculate_grade()
