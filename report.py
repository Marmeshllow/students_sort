import csv
import pandas as pd
import openpyxl
import os

students_avg_scores = {'Max': 4.964, 'Eric': 4.962, 'Peter': 4.923, 'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973,
                       'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936, 'Zoi': 4.937}


def make_report_about_top3(avg):
    res = sorted(avg.items(), key=lambda x: x[1], reverse=True)
    df = pd.DataFrame(res[:3])
    df.to_csv('result.csv', index=False, header=None)
    path = os.path.join(os.getcwd(), 'result.csv')
    return path


def make_report_about_top3_v2(avg):
    res = sorted(avg.items(), key=lambda x: x[1], reverse=True)
    with open('result.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(res[:3])
    path = os.path.join(os.getcwd(), 'result.csv')
    return path

def make_report_about_top3_v3(avg):
    res = sorted(avg.items(), key=lambda x: x[1], reverse=True)
    excel_file = openpyxl.Workbook()
    excel_sheet = excel_file.create_sheet(title='Best students', index=0)
    excel_sheet['A1'] = 'Name'
    excel_sheet['B1'] = 'Score'
    for row in res[:3]:
        excel_sheet.append(row)
    excel_file.save('result.xlsx')
    path = os.path.join(os.getcwd(), 'result.xlsx')
    return path
