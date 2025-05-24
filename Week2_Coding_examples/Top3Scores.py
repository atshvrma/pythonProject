if __name__ == '__main__':
    # Sample student marks dictionary
    student_scores = {
        "Amit": 88,
        "Neha": 95,
        "Ravi": 76,
        "Sita": 89,
        "Anil": 92
    }


    # Define a function to return the score (used instead of lambda)
    def get_score(item):
        return item[1]


    # Sort by scores in descending order
    top_students = sorted(student_scores.items(), key=get_score, reverse=True )

    # Print top 3
    print("Top 3 scorers:")
    for name, score in top_students[:3]:
        print(f"{name} - {score}")