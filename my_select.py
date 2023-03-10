from sqlalchemy import func, desc, select, and_
from pprint import pprint

from src.models import Student, Teacher, Discipline, Grade, Group
from src.db import session


def select_1():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів
    :return: list[dict]
    """
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result


def select_2(discipline_id: int):
    """
    Знайти студента із найвищим середнім балом з певного предмета
    :return: list[dict]
    """
    result = session.query(Discipline.name, Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .filter(Discipline.id == discipline_id) \
        .group_by(Student.id, Discipline.name) \
        .order_by(desc('avg_grade')) \
        .limit(1).all()
    return result


def select_3(discipline_id: int):
    """
    Знайти середній бал у групах з певного предмета
    :return: list[dict]
    """
    result = session.query(Discipline.name, Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(Discipline.id == discipline_id) \
        .group_by(Group.name, Discipline.name) \
        .order_by(desc('avg_grade')) \
        .all()
    return result


def select_4():
    """
    Знайти середній бал на потоці (по всій таблиці оцінок)
    :return: list[dict]
    """
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .all()
    return result


def select_5(teacher_id):
    """
    Знайти які курси читає певний викладач
    :return: list[dict]
    """
    result = session.query(Teacher.fullname, Discipline.name) \
        .select_from(Discipline) \
        .join(Teacher) \
        .filter(Teacher.id == teacher_id) \
        .group_by(Teacher.fullname, Discipline.name) \
        .all()
    return result


def select_6(group_id):
    """
    Знайти список студентів у певній групі
    :return: list[dict]
    """
    result = session.query(Student.fullname, Group.name) \
        .select_from(Student) \
        .join(Group) \
        .filter(Group.id == group_id) \
        .group_by(Group.id, Student.fullname) \
        .all()
    return result


def select_7(group_id, discipline_id):
    """
    Знайти оцінки студентів у окремій групі з певного предмета
    :return: list[dict]
    """
    result = session.query(Student.fullname, Discipline.name, Grade.grade) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .filter(and_(Student.group_id == group_id, Discipline.id == discipline_id)) \
        .order_by(Discipline.name) \
        .all()
    return result


def select_8(teacher_id):
    """
    Знайти середній бал, який ставить певний викладач зі своїх предметів
    :return: list[dict]
    """
    result = session.query(Discipline.name, Teacher.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Teacher) \
        .filter(Teacher.id == teacher_id) \
        .group_by(Teacher.fullname, Discipline.name) \
        .all()
    return result


def select_9(student_id):
    """
    Знайти список курсів, які відвідує студент
    :return: list[dict]
    """
    result = session.query(Student.fullname, Discipline.name) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Student) \
        .filter(Student.id == student_id) \
        .group_by(Student.fullname, Discipline.name) \
        .all()
    return result


def select_10(student_id, teacher_id):
    """
    Список курсів, які певному студенту читає певний викладач
    :return: list[dict]
    """
    subquery = (select(Discipline.id).where(Discipline.teacher_id == teacher_id).scalar_subquery())
    result = session.query(Discipline.name) \
        .select_from(Grade) \
        .join(Discipline) \
        .filter(and_(Grade.discipline_id.in_(subquery), Grade.student_id == student_id)) \
        .group_by(Discipline.name) \
        .all()
    return result


def select_11(student_id, teacher_id):
    """
    Середній бал, який певний викладач ставить певному студентові
    :return: list[dict]
    """
    subquery = (select(Discipline.id).where(Discipline.teacher_id == teacher_id).scalar_subquery())
    result = session.query(Discipline.name, func.round(func.avg(Grade.grade), 2) \
                           .label('avg_grade')) \
        .select_from(Grade) \
        .join(Discipline) \
        .filter(and_(Grade.discipline_id.in_(subquery), Grade.student_id == student_id)) \
        .group_by(Discipline.name) \
        .all()
    return result


def select_12(discipline_id, group_id):
    """
    Оцінки студентів у певній групі з певного предмета на останньому занятті
    :return: list[dict]
    """
    subquery = (select(Grade.date_of).join(Student).join(Group).where(
        and_(Grade.discipline_id == discipline_id, Group.id == group_id)
    ).order_by(desc(Grade.date_of)).limit(1).scalar_subquery())

    r = session.query(Discipline.name,
                      Student.fullname,
                      Group.name,
                      Grade.date_of,
                      Grade.grade
                      ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(and_(Discipline.id == discipline_id, Group.id == group_id, Grade.date_of == subquery)) \
        .order_by(desc(Grade.date_of)) \
        .all()
    return r


if __name__ == '__main__':
    pprint(select_1())
    pprint(select_2(2))
    pprint(select_3(1))
    pprint(select_4())
    pprint(select_5(1))
    pprint(select_6(1))
    pprint(select_7(1,1))
    pprint(select_8(1))
    pprint(select_9(1))
    pprint(select_10(1, 1))
    pprint(select_11(1, 1))
    pprint(select_12(7, 3))
