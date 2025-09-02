def student_report(students):
    """Generate a report from student names and scores."""
    if not students:
        return {"average": None, "highest": [], "lowest": []}
    
    scores = list(students.values())
    average_score = sum(scores) / len(scores)

    max_score = max(scores)
    min_score = min(scores)

    highest = [name for name, score in students.items() if score == max_score]
    lowest = [name for name, score in students.items() if score == min_score]

    return {
        "average": average_score,
        "highest": highest,
        "lowest": lowest
    }


# Example usage:
students_data = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 92,
    "Eve": 65
}

print(student_report(students_data))

