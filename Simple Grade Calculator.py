def calculate_average(grades):
    total = sum(grades)
    count = len(grades)
    average = total / count
    return average

def main():
    while True:
        try:
            print("Based on 5-point grading scale.")
            grades_input = input("Enter the grades separated by spaces (or 'q' to quit): ")
            
            if grades_input.lower() == 'q':
                print("Exiting the program...")
                break
                
            grades = [float(grade) for grade in grades_input.split()]
            
            average = calculate_average(grades)
            print(f"The average of the grades is: {average}\n")
            
        except ValueError:
            print("Error: Please enter only numbers separated by spaces.\n")

if __name__ == "__main__":
    main()