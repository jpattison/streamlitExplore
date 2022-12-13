import pandas as pd
import numpy as np

from pyvis.network import Network
import networkx as nx
import streamlit as st
import streamlit.components.v1 as components

windowSize = 900

dfFaults = pd.read_csv("data/FaultsTracking.csv")
#print(dfFaults.head(10))

def traceProcesses(dfInput):
    dfGrouped = dfInput.groupby(["Origin", "Destination"]).agg(value=("Weight",np.sum), title=("Weight", np.sum))
    dfGrouped = dfGrouped.reset_index()
    return dfGrouped

def generateHtmlGraph(htmlPath, csvSource, height, width, isDirected=False):
    dfInput = pd.read_csv(csvSource)
    dfInputGrouped = traceProcesses(dfInput)
    # Create graph
    if isDirected:
        createUsing=nx.DiGraph()
    else:
        createUsing=nx.Graph()

    G = nx.from_pandas_edgelist(dfInputGrouped, 'Origin', 'Destination', ['title', 'value'], create_using=createUsing)

    height = f"{height}px"
    width = f"{width}px"
    nt = Network(height, width, bgcolor='#444444', font_color='white', select_menu=False, directed = isDirected)

    # Take Networkx graph and translate it to a PyVis graph format
    nt.from_nx(G)
    nt.write_html(htmlPath, local=False)
    #nt.show(htmlPath)



# Set header title
st.title('Upload your csv to generate a graph')
isDirectedStr = st.radio("Graph type", ('Not directed', 'Directed'))
isDirected = isDirectedStr == "Directed"
height = st.slider("Graph height", min_value=200, max_value=1500, value=600, step=50)
width = st.slider("Graph width", min_value=200, max_value=1500, value=900, step=50)

htmlPath = 'nx3.html'

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    generateHtmlGraph(htmlPath, uploaded_file, height, width, isDirected)
    HtmlFile = open(htmlPath,'r',encoding='utf-8')
    # Load HTML into HTML component for display on Streamlit
    components.html(HtmlFile.read(), height = height,width=width)
