import csv

from package import Package

# function to load distance data from a csv into a list
def load_distances(filename):
    with open(filename, 'r', encoding='utf-8-sig') as distance_csv:
        distances = csv.reader(distance_csv)
        distances = list(distances)
    return distances

# function to load address data from a csv into a list
def load_addresses(filename):
    with open(filename, 'r', encoding='utf-8-sig') as address_csv:
        addresses = csv.reader(address_csv)
        addresses = list(addresses)
    return addresses

# function to load packages from csv into a hash table
def load_package(filename, hash_table):
    with open(filename, 'r', encoding='utf-8-sig') as package_csv:
        package_info = csv.reader(package_csv)
        for row in package_info:
            package = Package(
                package_id = int(row[0]),
                package_address = row[1],
                city = row[2],
                state = row[3],
                zipcode = row[4],
                deadline = row[5],
                weight = int(row[6]),
                notes = row[7] if len(row) > 7 else '',
                status = 'At Hub'
            )
            hash_table.insert(package.package_id, package)