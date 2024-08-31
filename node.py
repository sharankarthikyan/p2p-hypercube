class Node:
    def __init__(self, id):
        self.id = id
        self.data = {}
        self.neighbors = []

    def connect(self, node):
        if node not in self.neighbors:
            self.neighbors.append(node)
            node.neighbors.append(self)
            
    def route_message(self, target_node, network):
        current_node = self
        path = [current_node.id]
        while current_node.id != target_node.id:
            for i in range(len(current_node.id)):
                if current_node.id[i] != target_node.id[i]:
                    next_hop_id = list(current_node.id)
                    next_hop_id[i] = target_node.id[i]
                    next_hop_id = ''.join(next_hop_id)
                    current_node = network.get_node_by_id(next_hop_id)
                    path.append(current_node.id)
                    break
        return path