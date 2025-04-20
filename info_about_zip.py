import zipfile
from zipfile import ZipFile
from pypdf import PdfReader
import pandas as pd
from PyPDF2 import PdfReader
from io import BytesIO

with ZipFile("myzip.zip", "a") as test:
    print(test.infolist())


def read_csv_from_zip_pandas(zip_path, csv_filename):
    with zipfile.ZipFile("myzip.zip") as zf:
        with zf.open("outpu1.csv") as csv_file:
            # For pandas, we can read directly from the file object
            df = pd.read_csv(csv_file)

    return df


zip_file = 'myzip.zip'
csv_file = 'outpu1.csv'
df = read_csv_from_zip_pandas("myzip.zip", "outpu1.csv")

print(df.head())
assert "plu" in df


def read_xlsx_from_zip(zip_path, xlsx_filename, sheet_name=0):
    with zipfile.ZipFile("myzip.zip") as zf:
        with zf.open("item1.xlsx") as xlsx_file:
            excel_data = BytesIO(xlsx_file.read())
            return pd.read_excel(excel_data, sheet_name=sheet_name)


zip_file = 'myzip.zip'
xlsx_file = 'item1.xlsx'
df = read_xlsx_from_zip('myzip.zip', 'item1.xlsx')

print(f"Read {len(df)} rows from {xlsx_file}")
print(df.head())
assert "new" in df


def read_pdf_from_zip(zip_path, pdf_filename, page_limit=None):
    text = ""

    with zipfile.ZipFile("myzip.zip") as zf:
        with zf.open("Untitled document.pdf") as pdf_file:
            pdf_data = BytesIO(pdf_file.read())
            reader = PdfReader(pdf_data)
            for i, page in enumerate(reader.pages):
                if page_limit and i >= page_limit:
                    break
                text += page.extract_text() + "\n\n"

    return text


zip_file = 'documents.zip'
pdf_file = 'report.pdf'
pdf_text = read_pdf_from_zip(zip_file, pdf_file, page_limit=1)
print(f"First page:\n{pdf_text[:1000]}...")  # Print first 1000 chars
assert "решение" in pdf_text
