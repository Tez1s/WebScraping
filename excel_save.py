import xlsxwriter
from scraper import set


def writer(parametr):
    book = xlsxwriter.Workbook(r"C:\Users\38066\Desktop\sp_save_e.xlsx")
    page = book.add_worksheet("product")

    row = 0
    column = 0

    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 70)
    page.set_column("D:D", 70)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        row += 1

    book.close()


writer(set)
