con = [
    {'name': 'vasya', 'scores': {'math': 58, 'res_lang': 62, 'cs': 48}, 'extra': 0},    # 168
    {'name': 'fedya', 'scores': {'math': 33, 'res_lang': 85, 'cs': 42}, 'extra': 2},    # 162
    {'name': 'petya1', 'scores': {'math': 92, 'res_lang': 33, 'cs': 34}, 'extra': 1},   # 160
    {'name': 'petya2', 'scores': {'math': 100, 'res_lang': 30, 'cs': 29}, 'extra': 1},  # 160
]


def find_top_20(con_lst):
    lst = sorted(con_lst, key=lambda x: (x['scores']['math'] + x['scores']['res_lang'] + x['scores']['cs'] + x['extra'],
                 x['scores']['math'] + x['scores']['cs']),
                 reverse=True)
    result = [student.get('name') for student in lst[:20]]
    return result
