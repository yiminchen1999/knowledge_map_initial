import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import got 
#Network(notebook=True)
st.title('Hello Pyvis')
# make Network show itself with repr_html

#def net_repr_html(self):
#  nodes, edges, height, width, options = self.get_network_data()
#  html = self.template.render(height=height, width=width, nodes=nodes, edges=edges, options=options)
#  return html

#Network._repr_html_ = net_repr_html
st.sidebar.title('Choose your week')
option=st.sidebar.selectbox('select graph',('week1','week2', 'week3'))
physics=st.sidebar.checkbox('add physics interactivity?')
got.simple_func(physics)

if option=='week1':
  HtmlFile = open("index.html", 'r', encoding='utf-8')
  source_code = HtmlFile.read() 
  components.html(source_code, height = 900,width=900)


got.got_func(physics)

if option=='week2':
  HtmlFile = open("index2.html", 'r', encoding='utf-8')
  source_code = HtmlFile.read() 
  components.html(source_code, height = 1200,width=1000)



got.karate_func(physics)

if option=='week3':
  HtmlFile = open("index3.html", 'r', encoding='utf-8')
  source_code = HtmlFile.read() 
  components.html(source_code, height = 1200,width=1000)
