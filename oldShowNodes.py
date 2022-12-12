"""
Goal: Visualise the karate kid

Goal One: Recreate the pyvis tutorial https://towardsdatascience.com/how-to-deploy-interactive-pyvis-network-graphs-on-streamlit-6c401d4c99db

Goal two: Update to visualise from a csv file

Goal three: Use the file uploader in streamlit to recreate

<Goal for today done>

Goal four: Ability to download colour schema/ edits.
"""


from pyvis.network import Network
import networkx as nx
# nx_graph = nx.cycle_graph(10)
# nx_graph.nodes[1]['title'] = 'Number 1'
# nx_graph.nodes[1]['group'] = 1
# nx_graph.nodes[3]['title'] = 'I belong to a different group!'
# nx_graph.nodes[3]['group'] = 10
# nx_graph.add_node(20, size=20, title='couple', group=2)
# nx_graph.add_node(21, size=15, title='couple', group=2)
# nx_graph.add_edge(20, 21, weight=5)
# nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)
# nt = Network('500px', '500px', select_menu=True)
# # populates the nodes and edges data structures
# nt.from_nx(nx_graph)
# nt.toggle_physics(True)
# nt.show_buttons(filter_=['physics'])
# nt.show('nx.html')

G = nx.karate_club_graph()

nt = Network('500px', '500px', select_menu=True)
# populates the nodes and edges data structures
nt.from_nx(G)
nt.toggle_physics(True)
nt.show_buttons(filter_=['physics'])
#nt.show('nx.html')
print(G)