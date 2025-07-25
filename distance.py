from load_package import load_addresses, load_distances

address_list = load_addresses('data/Address_File.csv')
distance_list = load_distances('data/Distance_File.csv')

# function to return the index number
def get_address_index(address):
    for row in address_list:
        if address in row[1]:
            return address_list.index(row)
    return None

def get_distance(addr1, addr2):
    if get_address_index(addr1) < get_address_index(addr2):
        return distance_list[get_address_index(addr2)][get_address_index(addr1)]
    else:
        return distance_list[get_address_index(addr1)][get_address_index(addr2)]