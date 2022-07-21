import os
import pandas as pd
from tabula.io import read_pdf
# Сброс ограничений на количество выводимых рядов
def return_last():
    # pd.set_option('display.max_rows', None)
    #
    # # Сброс ограничений на число столбцов
    # pd.set_option('display.max_columns', None)
    #
    # # Сброс ограничений на количество символов в записи
    # pd.set_option('display.max_colwidth', None)
    avg_mnth_income = []
    avg_mnth_cost = []
    grp = []
    file_path = r'../Region_Pokaz_2021.pdf'
    pr = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    df1 = read_pdf(file_path, pages=['19', '21', '23'], multiple_tables=False)
    for item in list((df1[0]['Средне-.1'])[14:]):
        if type(item) == str:
            if item.startswith(pr):
                avg_mnth_income.append(item)
    for item in list((df1[0]['Потреби-'])[14:]):
        if type(item) == str:
            if item.startswith(pr) and not item.endswith(','):
                avg_mnth_cost.append(item)
    for item in list((df1[0]['Валовой'])[14:]):
        if type(item) == str:
            if item.startswith(pr) and not item.endswith(','):
                grp.append(item)

    reader_df_data = pd.ExcelFile('../data.xls')
    df_data = pd.DataFrame(reader_df_data.parse(header=0))
    jan_avg_pension = df_data['Unnamed: 7'][3:99]
    feb_avg_pension = df_data['Unnamed: 8'][3:99]
    mar_avg_pension = df_data['Unnamed: 9'][3:99]

    return avg_mnth_income, avg_mnth_cost, grp, jan_avg_pension, feb_avg_pension, mar_avg_pension
