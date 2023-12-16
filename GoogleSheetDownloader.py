import os
import sys
import pygsheets

# config setting
service_file = 'project.json'
txt_file_path = 'sheetPath.txt'
csv_filenames = ['example1', 'example2']
sheet_name = ['example1', 'example2']

if __name__ == "__main__":
    path = sys.argv[1]
    # 測試用
    #path = os.getcwd()
    os.chdir(path)
    if os.path.exists(txt_file_path) and os.path.exists(service_file):
        file = open(txt_file_path, 'r')
        url = file.read()
        file.close()
        for filename in csv_filenames:
            if os.path.exists(filename + '.csv'):
                os.remove(filename + '.csv')
        google_connect = pygsheets.authorize(service_file=service_file)
        sheet = google_connect.open_by_url(url)
        workspace_list = sheet.worksheets()
        titles = {}
        for each in workspace_list:
            titles[each.title] = each

        titles[sheet_name[0]].export(pygsheets.ExportType.CSV, filename=csv_filenames[0])
        titles[sheet_name[1]].export(pygsheets.ExportType.CSV, filename=csv_filenames[1])
