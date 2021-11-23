from random import randrange

def srs(entities, sample_size):
    if len(entities) < sample_size: # check sample size
        print("ERROR: sample size cannot be bigger than number of entities")
        exit(-1)
    entity_sample = []
    chosen_numbers = []
    for i in range(sample_size):
        index = randrange(sample_size)
        while index in chosen_numbers:
            index = randrange(sample_size)
        entity_sample.append(entities[index])
        chosen_numbers.append(index)
    return entity_sample

def block_srs(students, num_subgroups, subgroup_size, category):
    entity_sample = []
    if category == "teacher":
        stud_to_teacher = {}
        teacher_min = {}
        for student in students:
            if student.teacher not in stud_to_teacher:
                stud_to_teacher[student.teacher] = []
                teacher_min[student.teacher] = 0
            stud_to_teacher[student.teacher].append(student)
            teacher_min[student.teacher] += 1
        if len(stud_to_teacher) < num_subgroups:
            print("ERROR: number of subgroups cannot exceed the block category")
            exit(-1)
        if min(list(teacher_min.values())) < subgroup_size:
            print("ERROR: subgroup size cannot exceed minimum amount of students assigned to any individual block "
                  "category")
            exit(-1)
        teachers = srs(list(stud_to_teacher.keys()), num_subgroups)
        for teacher in teachers:
            students_of_teacher_sample = srs(stud_to_teacher[teacher], subgroup_size)
            for s in students_of_teacher_sample:
                entity_sample.append(s)
    elif category == "sex":
        stud_to_sex = {}
        sex_min = {}
        for student in students:
            if student.sex not in stud_to_sex:
                stud_to_sex[student.sex] = []
                sex_min[student.sex] = 0
            stud_to_sex[student.sex].append(student)
            sex_min[student.sex] += 1
        if len(stud_to_sex) < num_subgroups:
            print("ERROR: number of subgroups cannot exceed the block category")
            exit(-1)
        if min(list(sex_min.values())) < subgroup_size:
            print("ERROR: subgroup size cannot exceed minimum amount of students assigned to any individual block "
                  "category")
            exit(-1)
        sexes = srs(list(stud_to_sex.keys()), num_subgroups)
        for sex in sexes:
            students_of_sex_sample = srs(stud_to_sex[sex], subgroup_size)
            for s in students_of_sex_sample:
                entity_sample.append(s)
    else:
        stud_to_status = {}
        status_min = {}
        for student in students:
            if student.status not in stud_to_status:
                stud_to_status[student.status] = []
                status_min[student.status] = 0
            stud_to_status[student.status].append(student)
            status_min[student.status] += 1
        if len(stud_to_status) < num_subgroups:
            print("ERROR: number of subgroups cannot exceed the block category")
            exit(-1)
        if min(list(status_min.values())) < subgroup_size:
            print("ERROR: subgroup size cannot exceed minimum amount of students assigned to any individual block "
                  "category")
            exit(-1)
        statuses = srs(list(stud_to_status.keys()), num_subgroups)
        for status in statuses:
            students_of_status_sample = srs(stud_to_status[status], subgroup_size)
            for s in students_of_status_sample:
                entity_sample.append(s)
    return entity_sample


