import pandas as pd
import numpy as np

from pyvis.network import Network
import networkx as nx
import streamlit as st
import streamlit.components.v1 as components

isDirected = False

dfFaults = pd.read_csv("data/FaultsTracking.csv")
#print(dfFaults.head(10))

def traceProcesses(dfInput):
    dfGrouped = dfInput.groupby(["Origin", "Destination"]).agg(value=("Weight",np.sum), title=("Weight", np.sum))
    dfGrouped = dfGrouped.reset_index()
    return dfGrouped

def generateHtmlGraph(csvSource, htmlPath, isDirected=False):
    
    dfInput = pd.read_csv(csvSource)

    dfInputGrouped = traceProcesses(dfInput)

    #print(dfInputGrouped.head(10))


    # Create graph
    if isDirected:
        createUsing=nx.DiGraph()
    else:
        createUsing=nx.Graph()


    G = nx.from_pandas_edgelist(dfInputGrouped, 'Origin', 'Destination', ['title', 'value'], create_using=createUsing)

    nt = Network('500px', '500px', bgcolor='#222222', font_color='white', select_menu=True, directed = isDirected)
    # Take Networkx graph and translate it to a PyVis graph format
    nt.from_nx(G)

    #nt.show_buttons(filter_=['generate options'])
    #nt.show_buttons(filter_=True)
    nt.save_graph(htmlPath)

#generateHtmlGraph("data/FaultsTracking.csv")
#generateHtmlGraph("data/FaultsTrackingTwo.csv")

htmlPath = '/tmp/nx.html'

# Set header title
st.title('Generate graph')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    
    generateHtmlGraph(uploaded_file, htmlPath)
    #generateHtmlGraph("data/FaultsTracking.csv", htmlPath)

    # Create visualisation on streamlit sharing
    

    HtmlFile = open(htmlPath,'r',encoding='utf-8')

    # Load HTML into HTML component for display on Streamlit
    components.html(HtmlFile.read(), height=500)