class Package:
    def __init__(self, package_id, package_address, city, state, zipcode, deadline, weight, notes, status):
        self.package_id = package_id
        self.package_address = package_address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.loading_time = None
        self.deliver_time = None
        self.status = status

    def __str__(self): # creating print statement for a package object
        return (f"ID: {self.package_id}, Address: {self.package_address}, {self.city}, {self.state}, {self.zipcode}, "
                f"Deadline: {self.deadline}, Weight: {self.weight} kg, Status: {self.status}")

    def __repr__(self):
        return (f"ID: {self.package_id}, Address: {self.package_address}, {self.city}, {self.state}, {self.zipcode}, "
                f"Deadline: {self.deadline}, Weight: {self.weight} kg, Status: {self.status}")
