from zipfile import ZipFile

with ZipFile("myzip.zip", "w") as test:
    test.write("pdf_sample.pdf")
    test.write("item1.xlsx")
    test.write("outpu1.csv")
