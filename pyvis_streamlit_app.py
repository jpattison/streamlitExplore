"""

Goal One: Recreate the pyvis tutorial https://towardsdatascience.com/how-to-deploy-interactive-pyvis-network-graphs-on-streamlit-6c401d4c99db

Goal two: Update to visualise from a csv file

Goal three: Use the file uploader in streamlit to recreate

<Goal for today done>

Goal four: Ability to download colour schema/ edits.
"""


# Import dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network




# Read dataset
df_interact = pd.read_csv('data/processed_drug_interactions.csv')

#print(df_interact.head(20))

# Set header title
st.title('Network Graph Visualization of Drug-Drug Interactions')

# Define selection options and sort alphabetically
drug_list = ['Metformin', 'Glipizide', 'Lisinopril', 'Simvastatin',
            'Warfarin', 'Aspirin', 'Losartan', 'Ibuprofen']
drug_list.sort()
# Implement multiselect dropdown menu for option selection
selected_drugs = st.multiselect('Select drug(s) to visualize', drug_list)

# Set info message on initial site load
if len(selected_drugs) == 0:
   st.text('Please choose at least 1 drug to get started')
# Create network graph when user selects >= 1 item
else:
   # Code for filtering dataframe and generating network
    print("drug selected")
	df_select = df_interact.loc[df_interact['drug_1_name'].isin(selected_drugs) | \
		df_interact['drug_2_name'].isin(selected_drugs)]
	df_select = df_select.reset_index(drop=True)

	# Create networkx graph object from pandas dataframe
	G = nx.from_pandas_edgelist(df_select, 'drug_1_name', 'drug_2_name', 'weight')

	# Initiate PyVis network object
	drug_net = Network(height='465px', bgcolor='#222222', font_color='white')

	# Take Networkx graph and translate it to a PyVis graph format
	drug_net.from_nx(G)

	# Generate network with specific layout settings
	drug_net.repulsion(node_distance=420, central_gravity=0.33,
		spring_length=110, spring_strength=0.10,
		damping=0.95)


	#Create visualisation locally
	path = 'html_files'

	# Create visualisation on streamlit sharing
	path = '/tmp'

	drug_net.save_graph(f'{path}/pyvis_graph.html')
	HtmlFile = open(f'{path}/pyvis_graph.html','r',encoding='utf-8')

	# Load HTML into HTML component for display on Streamlit
	components.html(HtmlFile.read())
	st.text('Loaded')

