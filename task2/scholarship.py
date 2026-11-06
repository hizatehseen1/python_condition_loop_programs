print("========================================")
print("     STUDENT SCHOLARSHIP ELIGIBILITY SYSTEM")
print("========================================")

# Step 1: Collect student information
name = input("Enter Student Name: ")

# Validate name first
if name.strip() == "":
    print("\nError: Student name cannot be empty.")
else:
    # Step 2: Validate and collect numbers
    try:
        marks = float(input("Enter Academic Marks (%): "))
        attendance = float(input("Enter Attendance Percentage (%): "))
        income = float(input("Enter Monthly Family Income (Rs.): "))

        # Step 3: Validate ranges
        if marks < 0 or marks > 100:
            print("\nError: Marks must be between 0 and 100.")
        elif attendance < 0 or attendance > 100:
            print("\nError: Attendance must be between 0 and 100.")
        elif income < 0:
            print("\nError: Family income cannot be negative.")
        else:
            # Step 4: Check scholarship eligibility
            reasons = []

            if marks < 80:
                reasons.append("Academic marks are below 80%.")

            if attendance < 85:
                reasons.append("Attendance is below 85%.")

            if income > 50000:
                reasons.append("Monthly family income exceeds Rs. 50,000.")

            # Step 5: Display scholarship result
            print("\n========================================")
            print("       SCHOLARSHIP EVALUATION REPORT")
            print("========================================")

            print("Student Name:", name)
            print("Academic Marks:", marks, "%")
            print("Attendance:", attendance, "%")
            print("Monthly Family Income: Rs.", income)

            print("----------------------------------------")

            if len(reasons) == 0:
                if marks >= 90:
                    print("Scholarship Status: Eligible")
                    print("Scholarship Type: Full Scholarship")
                elif marks >= 80:
                    print("Scholarship Status: Eligible")
                    print("Scholarship Type: Partial Scholarship")
            else:
                print("Scholarship Status: Not Eligible")
                print("Reasons for Ineligibility:")

                for reason in reasons:
                    print("-", reason)

            print("========================================")
            print("          EVALUATION COMPLETED")
            print("========================================")

    except ValueError:
        print("\nError: Please enter valid numeric values for marks, attendance, and income.")
