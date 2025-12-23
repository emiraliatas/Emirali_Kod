class Package:
    def __init__(self, id, sender, recipient, weight):
        self.id = id
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    def __str__(self):
        return f"Package {self.id}: {self.sender} to {self.recipient}, {self.weight}kg"
    
    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg




def main():
    packages = [
        Package(id=1, sender="Bob", recipient="Alice", weight=5),
        Package(id=2, sender="Alice", recipient="Charlie", weight=7)
    ]
    for package in packages:
        print(f"{package}, costs {package.calculate_cost(cost_per_kg=3)}") 


if __name__ == "__main__":
    main()

