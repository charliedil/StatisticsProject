import tabula
import argparse
import student


def parse_csv(csv_path):
    file = open(csv_path, "r")
    text = file.read()
    lines = text.split("\n")
    students = []
    for line in lines[1:len(lines)-1]:
        attr = line.split(",")
        students.append(student.Student(attr[0], attr[1], attr[2], attr[3], attr[4]))
    return students


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Run scraper/sampler on dataset")
    parser.add_argument('--pdf', type=str, help="Provide path to input pdf. Required if no path for csv is provided")
    parser.add_argument('--csv', type=str, help="Provide path to input csv. Required if no path to pdf is provided")
    parser.add_argument('--output', type=str, help="Provide path to where processed data should go. Default is data "
                                                   "subdirectory")
    args = parser.parse_args()

    pdf_path = args.pdf
    csv_path = args.csv
    output_path = args.output
    scraper = True
    print(pdf_path)
    # Flags for whether paths are given
    if pdf_path is None and csv_path is not None:
        scraper = False
    if output_path is None:
        output_path = "data/"
    # Error handling
    if pdf_path is None and csv_path is None:
        print("Either pdf path or csv path must be provided.")
        exit(-1)
    # actual algorithm
    if scraper:
        tabula.convert_into(pdf_path, output_path + "studentData.csv", pages='all')
        csv_path = output_path + "studentData.csv"
    students = parse_csv(csv_path)
    print(students)
