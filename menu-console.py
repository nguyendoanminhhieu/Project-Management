class Course:
    def __init__(self, name, duration, topics):
        self.name = name
        self.duration = duration
        self.topics = topics

    def get_info(self):
        return f"Course: {self.name}\nDuration: {self.duration} weeks\nTopics: {', '.join(self.topics)}"


class Student:
    def __init__(self, name):
        self.name = name
        self.enrolled_courses = []

    def enroll(self, course):
        self.enrolled_courses.append(course)

    def unenroll(self, course_name):
        for course in self.enrolled_courses:
            if course.name == course_name:
                self.enrolled_courses.remove(course)

    def list_enrolled_courses(self):
        return [course.name for course in self.enrolled_courses]


class CourseManager:
    def __init__(self):
        self.courses = []

    def create_course(self, name, duration, topics):
        course = Course(name, duration, topics)
        self.courses.append(course)
        return course

    def list_courses(self):
        return [course.name for course in self.courses]


students = []
course_manager = CourseManager()

while True:
    print("\nMenu:")
    print("1. Create a new student")
    print("2. Create a new course")
    print("3. Enroll a student in a course")
    print("4. Unenroll a student from a course")
    print("5. List enrolled courses for a student")
    print("6. List all courses")
    print("7. List all students")
    print("8. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_name = input("Enter student's name: ")
        student = Student(student_name)
        students.append(student)
        print(f"Student {student_name} created.")

    elif choice == "2":
        course_name = input("Enter course name: ")
        course_duration = int(input("Enter course duration (in weeks): "))
        course_topics = input("Enter course topics (comma-separated): ").split(',')
        course = course_manager.create_course(course_name, course_duration, course_topics)
        print(f"Course {course_name} created.")

    elif choice == "3":
        student_name = input("Enter student's name: ")
        course_name = input("Enter course name: ")
        for student in students:
            if student.name == student_name:
                for course in course_manager.courses:
                    if course.name == course_name:
                        student.enroll(course)
                        print(f"{student_name} enrolled in {course_name}.")
                        break
                else:
                    print(f"Course {course_name} not found.")
                break
        else:
            print(f"Student {student_name} not found.")

    elif choice == "4":
        student_name = input("Enter student's name: ")
        course_name = input("Enter course name: ")
        for student in students:
            if student.name == student_name:
                student.unenroll(course_name)
                print(f"{student_name} unenrolled from {course_name}.")
                break
        else:
            print(f"Student {student_name} not found.")

    elif choice == "5":
        student_name = input("Enter student's name: ")
        for student in students:
            if student.name == student_name:
                enrolled_courses = student.list_enrolled_courses()
                if enrolled_courses:
                    print(f"{student_name} is enrolled in the following courses: {', '.join(enrolled_courses)}")
                else:
                    print(f"{student_name} is not enrolled in any courses.")
                break
        else:
            print(f"Student {student_name} not found.")

    elif choice == "6":
        courses = course_manager.list_courses()
        if courses:
            print("List of available courses:")
            for course_name in courses:
                print(course_name)
        else:
            print("No courses available.")

    elif choice == "7":
        if students:
            print("List of students:")
            for student in students:
                print(student.name)
        else:
            print("No students available.")

    elif choice == "8":
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")