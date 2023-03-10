from datetime import datetime
from pprint import pprint

from src.models import Teacher, Student, Grade, Discipline, Group
from src.db import session


def create_student(fullname, group_id):
    student = Student(fullname=fullname, group_id=group_id)
    session.add(student)
    session.commit()
    session.close()


def create_teacher(fullname):
    teacher = Teacher(fullname=fullname)
    session.add(teacher)
    session.commit()


def create_group(name):
    group = Group(name=name)
    session.add(group)
    session.commit()


def create_discipline(name, teacher_id):
    discipline = Discipline(name=name, teacher_id=teacher_id)
    session.add(discipline)
    session.commit()


def create_grade(grade, date, student_id, discipline_id):
    grade = Grade(grade=grade, date_of=datetime.strptime(date, '%Y-%M-%d').date(), student_id=student_id, discipline_id=discipline_id)
    session.add(grade)
    session.commit()


def show_grades():
    grades = session.query(Grade.grade, Grade.date_of, Grade.student_id, Grade.discipline_id) \
        .select_from(Grade) \
        .all()
    pprint(grades)
    session.commit()


def show_students():
    students = session.query(Student.id, Student.fullname, Student.group_id) \
        .select_from(Student) \
        .all()
    pprint(students)
    session.commit()


def show_teachers():
    teachers = session.query(Teacher.id, Teacher.fullname) \
        .select_from(Teacher) \
        .all()
    pprint(teachers)
    session.commit()


def show_disciplines():
    disciplines = session.query(Discipline.id, Discipline.name) \
        .select_from(Discipline) \
        .all()
    pprint(disciplines)
    session.commit()


def show_groups():
    groups = session.query(Group.id, Group.name) \
        .select_from(Group) \
        .all()
    pprint(groups)
    session.commit()


def update_student(student_id, fullname, group_id):
    student = session.query(Student).filter(Student.id == student_id)
    if student:
        student.update({"fullname": fullname, "group_id": group_id})
        session.commit()


def update_teacher(fullname, teacher_id):
    teacher = session.query(Teacher).filter(Teacher.id == teacher_id)
    if teacher:
        teacher.update({"fullname": fullname})
        session.commit()


def update_group(group_id, name):
    group = session.query(Group).filter(Group.id == group_id)
    if group:
        group.update({"name": name})
        session.commit()


def update_discipline(discipline_id, name):
    discipline = session.query(Discipline).filter(Discipline.id == discipline_id)
    if discipline:
        discipline.update({"name": name})
        session.commit()


def update_grade(grade_id, grade, date_of, student_id, discipline_id):
    gr = session.query(Grade).filter(Grade.id == grade_id)
    if gr:
        gr.update({'grade': grade,
                   'date_of': datetime.strptime(date_of, '%Y-%M-%d').date(),
                   'student_id': student_id,
                   'discipline_id': discipline_id})
        session.commit()


def delete_student(student_id):
    session.query(Student).filter(Student.id == student_id).delete()
    session.commit()


def delete_discipline(discipline_id):
    session.query(Discipline).filter(Discipline.id == discipline_id).delete()
    session.commit()


def delete_teacher(teacher_id):
    session.query(Teacher).filter(Teacher.id == teacher_id).delete()
    session.commit()


def delete_group(group_id):
    session.query(Group).filter(Group.id == group_id).delete()
    session.commit()


def delete_grade(grade_id):
    session.query(Grade).filter(Grade.id == grade_id).delete()
    session.commit()

