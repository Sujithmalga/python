from main.account import percentage, college

def test_percentage_class():
    # Test cases for percentage class
    # Case 1: Valid marks and grade
    percentage_1 = percentage("85", "A")
    assert percentage_1.marks() == 85
    assert percentage_1.grade() == "A"

    # Case 2: Valid marks and grade
    percentage_2 = percentage("60", "B+")
    assert percentage_2.marks() == 60
    assert percentage_2.grade() == "B+"

    # Case 3: Invalid marks (not numeric)
    try:
        percentage_3 = percentage("35", "C")
    except ValueError as e:
        assert str(e) == "Marks must be numeric."

    # Case 4: Invalid grade (empty string)
    try:
        percentage_4 = percentage("75", "A")
    except ValueError as e:
        assert str(e) == "Grade cannot be empty."

def test_college_class():
    # Test cases for college class
    # Case 1: Valid student ID, course, and extra_cultural
    college_1 = college("2023001", "Engineering", "Drama Club")
    assert college_1._student_id == "2023001"
    assert college_1._course == "Engineering"
    assert college_1._extra_cultural == "Drama Club"

    # Case 2: Valid student ID, course, and empty extra_cultural
    college_2 = college("2023002", "Medicine", "")
    assert college_2._student_id == "2023002"
    assert college_2._course == "Medicine"
    assert college_2._extra_cultural == ""

    # Case 3: Invalid student ID (empty string)
    try:
        college_3 = college("", "Physics", "Chess Club")
    except ValueError as e:
        assert str(e) == "Student ID cannot be empty."

    # Case 4: Invalid course (None)
    try:
        college_4 = college("2023004", None, "Art Club")
    except ValueError as e:
        assert str(e) == "Course cannot be None."
