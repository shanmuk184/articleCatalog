import os
from django.conf import settings
path = os.path.join(settings.BASE_DIR, "files", "sudhakar u.xlsx")
import xlrd
from articles.models import Article
def run():
    wb = xlrd.open_workbook(path)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    rows = []
    for j in range(1, sheet.nrows):
        row = []
        for i in range(sheet.ncols):
            if i not in [10, 11]:
                if i < 4:
                    row.append(int(sheet.cell_value(j, i)))
                else:
                    row.append(sheet.cell_value(j, i))

        print(len(row))
        article = Article(
            job_id = row[0],
            ns_category_id = row[1],
            location_id = row[2],
            job_type_id = row[3],
            filename = row[4],
            job_title = row[5],
            job_slug = row[6],
            job_description = row[7],
            job_image = row[8],
            job_status = row[9],


            location = row[10],
            House_of = row[11],
            Year = row[12],
            epaperlink = row[13],
            imagelink = row[14],
            imagelinkautogenerate = row[15]
)
        article.save()
        print(article)