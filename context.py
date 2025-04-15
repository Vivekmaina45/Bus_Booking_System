import matplotlib.pyplot as plt
import networkx as nx

def draw_context_diagram():
    G = nx.DiGraph()
    
    # Nodes
    G.add_node("Customer", shape='ellipse')
    G.add_node("Supermarket System", shape='rectangle')
    G.add_node("Supermarket Staff", shape='ellipse')
    G.add_node("Supermarket Manager", shape='ellipse')
    
    # Edges (Interactions)
    G.add_edge("Customer", "Supermarket System", label="Register / Purchase")
    G.add_edge("Supermarket System", "Supermarket Staff", label="Process Transactions")
    G.add_edge("Supermarket System", "Supermarket Manager", label="Generate Reports")
    G.add_edge("Supermarket Manager", "Supermarket System", label="Award Gifts")
    
    # Draw Graph
    plt.figure(figsize=(8, 5))
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', edge_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Context Diagram")
    plt.show()

def draw_overview_diagram():
    G = nx.DiGraph()
    
    # Nodes
    G.add_node("Customer", shape='ellipse')
    G.add_node("Supermarket System", shape='rectangle')
    G.add_node("Register Customer", shape='rectangle')
    G.add_node("Process Purchase", shape='rectangle')
    G.add_node("Identify Top Customers", shape='rectangle')
    G.add_node("Award Gifts", shape='rectangle')
    G.add_node("Supermarket Manager", shape='ellipse')
    
    # Edges (Processes)
    G.add_edge("Customer", "Register Customer", label="Provide Details")
    G.add_edge("Register Customer", "Supermarket System", label="Assign CN")
    G.add_edge("Customer", "Process Purchase", label="Provide CN + Purchase")
    G.add_edge("Process Purchase", "Supermarket System", label="Update Purchase File")
    G.add_edge("Supermarket System", "Identify Top Customers", label="Analyze Purchases")
    G.add_edge("Identify Top Customers", "Award Gifts", label="Generate List")
    G.add_edge("Award Gifts", "Supermarket Manager", label="Distribute Gifts")
    
    # Draw Graph
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightgreen', edge_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Overview Diagram (Level 0 DFD)")
    plt.show()

# Draw both diagrams
draw_context_diagram()
draw_overview_diagram()