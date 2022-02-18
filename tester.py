# import PySimpleGUI as sg
#
#
# def hi(result):
#     a = []
#     for res in result:
#         res = list(res)
#         a.append(res)
#
#     print(a)
#     print(type(a[0]))
#     return a
#
# def my_little_window(result):
#     layout_c = [[sg.Table(values=[['0','0','0', 0, 0]], headings=['-','-','-','-','55'],
#                     auto_size_columns=False,
#                     # display_row_numbers=False,
#                     justification='right',
#                     num_rows=20,
#                     row_height=35,
#                     size=(88, 20),
#                     key='table',
#                     tooltip='Данные по транзакции')],[sg.Button('Find')]]
#
#     window = sg.Window('Поиск транзакции', layout_c)
#     while True:
#         event, values = window.read()
#         if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Cancel':
#             break
#         if event == 'Find':
#             a = hi(result)
#             window.Element('table').Update(values=a)
#
#
# result = [('ss', 33, 'dee',555), [2, 44, 'ff', 4,'44','3'], (3, 4, 4, "fdd")]
# my_little_window(result)

# # ---------------
# import PySimpleGUI as sg
# import random
# import string
#
# sg.theme('Dark Green')
#
# data = [('ss', 33, 'dee'), [2, 44, 'ff', 4], (3, 4, 4, "fdd")]
# def hi(result):
#     a = []
#     for res in result:
#         res = list(res)
#         a.append(res)
#
#     print(a)
#     print(type(a[0]))
#     return a
# a = hi(data)
#
# headings = ['column 1', 'column 10', 'column 2', 'column 3', 'column 4', 'column 5']
#
# # ------ Window Layout ------
# layout = [[sg.Table(values=a, headings=headings, max_col_width=35,
#                     # background_color='light blue',
#                     auto_size_columns=True,
#                     display_row_numbers=True,
#                     justification='right',
#                     num_rows=20,
#                     alternating_row_color='lightyellow',
#                     key='-TABLE-',
#                     row_height=35,
#                     tooltip='This is a table')],
#           [sg.Button('Read')],
#           [sg.Text('Read = read which rows are selected')]]
#
# # ------ Create Window ------
# window = sg.Window('The Table Element', layout)
#
# # ------ Event Loop ------
# while True:
#     event, values = window.read()
#     print(event, values)
#     if event == sg.WIN_CLOSED:
#         break
#     if event == 'Read':
#         data2 = [['ss', 33, '44'], (21, 44, 'ggg', 4), [3, -4, 4, "fdd"]]
#         a2 = hi(data2)
#         window.Element('-TABLE-').Update(values=a2)
#
# window.close()

def rotate(lis):
    if lis != []:
        x = lis.pop()
        lis.insert(0, x)
    return lis

l = [1, 2, 3]
print(rotate(l))
