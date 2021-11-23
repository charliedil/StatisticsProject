import tabula
import argparse
import student
import sampling


def parse_csv(csv_path):
    file = open(csv_path, "r")
    text = file.read()
    file.close()
    lines = text.split("\n")
    students = []
    for line in lines[1:len(lines)-1]:
        attr = line.split(",")
        students.append(student.Student(attr[0], attr[1], attr[2], attr[3], attr[4]))
    return students


def write_out_samples(samples, output):
    file = open(output, "w")
    file.write("ID Number, Sex, Teacher, Status, SOL score\n")
    for sample in samples:
        file.write(sample.id+","+sample.sex+","+sample.teacher+","+sample.status+","+sample.score+"\n")
    file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Run scraper/sampler on dataset")
    parser.add_argument('--pdf', type=str, help="Provide path to input pdf. Required if no path for csv is provided")
    parser.add_argument('--csv', type=str, help="Provide path to input csv. Required if no path to pdf is provided")
    parser.add_argument('--output', type=str, help="Provide path to where processed data should go. Default is data "
                                                   "subdirectory")
    parser.add_argument("--block", type=str, help="If you want to do block SRS, what category do you wish for the "
                                                  "blocks to be (Options: Sex, teacher, or status). Default will be"
                                                  "regular SRS.")
    parser.add_argument("--sample_size", type=int, help="Required for regular SRS. Size of the desired samples.", default=-1)
    parser.add_argument("--num_subgroups", type=int, help="Required for block SRS. Number of blocks desired.", default=-1)
    parser.add_argument("--subgroup_size", type=int, help="Required for block SRS. Size of subgroup samples.",default=-1)
    args = parser.parse_args()

    pdf_path = args.pdf
    csv_path = args.csv
    output_path = args.output
    block = args.block
    sample_size = args.sample_size
    num_subgroups = args.num_subgroups
    subgroup_size = args.subgroup_size
    categories = ["sex", "teacher", "status"]

    # check for whether we will be doing regular srs or block srs.
    srs = False
    if block is None:
        srs = True
    else:
        block = block.lower()
    scraper = True

    # Flags for whether paths are given
    if pdf_path is None and csv_path is not None:
        scraper = False
    if output_path is None:
        output_path = "data/"

    # Error handling
    if pdf_path is None and csv_path is None:
        print("Either pdf path or csv path must be provided.")
        exit(-1)
    if not srs and block not in categories:
        print("If block srs, then the category should be either sex, teacher, or status")
        exit(-1)
    if not srs and (num_subgroups<=0 or subgroup_size<=0):
        print("If block srs, then specify num_subgroups and subgroup_size with a positive integer.")
        exit(-1)
    if srs and sample_size <=0:
        print("if srs, then specify sample_size with a positive integer.")
        exit(-1)
    # actual algorithm
    if scraper:
        tabula.convert_into(pdf_path, output_path + "studentData.csv", pages='all')
        csv_path = output_path + "studentData.csv"
    students = parse_csv(csv_path)
    samples = []
    if srs:
        samples = sampling.srs(students, sample_size)
    else:
        samples = sampling.block_srs(students, num_subgroups, subgroup_size, block)
    write_out_samples(samples, output_path + "sample.csv")


