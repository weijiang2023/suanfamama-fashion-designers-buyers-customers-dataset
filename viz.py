import networkx as nx
import matplotlib.pyplot as plt
import csv

def read_csv_relationships(filename):
    relationships = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            source = row[0]
            targets = row[1:]
            for target in targets:
                relationships.append((source, target))
    return relationships

def visualize_relationships():
    # Read relationships from CSV files
    customer_to_buyers = read_csv_relationships('customer_to_buyers.csv')
    buyer_to_designers = read_csv_relationships('buyer_to_designers.csv')
    designer_to_buyers = read_csv_relationships('designer_to_buyers.csv')

    # Create a graph
    G = nx.DiGraph()

    # Add edges to the graph
    G.add_edges_from(customer_to_buyers, relationship='Customer-Buyer')
    G.add_edges_from(buyer_to_designers, relationship='Buyer-Designer')
    G.add_edges_from(designer_to_buyers, relationship='Designer-Buyer')

    # Draw the graph
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(G, k=0.5, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')

    # Add a legend
    edge_labels = nx.get_edge_attributes(G, 'relationship')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title('Relationships Between Customers, Buyers, and Designers')
    plt.show()

if __name__ == '__main__':
    visualize_relationships()