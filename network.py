from node import Node

class HypercubeNetwork:
    def __init__(self, dimension=4):
        self.dimension = dimension
        self.nodes = []
        self.create_hypercube()

    def create_hypercube(self):
        num_nodes = 2 ** self.dimension
        for i in range(num_nodes):
            node = Node(bin(i)[2:].zfill(self.dimension))
            self.nodes.append(node)
        
        for node in self.nodes:
            for j in range(self.dimension):
                neighbor_id = list(node.id)
                neighbor_id[j] = '1' if neighbor_id[j] == '0' else '0'
                neighbor_id = ''.join(neighbor_id)
                neighbor_node = self.get_node_by_id(neighbor_id)
                node.connect(neighbor_node)

    def store_data(self, key, data):
        key_id = hash(key) % len(self.nodes)
        print(key_id)
        key_node = self.get_node_by_id(bin(key_id)[2:].zfill(self.dimension))
        key_node.data[key] = data
        print(f"Data stored at node {key_node.id}")
    
    def retrieve_data(self, key):
        key_id = hash(key) % len(self.nodes)
        key_node = self.get_node_by_id(bin(key_id)[2:].zfill(self.dimension))
        if key in key_node.data:
            print(f"Data retrieved from node {key_node.id}")
            return key_node.data[key]
        else:
            return "Data not found"
        
    def route_message(self, start_id, end_id):
        start_node = self.get_node_by_id(start_id)
        end_node = self.get_node_by_id(end_id)
        path = start_node.route_message(end_node, self)
        print(f"Message routed through: {path}")
        return path

    def get_node_by_id(self, id):
        for node in self.nodes:
            if node.id == id:
                return node
        return None