from tika import parser

if __name__ == "__main__":

    doc = "23-25-trio-clinical-report.pdf"
    parsed_pdf = parser.from_file(doc)

    print(parsed_pdf['text'])
