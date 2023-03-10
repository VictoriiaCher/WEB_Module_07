import argparse

from src.CRUD import create_group, create_teacher, create_grade, create_discipline, create_student
from src.CRUD import show_grades, show_students, show_disciplines, show_teachers, show_groups
from src.CRUD import update_student, update_teacher, update_discipline, update_group, update_grade
from src.CRUD import delete_student, delete_group, delete_teacher, delete_discipline, delete_grade

parser = argparse.ArgumentParser(description='CLI CreateReadUpdateDelete')

parser.add_argument('-a', '--action', help='Command: create, show, update, delete', required=True)
parser.add_argument('-m', '--model', help='Student, Teacher, Group, Discipline, Grade', required=True)
parser.add_argument('-n', '--name', help='Name of model"s object')
parser.add_argument('-fn', '--fullname', help='Name of model"s object')
parser.add_argument('-sid', '--student_id')
parser.add_argument('-tid', '--teacher_id')
parser.add_argument('-gid', '--group_id')
parser.add_argument('-did', '--discipline_id')
parser.add_argument('-grid', '--grade_id')
parser.add_argument('-g', '--grade')
parser.add_argument('-d', '--date_of')


def crud():
    args = parser.parse_args()
    print(args)
    arg = vars(args)

    action = arg.get('action')
    model = arg.get('model')
    date = arg.get('date_of')
    fullname = arg.get('fullname')
    name = arg.get('name')
    g_id = arg.get('group_id')
    t_id = arg.get('teacher_id')
    d_id = arg.get('discipline_id')
    s_id = arg.get('student_id')
    grade = arg.get('grade')
    gr_id = arg.get('grade_id')

    match action:
        case 'create':
            if model == 'Teacher':
                create_teacher(fullname)
            elif model == 'Student':
                create_student(fullname, g_id)
            elif model == 'Group':
                create_group(name)
            elif model == 'Discipline':
                create_discipline(name, t_id)
            elif model == 'Grade':
                create_grade(grade, date, s_id, d_id)
        case 'show':
            if model == 'Teacher':
                show_teachers()
            elif model == 'Student':
                show_students()
            elif model == 'Group':
                show_groups()
            elif model == 'Discipline':
                show_disciplines()
            elif model == 'Grade':
                show_grades()
        case 'update':
            if model == 'Teacher':
                update_teacher()
            elif model == 'Student':
                update_student(s_id, fullname, g_id)
            elif model == 'Group':
                update_group()
            elif model == 'Discipline':
                update_discipline()
            elif model == 'Grade':
                update_grade()
        case 'delete':
            if model == 'Teacher':
                delete_teacher(t_id)
            elif model == 'Student':
                delete_student(s_id)
            elif model == 'Group':
                delete_group(g_id)
            elif model == 'Discipline':
                delete_discipline(d_id)
            elif model == 'Grade':
                delete_grade(gr_id)
        case _:
            print("Error")


if __name__ == "__main__":
    crud()
