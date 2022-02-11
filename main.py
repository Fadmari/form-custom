import PySimpleGUI as sg
import FormBase_Custom as fc
import FormBase_Orders as fo
import FormBase_Transaction as ft
import Find_Info as fi

sg.theme('Dark Blue 3')

layout = [  [sg.Text('Загрузка отчётов')],
            [sg.Text('Клиенты   '), sg.InputText(), sg.FileBrowse(),],
            [sg.Text('Заказы     '), sg.InputText(), sg.FileBrowse(),],
            [sg.Text('Танзакции'), sg.InputText(), sg.FileBrowse(),],
            [sg.Button('Подготовить базы'),],
            [sg.Output(size=(88, 9))],
            [sg.Button('Поиск транзакции'),],
            [sg.Button('Сохранить базу киентов'), sg.Button('Cancel')] ]

window = sg.Window('Form BD', layout)

def my_little_window():
    layout_c = [[sg.Text('№ транзакции')], [sg.InputText()],
                [sg.Button('Find')],
                [sg.Output(size=(88, 5))]]

    window = sg.Window('Поиск транзакции', layout_c)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Cancel':
            break
        if event == 'Find':
            number = values[0]
            bdpass = sg.popup_get_folder('Откройте папку с базой данных')
            result = fi.find_transaction(bdpass, number)
            print(result)


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

    if event == 'Сохранить базу киентов':
        passoffileC = '' + values[0]
        savepass = sg.popup_get_folder('Куда сохранить базу клиентов?')
        fc.savexcl(savepass, passoffileC)
        print('База сохранена.')

    # print(event, values) #debug

window.close()