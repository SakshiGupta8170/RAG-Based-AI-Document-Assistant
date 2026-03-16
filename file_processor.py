import pandas as pd
import pdfplumber


def read_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


def read_csv(file):
    df = pd.read_csv(file)
    return df.to_string(index=False)


def read_excel(file):
    df = pd.read_excel(file)
    return df.to_string(index=False)


def read_txt(file):
    return file.read().decode("utf-8")


def process_file(file):
    name = file.name.lower()

    if name.endswith(".pdf"):
        return read_pdf(file)
    elif name.endswith(".csv"):
        return read_csv(file)
    elif name.endswith(".xlsx") or name.endswith(".xls"):
        return read_excel(file)
    elif name.endswith(".txt"):
        return read_txt(file)
    else:
        return ""