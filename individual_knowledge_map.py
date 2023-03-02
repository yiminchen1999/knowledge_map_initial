from pyvis.network import Network
import pandas as pd
import networkx as nx
import webbrowser
import os
from IPython.core.display import display, HTML

week_keyword = pd.read_excel("week_keyword_table_s01_2021.xlsx", index_col=0, engine='openpyxl')
keyword_category = pd.read_excel("keyword_category_table.xlsx", index_col=0, engine='openpyxl')
print(week_keyword)
print(keyword_category)
keywords = list(week_keyword.head())
print(keywords)
# the number shows which category the keyword belongs to
keywords_group = keyword_category.iloc[:, 0].to_numpy()
#print(keywords_group)
# extract each week's keyword list
week1 = week_keyword.iloc[0].to_numpy()
week2 = week_keyword.iloc[1].to_numpy()
week3 = week_keyword.iloc[2].to_numpy()
#print(week1)
#print(week2)
#print(week3)
# create gradient color for each week's nodes
from palettable.colorbrewer.sequential import Blues_3
palette = Blues_3.hex_colors
#print(palette)
palette[0]
#net1 = Network(notebook=True, heading="Individual Knowledge Map Week 1", cdn_resources='remote')
#initialize code
net1 = Network(notebook=False, heading="Individual Knowledge Map Week 1" )
#name for html
title =[]
html_name='index.html'
notebook=False
# cacluates the number of occurences for each keywork for week 1
occurence_week1 = week_keyword.iloc[:1].sum()
for i, value in enumerate(week1):
    if value == 1:
        net1.add_node(i, label=keywords[i], title='Week1', size=(int(occurence_week1[i]) + 1) * 3, color=palette[0])
# show the all node ids we have in the net
net1_id = [dic['id'] for dic in net1.nodes]
#print(net1_id)
for i in net1_id:
    for j in net1_id:
        if i != j and keywords_group[i] == keywords_group[j]:
            net1.add_edge(i, j)
#net1.show("social_network.html")
net1.show_buttons(filter_="physics")
net1.show('index.html')

#open the result in webbrowser
try:
    from urllib import pathname2url
except:
    from urllib.request import pathname2url

url = 'file:{}'.format(pathname2url(os.path.abspath(html_name)))
webbrowser.open(url)
#def show_graph(name):
    #net1.show(name)
    #display(HTML(name))

#show_graph('index.html')

net2 = Network(notebook=False, heading="Individual Knowledge Map Week 2" )
#name for html
title =[]
html_name='index2.html'
#net2 = Network(notebook=True, heading="Individual Knowledge Map Week 2", filter_menu=True, cdn_resources='remote')
# cacluates the number of occurences for each keywork for week 1 & week2 in total
occurence_week2 = week_keyword.iloc[:2].sum()
for i, value in enumerate(week1):
    if value == 1:
        net2.add_node(i, label=keywords[i], title='Week1', size=(int(occurence_week2[i]) + 1) * 3, color=palette[0])
for i, value in enumerate(week2):
    if value == 1:
        net2.add_node(i, label=keywords[i], title='Week2', size=(int(occurence_week2[i]) + 1) * 3, color=palette[1])
# show the all node ids we have in the net
net2_id = [dic['id'] for dic in net2.nodes]
print(net2_id)
for i in net2_id:
    for j in net2_id:
        if i != j and keywords_group[i] == keywords_group[j]:
            net2.add_edge(i, j)
#net2.show("social_network.html")
#net2.show_buttons(filter_="physics")
net2.show_buttons(filter_=['physics'])
net2.show('index2.html')
#open the result in webbrowser
try:
    from urllib import pathname2url
except:
    from urllib.request import pathname2url

url = 'file:{}'.format(pathname2url(os.path.abspath(html_name)))
webbrowser.open(url)


net3 = Network(notebook=False, heading="Individual Knowledge Map Week 3" )
title =[]
html_name='index3.html'
#net3 = Network(notebook=True, heading="Individual Knowledge Map Week 3", filter_menu=True, cdn_resources='remote')
# cacluates the number of occurences for each keywork for week 1 & week2 & week3 in total
occurence_week3 = week_keyword.iloc[:2].sum()
for i, value in enumerate(week1):
    if value == 1:
        net3.add_node(i, label=keywords[i], title='Week1', size=(int(occurence_week3[i]) + 1) * 3, color=palette[0])
for i, value in enumerate(week2):
    if value == 1:
        net3.add_node(i, label=keywords[i], title='Week2', size=(int(occurence_week3[i]) + 1) * 3, color=palette[1])
for i, value in enumerate(week3):
    if value == 1:
        net3.add_node(i, label=keywords[i], title='Week3', size=(int(occurence_week3[i]) + 1) * 3, color=palette[2])
# show the all node ids we have in the net
net3_id = [dic['id'] for dic in net3.nodes]
print(net3_id)
for i in net3_id:
    for j in net3_id:
        if i != j and keywords_group[i] == keywords_group[j]:
            net3.add_edge(i, j)
#net3.show("social_network.html")
net3.show_buttons(filter_="physics")
net3.show('index3.html')

#open the result in webbrowser
try:
    from urllib import pathname2url
except:
    from urllib.request import pathname2url

url = 'file:{}'.format(pathname2url(os.path.abspath(html_name)))
webbrowser.open(url)
