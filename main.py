import PySimpleGUI as sg
import FormBase_Custom as fc
import FormBase_Orders as fo
import FormBase_Transaction as ft

sg.theme('Dark Blue 3')

layout = [  [sg.Text('Загрузка отчёта')],
            [sg.Text('Custom'), sg.InputText(), sg.FileBrowse(),],
            [sg.Text('Orders'), sg.InputText(), sg.FileBrowse(),],
            [sg.Text('Transactions'), sg.InputText(), sg.FileBrowse(),],
            [sg.Button('Form data base'),],
            [sg.Output(size=(88, 9))],
            [sg.Button('Save'), sg.Button('Cancel')] ]

window = sg.Window('Form BD', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Cancel':
        break
    if event == 'Form data base':
        passoffileC = '' + values[0]
        passoffileO = '' + values[1]
        passoffileT = '' + values[2]
        fc.form_custom_base(str(passoffileC))
        mycount = fc.service(passoffileC)
        fo.form_order_base(str(passoffileO))
        ft.form_transaction_base(str(passoffileT))
        print('Базы готовы к работе!')
        print(f'Обработано {mycount[0]} клиентов.')
        print(f'В базе {mycount[1]} юридических лиц.')
        print(f'В базе {mycount[2]} физических лиц.')

    if event == 'Save':
        passoffileC = '' + values[0]
        savepass = sg.popup_get_folder('Куда сохранить отчёт?')
        fc.savexcl(savepass, passoffileC)
        print('Отчёт сохранён.')

    # print(event, values) #debug

window.close()