if __name__ == '__main__':
    # Student marks dictionary
    student_marks = {
        "Anjali": 87,
        "Ravi": 92,
        "Neha": 95,
        "Amit": 78,
        "Sita": 90
    }


    # Sort by marks in descending order
    def get_marks(item):
        return item[1]


    top_three = sorted(student_marks.items(), key=get_marks, reverse=True)[:3]

    # Print top 3 scorers
    print("Top 3 Scorers:")
    for name, marks in top_three:
        print(f"{name} - {marks}")