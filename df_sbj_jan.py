import pandas as pd
from tabula.io import read_pdf


def return_june():
    # # Сброс ограничений на количество выводимых рядов
    # pd.set_option('display.max_rows', None)
    #
    # # Сброс ограничений на число столбцов
    # pd.set_option('display.max_columns', None)
    #
    # # Сброс ограничений на количество символов в записи
    # pd.set_option('display.max_colwidth', None)

    path = r'../df_org_1.pdf'
    liv_sp = []
    turn_retail = []
    turn_catering = []
    turn_pservice = []
    cpi_good_service = []
    cpi_food_pr = []
    cpi_nonfood_pr = []
    cpi_service = []
    cost_fix_set_r = []
    cost_fix_set_p = []
    nmb_labour_force = []
    nmb_working = []
    unemploy_rate = []
    for page in [('311', '312'), ('313', '314'), ('319', '320'), ('321', '322'), ('339', '340'), ('341', '342'),
                 ('369', '370'), ('371', '372')]:
        df1 = read_pdf(path, pages=page[0], multiple_tables=False)
        df2 = read_pdf(path, pages=page[1], multiple_tables=False)
        if page == ('311', '312'):
            for item in list(df1[0]['Введено,\r2тыс. м  общей площади жилых\rпомещений с учетом жилых домов,\rпостроенных на земельных\rучастках для ведения садоводства']):
                liv_sp.append(item)
            for item in list((df2[0]['Введено,\r2тыс. м  общей площади жилых\rпомещений с учетом жилых домов,\rпостроенных на земельных\rучастках для ведения садоводства'])[:-1]):
                liv_sp.append(item)
        if page == ('313', '314'):
            for item in list(df1[0]['1) Млн'])[2:]:
                if item != 'в том числе:':
                    turn_retail.append(item.split()[-1])
            for item in list(df2[0]['Млн\rрублей'])[1:-1]:
                turn_retail.append(item)
        if page == ('319', '320'):
            for item in list(df1[0]['1) Млн'])[2:]:
                if item != 'в том числе:':
                    turn_catering.append(item.split()[-1])
            for item in list(df2[0]['Млн\rрублей'])[1:-1]:
                turn_catering.append(item)
        if page == ('321', '322'):
            for item in list(df1[0]['1) Млн'])[2:]:
                if item != 'в том числе:':
                    turn_pservice.append(item.split()[-1])
            for item in list(df2[0]['Млн\rрублей'])[1:-1]:
                turn_pservice.append(item)
        if page == ('339', '340'):
            for item in list(df1[0]['Unnamed: 1'])[5:]:
                if item != 'в том числе:' and type(item) == str:
                    cpi_good_service.append(item)
            for item in list(df1[0]['К предыдущему месяцу'])[5:]:
                if item != 'в том числе:' and type(item) == str:
                    i = item.split()
                    cpi_food_pr.append(i[0])
                    cpi_nonfood_pr.append(i[1])
            for item in list(df1[0]['Unnamed: 3'])[5:]:
                if item != 'в том числе:' and type(item) == str:
                    cpi_service.append(item)
            for item in list(df2[0]['К предыдущему месяцу'])[2:]:
                if item != 'в том числе:' and type(item) == str:
                    cpi_good_service.append(item)
            for item in list(df2[0]['Unnamed: 2'])[2:]:
                if item != 'в том числе:' and type(item) == str:
                    cpi_food_pr.append(item)
            for item in list(df2[0]['Unnamed: 3'])[2:]:
                if item != 'в том числе:' and type(item) == str:
                    cpi_nonfood_pr.append(item)
            for item in list(df2[0]['Unnamed: 4'])[2:]:
                if item != 'в том числе:' and type(item) == str:
                    cpi_service.append(item)
        if page == ('341', '342'):
            for item in list(df1[0]['Стоимость набора'][3:]):
                if item != 'в том числе:' and type(item) == str:
                    i = item.split()
                    cost_fix_set_r.append(i[0])
                    cost_fix_set_p.append(i[1])
            for item in list((df2[0]['Стоимость набора'])[1:]):
                if item != 'в том числе:' and type(item) == str:
                    cost_fix_set_r.append(item)
            for item in list((df2[0]['Изменение\rстоимости набора\rк предыдущему\rмесяцу, %'])[1:]):
                if item != 'в том числе:' and type(item) == str:
                    cost_fix_set_p.append(item)
            cost_fix_set_r.insert(25, 'нет данных')
            cost_fix_set_p.insert(25, 'нет данных')
            cost_fix_set_r.insert(71, 'нет данных')
            cost_fix_set_p.insert(71, 'нет данных')
        if page == ('369', '370'):
            for item in list((df1[0]['Численность'])[3:]):
                if item != 'в том числе:' and type(item) == str:
                    nmb_labour_force.append(item)
            for item in list((df1[0]['В том числе'])[3:]):
                if item != 'в том числе:' and type(item) == str:
                    i = item.split()
                    nmb_working.append(i[0])
            for item in list((df2[0]['Численность\rрабочей силы,\rтыс.\rчеловек'])[1:]):
                if item != 'в том числе:' and type(item) == str:
                    nmb_labour_force.append(item)
            for item in list((df2[0]['В том числе'])[1:]):
                if item != 'в том числе:' and type(item) == str:
                    nmb_working.append(item)
        if page == ('371', '372'):
            for item in list((df1[0]['Январь\r2022 г.'])[1:]):
                if item != 'в том числе:' and type(item) == str:
                    unemploy_rate.append(item)
            for item in list((df2[0]['Январь\r2022 г.'])[1:]):
                if item != 'в том числе:' and type(item) == str:
                    unemploy_rate.append(item)
    return liv_sp, turn_retail, turn_catering, turn_pservice, cpi_good_service, cpi_food_pr, \
           cpi_nonfood_pr, cpi_service, cost_fix_set_r, cost_fix_set_p, nmb_labour_force, nmb_working, unemploy_rate

