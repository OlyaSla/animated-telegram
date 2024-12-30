class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def get_average_grade(self):
        total_grades = []
        for course, grades in self.grades.items():
            total_grades.extend(grades)
        return sum(total_grades) / len(total_grades) if total_grades else 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else 'Нет'
        courses_in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else 'Нет'
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        total_grades = []
        for course, grades in self.grades.items():
            total_grades.extend(grades)
        return sum(total_grades) / len(total_grades) if total_grades else 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        courses = ', '.join(self.courses_attached) if self.courses_attached else 'Нет'
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Курсы, которые он проверяет: {courses}")


def get_average_grade_for_course(students, course):
    total_grades = []
    for student in students:
        if course in student.courses_in_progress:
            if course in student.grades:
                total_grades.extend(student.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0


def get_average_grade_for_lecturers(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            if course in lecturer.grades:
                total_grades.extend(lecturer.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0


student1 = Student('Ruoy', 'Eman', 'male')
student1.grades = {'Python': [10, 9, 8]}
student1.courses_in_progress = ['Python']
student1.finished_courses = ['Введение в программирование']

student2 = Student('Anna', 'Smith', 'female')
student2.grades = {'Python': [8, 7, 9]}
student2.courses_in_progress = ['Python']

students = [student1, student2]

lecturer1 = Lecturer('John', 'Doe')
lecturer1.grades = {'Python': [9, 10, 8]}
lecturer1.courses_attached = ['Python']

lecturer2 = Lecturer('Jane', 'Doe')
lecturer2.grades = {'Python': [7, 8, 9]}
lecturer2.courses_attached = ['Python']

lecturers = [lecturer1, lecturer2]

reviewer1 = Reviewer('Alice', 'Johnson')
reviewer1.courses_attached = ['Python']

reviewer2 = Reviewer('Bob', 'White')
reviewer2.courses_attached = ['Python']

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

average_grade_students = get_average_grade_for_course(students, 'Python')
print(f"Средняя оценка за курс 'Python' у студентов: {average_grade_students:.1f}")

average_grade_lecturers = get_average_grade_for_lecturers(lecturers, 'Python')
print(f"Средняя оценка за курс 'Python' у лекторов: {average_grade_lecturers:.1f}")
