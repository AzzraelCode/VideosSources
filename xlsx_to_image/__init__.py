# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
from PIL import ImageGrab

from config import get_path

# https://pypi.org/project/pywin32/
import win32com.client


def main():
    print("I'm %s at %s" % (__name__, get_path(__name__)))
    xlsx_path = get_path('data', 'sample.xlsx')
    # https://stackoverflow.com/questions/44850522/python-export-excel-sheet-range-as-image

    # https://docs.microsoft.com/ru-ru/office/vba/api/excel.application(object)
    client = win32com.client.Dispatch("Excel.Application")
    # https://docs.microsoft.com/ru-ru/office/vba/api/excel.workbooks
    wb = client.Workbooks.Open(xlsx_path)
    # https://docs.microsoft.com/ru-ru/office/vba/api/excel.worksheet
    # ws = wb.ActiveSheet
    ws = wb.Worksheets("Sheet1")

    # for v in ws.Range("A1"): print(v)

    # https://docs.microsoft.com/ru-ru/office/vba/api/excel.range.copypicture
    ws.Range("A1:D6").CopyPicture(Format = 2)

    img = ImageGrab.grabclipboard()
    img.save(get_path('data', 'image.jpg'))

    wb.Close() # иначе табл будет открыта
    client.Quit()