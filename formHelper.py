
def form_tel (onerow, i):
    telList = str(onerow[i])
    newTel = ''
    if type(telList) == str:
        for s in telList:
            if '0' <= s <= '9':
                newTel += s
        if newTel == '':
            onerow[i] = '+7-000-000-00-00'
        else:
            if len(newTel) <= 10:
                newTel = newTel.zfill(11)
                newTel = ('+7-{}-{}-{}-{}'.format(newTel[1:4], newTel[4:7], newTel[7:9], newTel[9:11]))
                onerow[i] = newTel
            elif len(newTel) > 11:
                writel = ''
                try:
                    twonum = telList.split(',')
                    for num in twonum:
                        newTel3 = ''
                        for n in num:
                            if '0' <= n <= '9':
                                newTel3 += n
                        if len(newTel3) <= 10:
                            newTel2 = newTel3.zfill(11)
                            newTel2 = ('+7-{}-{}-{}-{}'.format(newTel2[1:4], newTel2[4:7], newTel2[7:9], newTel2[9:11]))
                        else:
                            newTel2 = ('+7-{}-{}-{}-{}'.format(newTel3[1:4], newTel3[4:7], newTel3[7:9], newTel3[9:11]))
                        writel += newTel2 + '; '
                    onerow[i] = writel
                except:
                    onerow[i] = newTel
                    #onerow[4] = 'wrong number'
            else:
                newTel = ('+7-{}-{}-{}-{}'.format(newTel[1:4], newTel[4:7], newTel[7:9], newTel[9:11]))
                onerow[i] = newTel
    return onerow


def form_name(onerow):
    if onerow[8] != 'Юридическое лицо':
        nameList = str(onerow[0])
        strname = ['ова', 'ева', 'кий', 'кая', 'ная', 'ный', 'ман', 'ов', 'ев', 'их', 'ко', 'лин', 'ина', 'ин', 'Савва', 'Илья', 'Добрыня']
        try:
            names = nameList.split(' ')
            if len(names) == 3:
                onerow[1] = names[0]
                onerow[2] = names[1]
                onerow[3] = names[2]
            elif len(names) == 2:
                if names[1][-3:] =='вич' or names[1][:-3] =='вна':
                    onerow[2] = names[0]
                    onerow[3] = names[1]
                elif names[1][-2:] in strname or names[1][-3:] in strname:
                    onerow[2] = names[0]
                    onerow[1] = names[1]
                elif names[0][-2:] in strname or names[0][-3:] in strname:
                    onerow[2] = names[1]
                    onerow[1] = names[0]
                else:
                    if onerow[2] == '':
                        onerow[2] = onerow[0]
            else:
                if onerow[2] == '':
                    onerow[2] = onerow[0]
        except:
            if onerow[2] == '':
                onerow[2] = onerow[0]
        return onerow
    else:
        onerow[2] = onerow[0]
        return onerow


def form_gender(onerow):
    if onerow[8] == 'Юридическое лицо':
        gender = '-'
    else:
        strname = ['Кузьма', 'Лука', 'Никита', 'Абдула', 'Савва', 'Илья', 'Добрыня']
        testname = str(onerow[2])
        if onerow[2] in strname:
            gender = 'male'
        elif testname[-1:] == 'а' or testname[-1:] == 'я' or testname[1:] == 'юбовь':
            gender = 'female'
        else:
            gender = 'male'
    onerow.append(gender)
    return onerow


def form_type(onerow):
    custname = onerow[0]
    custtype = onerow[8]
    str = ['ООО', 'бществ', 'БЩЕСТВ', 'АО', 'ИП', 'предприним', 'ПРЕДПРИНИМ', '"', '«', 'КЦ', 'ентр', 'энер', 'сталь', 'ГК', 'омпани', 'оссии', 'СОШ', 'плюс']
    for st in str:
        if custtype == 'Контактное лицо':
            break
        elif custname.find(st) != -1:
            onerow[8] = 'Юридическое лицо'
            break
        else:
            onerow[8] = 'Физическое лицо'
    return onerow


def form_order_num(onerow, i):
    numlist = str(onerow[i])
    newNum = ''
    try:
        nums = numlist.split('/')
        for num in nums:
            for s in num:
                if '0' <= s <= '9':
                    newNum += s
            newNum += ' '
    except:
        for s in numlist:
            if '0' <= s <= '9':
                newNum += s
    onerow.append(newNum)