import pandas as pd
from tabula.io import read_pdf

def return_mar():

    # # Сброс ограничений на количество выводимых рядов
    # pd.set_option('display.max_rows', None)
    #
    # # Сброс ограничений на число столбцов
    # pd.set_option('display.max_columns', None)
    #
    # # Сброс ограничений на количество символов в записи
    # pd.set_option('display.max_colwidth', None)

    # file = "df_org_3.pdf"
    # path = 'cpr/' + file
    path = r'../df_org_3.pdf'
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
    pr_h_pi = []
    sec_h_pi = []
    avg_mnth_wage = []
    nmb_labour_force = []
    nmb_working = []
    unemploy_rate = []
    for page in [('262', '263'), ('266', '267'), ('270', '271'), ('272', '273'), ('284', '285'), ('286', '287'),
                 ('288', '289'), ('300', '301'), ('302', '303'), ('304', '305')]:
        if page == ('300', '301'):
            df1 = read_pdf(path, pages='300', multiple_tables=False, pandas_options={'names': [1, 2, 3, 4, 5, 6]})
        else:
            df1 = read_pdf(path, pages=page[0], multiple_tables=False, pandas_options={'on_bad_lines': 'skip'})
        df2 = read_pdf(path, pages=page[1], multiple_tables=False)
        if page == ('262', '263'):
            for item in list(df1[0]['Введено,\r2тыс. м  общей площади жилых\rпомещений с учетом жилых домов,\rпостроенных на земельных\rучастках для ведения садоводства']):
                liv_sp.append(item)
            for item in list((df2[0]['Введено,\r2тыс. м  общей площади жилых\rпомещений с учетом жилых домов,\rпостроенных на земельных\rучастках для ведения садоводства'])[:-1]):
                liv_sp.append(item)
        if page == ('266', '267'):
            for item in list(df1[0]['1) I квартал 2022 г.'])[3:]:
                if item != 'в том числе:' and type(item) == str:
                    turn_retail.append(item.split()[0])
            for item in list(df2[0]['1) I квартал 2022 г.'])[3:-1]:
                if item != 'в том числе:' and type(item) == str:
                    turn_retail.append(item.split()[-1])
        if page == ('270', '271'):
            for item in list(df1[0]['1) I квартал 2022 г.'])[3:]:
                if item != 'в том числе:' and type(item) == str:
                    turn_catering.append(item.split()[0])
            for item in list(df2[0]['1) I квартал 2022 г.'])[3:-1]:
                if item != 'в том числе:' and type(item) == str:
                    turn_catering.append(item.split()[-1])
        if page == ('272', '273'):
            for item in list(df1[0]['1) I квартал 2022 г.'])[3:]:
                if item != 'в том числе:' and type(item) == str:
                    turn_pservice.append(item.split()[0])
            for item in list(df2[0]['1) I квартал 2022 г.'])[3:-1]:
                if item != 'в том числе:' and type(item) == str:
                    turn_pservice.append(item.split()[-1])
        if page == ('284', '285'):
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
        if page == ('286', '287'):
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
        if page == ('288', '289'):
            for item in list((df1[0]['Первичный рынок'])[2:]):
                if item != 'в том числе:' and type(item) == str:
                    i = item.split()
                    pr_h_pi.append(i[1])
            for item in list((df1[0]['Вторичный рынок'])[2:]):
                if item != 'в том числе:' and type(item) == str:
                    i = item.split()
                    sec_h_pi.append(i[1])
            for item in list((df2[0]['Вторичный рынок'])[1:]):
                if item != 'в том числе:' and type(item) == str:
                    pr_h_pi.append(item)
            for item in list((df2[0]['Unnamed: 4'])[1:]):
                if item != 'в том числе:' and type(item) == str:
                    sec_h_pi.append(item)
            pr_h_pi.append('нет данных')
            sec_h_pi.append('нет данных')
        if page == ('300', '301'):
            for item in list((df1[0][4])[7:]):
                if item != 'в том числе:' and type(item) == str:
                    avg_mnth_wage.append(item)
            for item in list((df2[0]['Unnamed: 3'])[2:]):
                if item != 'в том числе:' and type(item) == str:
                    avg_mnth_wage.append(item)
        if page == ('302', '303'):
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
        if page == ('304', '305'):
            for item in list((df1[0]['Март\r2022 г.'])[1:]):
                if item != 'в том числе:' and type(item) == str:
                    unemploy_rate.append(item)
            for item in list((df2[0]['Март\r2022 г.'])[1:]):
                if item != 'в том числе:' and type(item) == str:
                    unemploy_rate.append(item)
    return liv_sp, turn_retail, turn_catering, turn_pservice, cpi_good_service, cpi_food_pr, \
           cpi_nonfood_pr, cpi_service, cost_fix_set_r, cost_fix_set_p, pr_h_pi, sec_h_pi, avg_mnth_wage, \
           nmb_labour_force, nmb_working, unemploy_rate
