from network import HypercubeNetwork

network = HypercubeNetwork()

network.store_data("message1", "secret message")

retrieved_data = network.retrieve_data("message1")
print(f"Retrieved Data: {retrieved_data}")