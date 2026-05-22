def solve_marks():
 
    try:
        num_semesters = int(input("Enter no of semester:\n"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    subjects_per_semester = []
    for i in range(num_semesters):
        sub_count = int(input(f"Enter no of subjects in {i+1} semester:\n"))
        subjects_per_semester.append(sub_count)

    max_marks_list = []

    for i in range(num_semesters):
        print(f"Marks obtained in semester {i+1}:")
        current_max = -1
        
        for j in range(subjects_per_semester[i]):
            mark = int(input())
            
            if mark < 0 or mark > 100:
                print("You have entered invalid mark.")
                return 
            
            if mark > current_max:
                current_max = mark
        
        max_marks_list.append(current_max)

    for i in range(num_semesters):
        print(f"Maximum mark in {i+1} semester:{max_marks_list[i]}")

if __name__ == "__main__":
    solve_marks()