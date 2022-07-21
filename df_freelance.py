import pandas as pd
from xd.df_sbj_jan import return_june
from xd.df_sbj_feb import return_feb
from xd.df_sbj_mar import return_mar
from xd.df_last import return_last
# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)

# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)
reader_df_cr_jan = pd.ExcelFile('../df_cr_1.xlsx')
reader_df_cr_feb = pd.ExcelFile('../df_cr_2.xlsx')
reader_df_cr_mar = pd.ExcelFile('../df_cr_3.xlsx')
df_cr_jan = pd.DataFrame(reader_df_cr_jan.parse(header=0))
df_cr_feb = pd.DataFrame(reader_df_cr_feb.parse(header=0))
df_cr_mar = pd.DataFrame(reader_df_cr_mar.parse(header=0))
df_cr_1 = pd.DataFrame({'sbj': df_cr_jan['Информация о кредитах, предоставленных '
                                            'физическим лицам - резидентам, млн руб.'][4:],
                        'yy_mm': df_cr_jan['Unnamed: 1'][0],
                        'loan_iss': df_cr_jan['Unnamed: 1'][4:],
                        'loan_debt': df_cr_jan['Unnamed: 4'][4:],
                        'loan_overd': df_cr_jan['Unnamed: 7'][4:]})
df_cr_2 = pd.DataFrame({'sbj': df_cr_feb['Информация о кредитах, предоставленных '
                                            'физическим лицам - резидентам, млн руб.'][4:],
                        'yy_mm': df_cr_feb['Unnamed: 1'][0],
                        'loan_iss': df_cr_feb['Unnamed: 1'][4:],
                        'loan_debt': df_cr_feb['Unnamed: 4'][4:],
                        'loan_overd': df_cr_feb['Unnamed: 7'][4:]})
df_cr_3 = pd.DataFrame({'sbj': df_cr_mar['Информация о кредитах, предоставленных '
                                            'физическим лицам - резидентам, млн руб.'][4:],
                        'yy_mm': df_cr_mar['Unnamed: 1'][0],
                        'loan_iss': df_cr_mar['Unnamed: 1'][4:],
                        'loan_debt': df_cr_mar['Unnamed: 4'][4:],
                        'loan_overd': df_cr_mar['Unnamed: 7'][4:]})
df_cr = pd.concat([df_cr_1, df_cr_2, df_cr_3], ignore_index=True)
print(df_cr)

reader_df_dep = pd.ExcelFile('../df_dep_1.xlsx')
df_dep_pre = pd.DataFrame(reader_df_dep.parse(header=1))
df_dep = pd.DataFrame({})
for i in ['01.02.2022', '01.03.2022', '01.04.2022']:
    df_dep = pd.concat([df_dep, pd.DataFrame({
        'sbj': df_dep_pre['Unnamed: 0'][0:96],
        'yy_mm': i,
        'dep': df_dep_pre[i][0:96]
    })], ignore_index=True)
print(df_dep)

reader_df_org_jan = pd.ExcelFile('../df_org_1.xlsx')
reader_df_org_feb = pd.ExcelFile('../df_org_2.xlsx')
reader_df_org_mar = pd.ExcelFile('../df_org_3.xlsx')
df_org_jan = pd.DataFrame(reader_df_org_jan.parse(header=0))
df_org_feb = pd.DataFrame(reader_df_org_feb.parse(header=0))
df_org_mar = pd.DataFrame(reader_df_org_mar.parse(header=0))
df_org_1 = pd.DataFrame({'sbj': df_org_jan['Статистика территориального присутствия действующих '
                                           'кредитных организаций и их подразделений по состоянию на 01.02.2022'][2:98],
                        'yy_mm': '01.02.2022',
                        'head_office': df_org_jan['Unnamed: 1'][2:98],
                        'branch': df_org_jan['Unnamed: 2'][2:98],
                        'rep_office': df_org_jan['Unnamed: 3'][2:98],
                        'add_office': df_org_jan['Unnamed: 4'][2:98],
                        'oper_cash': df_org_jan['Unnamed: 5'][2:98],
                        'cred_cash': df_org_jan['Unnamed: 6'][2:98],
                        'oper_office': df_org_jan['Unnamed: 7'][2:98],
                        'mob_p': df_org_jan['Unnamed: 8'][2:98],
                         })
df_org_2 = pd.DataFrame({'sbj': df_org_feb['Статистика территориального присутствия действующих '
                                           'кредитных организаций и их подразделений по состоянию на 01.03.2022'][2:98],
                        'yy_mm': '01.03.2022',
                        'head_office': df_org_feb['Unnamed: 1'][2:98],
                        'branch': df_org_feb['Unnamed: 2'][2:98],
                        'rep_office': df_org_feb['Unnamed: 3'][2:98],
                        'add_office': df_org_feb['Unnamed: 4'][2:98],
                        'oper_cash': df_org_feb['Unnamed: 5'][2:98],
                        'cred_cash': df_org_feb['Unnamed: 6'][2:98],
                        'oper_office': df_org_feb['Unnamed: 7'][2:98],
                        'mob_p': df_org_feb['Unnamed: 8'][2:98],
                         })
df_org_3 = pd.DataFrame({'sbj': df_org_mar['Статистика территориального присутствия действующих '
                                           'кредитных организаций и их подразделений по состоянию на 01.04.2022'][2:98],
                        'yy_mm': '01.04.2022',
                        'head_office': df_org_mar['Unnamed: 1'][2:98],
                        'branch': df_org_mar['Unnamed: 2'][2:98],
                        'rep_office': df_org_mar['Unnamed: 3'][2:98],
                        'add_office': df_org_mar['Unnamed: 4'][2:98],
                        'oper_cash': df_org_mar['Unnamed: 5'][2:98],
                        'cred_cash': 'нет данных',
                        'oper_office': 'нет данных',
                        'mob_p': 'нет данных'
                         })
df_org = pd.concat([df_org_1, df_org_2, df_org_3], ignore_index=True)
print(df_org)
lst_names = list(df_cr_jan['Информация о кредитах, предоставленных '
                                            'физическим лицам - резидентам, млн руб.'][4:-1])
lst_names.insert(26, 'Архангельская область без авт. округа')
liv_sp, turn_retail, turn_catering, turn_pservice, cpi_good_service, cpi_food_pr, \
           cpi_nonfood_pr, cpi_service, cost_fix_set_r, cost_fix_set_p, nmb_labour_force, nmb_working, unemploy_rate = return_june()
liv_sp1, turn_retail1, turn_catering1, turn_pservice1, cpi_good_service1, cpi_food_pr1, \
           cpi_nonfood_pr1, cpi_service1, cost_fix_set_r1, cost_fix_set_p1, avg_mnth_wage1, nmb_labour_force1, nmb_working1, unemploy_rate1 = return_feb()
liv_sp2, turn_retail2, turn_catering2, turn_pservice2, cpi_good_service2, cpi_food_pr2, \
           cpi_nonfood_pr2, cpi_service2, cost_fix_set_r2, cost_fix_set_p2, pr_h_pi, sec_h_pi, avg_mnth_wage2, \
           nmb_labour_force2, nmb_working2, unemploy_rate2 = return_mar()
avg_mnth_income, avg_mnth_cost, grp, jan_avg_pension, feb_avg_pension, mar_avg_pension = return_last()

df_sbj1 = pd.DataFrame({
    'sbj': lst_names,
    'yy_mm': 'янв',
    'liv_sp': liv_sp,
    'turn_retail': turn_retail,
    'turn_catering': turn_catering,
    'turn_pservice': turn_pservice,
    'cpi_good_service': cpi_good_service,
    'cpi_food_pr': cpi_food_pr,
    'cpi_nonfood_pr': cpi_nonfood_pr,
    'cpi_service': cpi_service,
    'cost_fix_set_r': cost_fix_set_r,
    'cost_fix_set_p': cost_fix_set_p,
    'pr_h_pi': pr_h_pi,
    'sec_h_pi': sec_h_pi,
    'avg_mnth_wage': avg_mnth_wage1,
    'nmb_labour_force': nmb_labour_force,
    'nmb_working': nmb_working,
    'unemploy_rate': unemploy_rate,
    'avg_mnth_income': avg_mnth_income,
    'avg_mnth_cost': avg_mnth_cost,
    'grp': grp,
    'avg_pension': jan_avg_pension
})
df_sbj2 = pd.DataFrame({
    'sbj': lst_names,
    'yy_mm': 'фев',
    'liv_sp': liv_sp1,
    'turn_retail': turn_retail1,
    'turn_catering': turn_catering1,
    'turn_pservice': turn_pservice1,
    'cpi_good_service': cpi_good_service1,
    'cpi_food_pr': cpi_food_pr1,
    'cpi_nonfood_pr': cpi_nonfood_pr1,
    'cpi_service': cpi_service1,
    'cost_fix_set_r': cost_fix_set_r1,
    'cost_fix_set_p': cost_fix_set_p1,
    'pr_h_pi': pr_h_pi,
    'sec_h_pi': sec_h_pi,
    'avg_mnth_wage': avg_mnth_wage2,
    'nmb_labour_force': nmb_labour_force1,
    'nmb_working': nmb_working1,
    'unemploy_rate': unemploy_rate1,
    'avg_mnth_income': avg_mnth_income,
    'avg_mnth_cost': avg_mnth_cost,
    'grp': grp,
    'avg_pension': feb_avg_pension
})

df_sbj3 = pd.DataFrame({
    'sbj': lst_names,
    'yy_mm': 'мар',
    'liv_sp': liv_sp2,
    'turn_retail': turn_retail2,
    'turn_catering': turn_catering2,
    'turn_pservice': turn_pservice2,
    'cpi_good_service': cpi_good_service2,
    'cpi_food_pr': cpi_food_pr2,
    'cpi_nonfood_pr': cpi_nonfood_pr2,
    'cpi_service': cpi_service2,
    'cost_fix_set_r': cost_fix_set_r2,
    'cost_fix_set_p': cost_fix_set_p2,
    'pr_h_pi': pr_h_pi,
    'sec_h_pi': sec_h_pi,
    'avg_mnth_wage': '-',
    'nmb_labour_force': nmb_labour_force2,
    'nmb_working': nmb_working2,
    'unemploy_rate': unemploy_rate2,
    'avg_mnth_income': avg_mnth_income,
    'avg_mnth_cost': avg_mnth_cost,
    'grp': grp,
    'avg_pension': mar_avg_pension
})
df_sbj = pd.concat([df_sbj1, df_sbj2, df_sbj3], ignore_index=True)
print(df_sbj)
