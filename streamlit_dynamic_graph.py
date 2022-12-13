import pandas as pd
import numpy as np

from pyvis.network import Network
import networkx as nx
import streamlit as st
import streamlit.components.v1 as components

isDirected = True
windowSize = 900

dfFaults = pd.read_csv("data/FaultsTracking.csv")
#print(dfFaults.head(10))

def traceProcesses(dfInput):
    dfGrouped = dfInput.groupby(["Origin", "Destination"]).agg(value=("Weight",np.sum), title=("Weight", np.sum))
    dfGrouped = dfGrouped.reset_index()
    return dfGrouped

def generateHtmlGraph(htmlPath, csvSource, windowSize, isDirected=False):
    dfInput = pd.read_csv(csvSource)
    dfInputGrouped = traceProcesses(dfInput)
    # Create graph
    if isDirected:
        createUsing=nx.DiGraph()
    else:
        createUsing=nx.Graph()

    G = nx.from_pandas_edgelist(dfInputGrouped, 'Origin', 'Destination', ['title', 'value'], create_using=createUsing)

    windowSize = f"{windowSize}px"
    nt = Network(windowSize, windowSize, bgcolor='#444444', font_color='white', select_menu=False, directed = isDirected)

    # Take Networkx graph and translate it to a PyVis graph format
    nt.from_nx(G)
    nt.write_html(htmlPath, local=False)
    #nt.show(htmlPath)



# Set header title
st.title('Generate graph')
htmlPath = 'nx3.html'

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    generateHtmlGraph(htmlPath, uploaded_file, windowSize, isDirected)
    HtmlFile = open(htmlPath,'r',encoding='utf-8')
    # Load HTML into HTML component for display on Streamlit
    components.html(HtmlFile.read(), height = windowSize,width=windowSize)
