import PySimpleGUI as sg
import FormBase_Custom as fc
import FormBase_Orders as fo
import FormBase_Transaction as ft
import Find_Info as fi


sg.theme('Dark Blue 3')

layout = [[sg.Text('Загрузка отчётов')],
            [sg.Text('Клиенты    '), sg.InputText(), sg.FileBrowse(),],
            [sg.Text('Заказы      '), sg.InputText(), sg.FileBrowse(),],
            [sg.Text('Транзакции'), sg.InputText(), sg.FileBrowse(),],
            [sg.Button('Подготовить базы'),],
            [sg.Output(size=(88, 9))],
            [sg.Button('Поиск транзакции'), sg.Button('Поиск клиента')],
            [sg.Button('Сохранить базу в Excel'), sg.Button('Cancel')]]

window = sg.Window('Form BD', layout)

def my_little_window():
    layout_t = [[sg.Text('№ транзакции')], [sg.InputText()],
                [sg.Button('Find')],
                [sg.Output(size=(88, 5))],
                [sg.Table(values=[['','','','','','']], headings=['1', '2', '3', '4', '5', '6'],
                    auto_size_columns=False,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=20,
                    # row_height=35,
                    size=(100, 5),
                    key='table',
                    tooltip='Данные по транзакции')]]

    window = sg.Window('Поиск транзакции', layout_t)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Cancel':
            break
        if event == 'Find':
            number = values[0]
            bdpass = sg.popup_get_folder('Откройте папку с базой данных')
            result = fi.find_transaction(bdpass, number)
            a = []
            for res in result:
                res = list(res)
                a.append(res)
            window.Element('table').Update(values=a)
            print(result)
            print(a)


def find_custom():
    layout_t = [[sg.Text('Телефон')], [sg.InputText()],
                [sg.Text('Имя')], [sg.InputText()],
                [sg.Button('Find')],
                [sg.Output(size=(100, 5))],
                [sg.Table(values=[[1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 0, 0, 0]], headings=['client', 'gender', 'tel', 'mail', 'client_type'],
                def_col_width = 20,
                auto_size_columns=False,
                display_row_numbers=True,
                justification='right',
                num_rows=10,
                row_height=55,
                size=(88, 88),
                key='table')]]

    window = sg.Window('Поиск клиента', layout_t)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Cancel':
            break
        if event == 'Find':
            if values[0] != '':
                number = values[0]
                bdpass = sg.popup_get_folder('Откройте папку с базой данных')
                result = fi.find_custom_tel(bdpass, number)
                a = []
                for res in result:
                    res = list(res)
                    a.append(res)
                window.Element('table').Update(values=a)

                print(a)
            elif values[1] != '':
                name = values[1]
                bdpass = sg.popup_get_folder('Откройте папку с базой данных')
                result = fi.find_custom_name(bdpass, name)
                a = []
                for res in result:
                    res = list(res)
                    a.append(res)
                window.Element('table').Update(values=a)

                print(a)



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Cancel':
        break
    if event == 'Подготовить базы':
        passoffileC = '' + values[0]
        passoffileO = '' + values[1]
        passoffileT = '' + values[2]
        fc.form_custom_base(passoffileC)
        mycount = fc.service(passoffileC)
        fo.form_order_base(passoffileO, passoffileC)
        ft.form_transaction_base(passoffileT, passoffileC)
        print('Базы готовы к работе')
        print(f'Обработано {mycount[0]} клиентов.')
        print(f'В базе {mycount[1]} юридических лиц.')
        print(f'В базе {mycount[2]} физических лиц.')

    if event == 'Поиск транзакции':
        my_little_window()

    if event == 'Поиск клиента':
        find_custom()

    if event == 'Сохранить базу в Excel':
        passoffileC = '' + values[0]
        savepass = sg.popup_get_folder('Куда сохранить?')
        fc.savexcl(savepass, passoffileC)
        print('Базы сохранены.')

    # print(event, values) #debug

window.close()