# -*- coding: utf-8 -*-
"""Real_Individual_Knowledge_Map_Weekly_1.0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v1KuS0b5oB72rHsvCNGFMWw3dSlEo_kj
"""

import pandas as pd
from pyvis.network import Network

keyword_category = pd.read_excel("assets/dictionary 2.0.xlsx",index_col=0).iloc[:,0:1]

print(keyword_category)

# read student files

file_names_2021 = ['Y2021_Student01','Y2021_Student02','Y2021_Student03','Y2021_Student04','Y2021_Student05','Y2021_Student06','Y2021_Student07']
year2021_df = []
for i in range(len(file_names_2021)):
    temp_df = pd.read_csv("assets/Year2021/"+file_names_2021[i]+".csv",index_col=0)
    year2021_df.append(temp_df)

file_names_2022 = ['Y2022_Student01','Y2022_Student02','Y2022_Student03','Y2022_Student04','Y2022_Student05','Y2022_Student06','Y2022_Student07','Y2022_Student08','Y2022_Student09','Y2022_Student10','Y2022_Student11','Y2022_Student12']
year2022_df = []
for i in range(len(file_names_2022)):
    temp_df = pd.read_csv("assets/Year2022/"+file_names_2022[i]+".csv",index_col=0)
    year2022_df.append(temp_df)

file_names_2023 = ['Y2023_Student01','Y2023_Student02','Y2023_Student03','Y2023_Student04','Y2023_Student05','Y2023_Student06','Y2023_Student07','Y2023_Student08','Y2023_Student09','Y2023_Student10','Y2023_Student11','Y2023_Student12']
year2023_df = []
for i in range(len(file_names_2023)):
    temp_df = pd.read_csv("assets/Year2023/"+file_names_2023[i]+".csv",index_col=0)
    year2023_df.append(temp_df)

keywords = list(year2021_df[0].head())
print(keywords)

# the number shows which category the keyword belongs to
keywords_group = keyword_category.iloc[:, 0].to_numpy()
print(keywords_group)

# create color for each category
category_color = []
for i in keywords_group:
    if i == 1:
        category_color.append('#e3342f')
    if i == 2:
        category_color.append('#f6993f')
    if i == 3:
        category_color.append('#ffed4a')
    if i == 4:
        category_color.append('#38c172')
    if i == 5:
        category_color.append('#4dc0b5')
    if i == 6:
        category_color.append('#3490dc')
    if i == 7:
        category_color.append('#6574cd')
    if i == 8:
        category_color.append('#9561e2')
    if i == 9:
        category_color.append('#f66d9b')

# create a function that produces weekly individual knowledge map for each student
def weekly_individual_knowledge_map(student_df):
    # extract each week's keyword list
    week_list = []
    for i in range(student_df.shape[0]):
        week_list.append(student_df.iloc[i].to_numpy())

    nets = []
    for i in range(student_df.shape[0]):
        net = Network(notebook=True)#, heading="Individual Knowledge Map Weekly " + str((i + 1)))
        for j, value in enumerate(week_list[i]):
            if value == 1:
                net.add_node(j, label=keywords[j], size=6, title='Week'+str(i+1),color=category_color[j])
                
        net_id = [dic['id'] for dic in net.nodes]

        for n in net_id:
            for j in net_id:
                if n != j and keywords_group[n] == keywords_group[j]:
                    net.add_edge(n,j)
        net.repulsion(central_gravity=1,spring_length=30)
        nets.append(net)
    
    return nets

indi_weekly_s1_2021 = weekly_individual_knowledge_map(year2021_df[0])
indi_weekly_s2_2021 = weekly_individual_knowledge_map(year2021_df[1])
indi_weekly_s3_2021 = weekly_individual_knowledge_map(year2021_df[2])
indi_weekly_s4_2021 = weekly_individual_knowledge_map(year2021_df[3])
indi_weekly_s5_2021 = weekly_individual_knowledge_map(year2021_df[4])
indi_weekly_s6_2021 = weekly_individual_knowledge_map(year2021_df[5])
indi_weekly_s7_2021 = weekly_individual_knowledge_map(year2021_df[6])

indi_weekly_s1_2022 = weekly_individual_knowledge_map(year2022_df[0])
indi_weekly_s2_2022 = weekly_individual_knowledge_map(year2022_df[1])
indi_weekly_s3_2022 = weekly_individual_knowledge_map(year2022_df[2])
indi_weekly_s4_2022 = weekly_individual_knowledge_map(year2022_df[3])
indi_weekly_s5_2022 = weekly_individual_knowledge_map(year2022_df[4])
indi_weekly_s6_2022 = weekly_individual_knowledge_map(year2022_df[5])
indi_weekly_s7_2022 = weekly_individual_knowledge_map(year2022_df[6])
indi_weekly_s8_2022 = weekly_individual_knowledge_map(year2022_df[7])
indi_weekly_s9_2022 = weekly_individual_knowledge_map(year2022_df[8])
indi_weekly_s10_2022 = weekly_individual_knowledge_map(year2022_df[9])
indi_weekly_s11_2022 = weekly_individual_knowledge_map(year2022_df[10])
indi_weekly_s12_2022 = weekly_individual_knowledge_map(year2022_df[11])

indi_weekly_s1_2023 = weekly_individual_knowledge_map(year2023_df[0])
indi_weekly_s2_2023 = weekly_individual_knowledge_map(year2023_df[1])
indi_weekly_s3_2023 = weekly_individual_knowledge_map(year2023_df[2])
indi_weekly_s4_2023 = weekly_individual_knowledge_map(year2023_df[3])
indi_weekly_s5_2023 = weekly_individual_knowledge_map(year2023_df[4])
indi_weekly_s6_2023 = weekly_individual_knowledge_map(year2023_df[5])
indi_weekly_s7_2023 = weekly_individual_knowledge_map(year2023_df[6])
indi_weekly_s8_2023 = weekly_individual_knowledge_map(year2023_df[7])
indi_weekly_s9_2023 = weekly_individual_knowledge_map(year2023_df[8])
indi_weekly_s10_2023 = weekly_individual_knowledge_map(year2023_df[9])
indi_weekly_s11_2023 = weekly_individual_knowledge_map(year2023_df[10])
indi_weekly_s12_2023 = weekly_individual_knowledge_map(year2023_df[11])

indi_weekly_s12_2023[0].show('assets/2023_s12_weekly_1.html')

indi_weekly_s12_2023[1].show('assets/2023_s12_weekly_2.html')

indi_weekly_s12_2023[2].show('assets/2023_s12_weekly_3.html')

indi_weekly_s12_2023[3].show('assets/2023_s12_weekly_4.html')

indi_weekly_s12_2023[4].show('assets/2023_s12_weekly_5.html')

years = [2021, 2022, 2023]
for year in years:
    year_df = f"year{year}_df"
    palette = f"palette_{year}"
    if year == 2021:
        for week in range(1, 9):
            week_df = year_df[week - 1]
            indi_weekly = weekly_individual_knowledge_map(week_df, palette)
            for j in range(1,8):
            indi_weekly[j].show(f"assets/{year}_s{j}_weekly_{week}.html")
    elif year == 2022:
        for week in range(1, 11):
            week_df = year_df[week - 1]
            indi_weekly = weekly_individual_knowledge_map(week_df, palette)
            for j in range(1, 13):
                indi_weekly[j].show(f"assets/{year}_s{j}_weekly_{week}.html")
    elif year == 2023:
        for week in range(1, 6):
            week_df = year_df[week - 1]
            indi_weekly = weekly_individual_knowledge_map(week_df, palette)
            for j in range(1, 13):
                indi_weekly[j].show(f"assets/{year}_s{j}_weekly_{week}.html")



