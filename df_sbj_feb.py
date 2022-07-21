import pandas as pd
from math import isnan
from tabula.io import read_pdf


def return_feb():

    # # Сброс ограничений на количество выводимых рядов
    # pd.set_option('display.max_rows', None)
    #
    # # Сброс ограничений на число столбцов
    # pd.set_option('display.max_columns', None)
    #
    # # Сброс ограничений на количество символов в записи
    # pd.set_option('display.max_colwidth', None)

    # file = "df_org_2.pdf"
    # path = 'cpr/' + file
    path = r'../df_org_2.pdf'
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
    avg_mnth_wage = []
    nmb_labour_force = []
    nmb_working = []
    unemploy_rate = []
    for page in [('266', '267'), ('268', '269'), ('270', '271'), ('272', '273'), ('290', '291'), ('292', '293'),
                 ('310', '311'), ('312', '313'), ('314', '315')]:
        df1 = read_pdf(path, pages=page[0], multiple_tables=False)
        df2 = read_pdf(path, pages=page[1], multiple_tables=False)
        if page == ('266', '267'):
            for item in list(df1[0]['Введено,\r2тыс. м  общей площади жилых\rпомещений с учетом жилых домов,\rпостроенных на земельных\rучастках для ведения садоводства']):
                liv_sp.append(item)
            for item in list((df2[0]['Введено,\r2тыс. м  общей площади жилых\rпомещений с учетом жилых домов,\rпостроенных на земельных\rучастках для ведения садоводства'])[:-1]):
                liv_sp.append(item)
        if page == ('268', '269'):
            for item in list(df1[0]['1)Январь-февраль 2022 г. Февраль 2022 г. в % к'])[3:]:
                if item != 'в том числе:' and type(item) == str:
                    turn_retail.append(item.split()[0])
            for item in list(df2[0]['1) Январь-февраль 2022 г.'])[3:-1]:
                if item != 'в том числе:' and type(item) == str:
                    turn_retail.append(item.split()[-1])
        if page == ('270', '271'):
            for item in list(df1[0]['1) Январь-февраль 2022 г.'])[3:]:
                if item != 'в том числе:'  and type(item) == str:
                    turn_catering.append(item.split()[0])
            for item in list(df2[0]['1) Январь-февраль 2022 г.'])[3:-1]:
                if item != 'в том числе:' and type(item) == str:
                    turn_catering.append(item.split()[-1])
        if page == ('272', '273'):
            for item in list(df1[0]['1) Январь-февраль 2022 г.'])[3:]:
                if item != 'в том числе:' and type(item) == str:
                    turn_pservice.append(item.split()[0])
            for item in list(df2[0]['1) Январь-февраль 2022 г.'])[3:-1]:
                if item != 'в том числе:' and type(item) == str:
                    turn_pservice.append(item.split()[-1])
        if page == ('290', '291'):
            for item in list(df1[0]['К предыдущему месяцу'])[5:]:
                if item != 'в том числе:' and type(item) == str:
                    i = item.split()
                    cpi_good_service.append(i[0])
                    cpi_food_pr.append(i[1])
                    cpi_nonfood_pr.append(i[2])
                    cpi_service.append(i[3])
            for item in list(df2[0]['К предыдущему месяцу'])[2:]:
                if item != 'в том числе:' and type(item) == str:
                    cpi_good_service.append(item)
            for item in list(df2[0]['К декабрю 2021 г.'])[2:]:
                if item != 'в том числе:' and type(item) == str:
                    cpi_food_pr.append(item)
            for item in list(df2[0]['Unnamed: 3'])[2:]:
                if item != 'в том числе:' and type(item) == str:
                    cpi_nonfood_pr.append(item)
            for item in list(df2[0]['Unnamed: 4'])[2:]:
                if item != 'в том числе:' and type(item) == str:
                    cpi_service.append(item)
        if page == ('292', '293'):
            for item in list(df1[0]['Стоимость набора'][3:]):
                if item != 'в том числе:' and type(item) == str:
                    i = item.split()
                    cost_fix_set_r.append(i[0])
                    cost_fix_set_p.append(i[1])
            for item in list((df2[0]['Стоимость набора'])[1:]):
                if item != 'в том числе:' and type(item) == str:
                    cost_fix_set_r.append(item)
            for item in list((df2[0]['Изменение стоимости набора, в %'])[1:]):
                if item != 'в том числе:' and type(item) == str:
                    cost_fix_set_p.append(item)
            cost_fix_set_r.insert(25, 'нет данных')
            cost_fix_set_p.insert(25, 'нет данных')
            cost_fix_set_r.insert(71, 'нет данных')
            cost_fix_set_p.insert(71, 'нет данных')
        if page == ('310', '311'):
            for item in list(df1[0]['Unnamed: 1'])[5:]:
                if item != 'в том числе:' and type(item) == str:
                    avg_mnth_wage.append(item)

            for item in list(df2[0]['Рублей'])[1:]:
                if item != 'в том числе:' and type(item) == float:
                    avg_mnth_wage.append(item)
        if page == ('312', '313'):
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
        if page == ('314', '315'):
            for item in list((df1[0]['Февраль\r2022 г.'])[1:]):
                if item != 'в том числе:' and type(item) == str:
                    unemploy_rate.append(item)
            for item in list((df2[0]['Февраль\r2022 г.'])[1:]):
                if item != 'в том числе:' and type(item) == str:
                    unemploy_rate.append(item)
    return liv_sp, turn_retail, turn_catering, turn_pservice, cpi_good_service, cpi_food_pr, \
           cpi_nonfood_pr, cpi_service, cost_fix_set_r, cost_fix_set_p, avg_mnth_wage, \
           nmb_labour_force, nmb_working, unemploy_rate
