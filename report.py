import csv
import pandas as pd
students_avg_scores = {'Max': 4.964, 'Eric': 4.962, 'Peter': 4.923, 'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973,
                       'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936, 'Zoi': 4.937}


def make_report_about_top3(avg):
    res = sorted(avg.items(), key=lambda x: x[1], reverse=True)
    df = pd.DataFrame(res[:3])
    df.to_csv('result.csv', index=False, header=None)


def make_report_about_top3_v2(avg):
    res = sorted(avg.items(), key=lambda x: x[1], reverse=True)
    with open('result.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(res[:3])


make_report_about_top3(students_avg_scores)
