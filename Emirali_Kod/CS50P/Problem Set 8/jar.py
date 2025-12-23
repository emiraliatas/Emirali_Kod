class Jar:
    def __init__(self, capacity):
        self._capacity = capacity
        self._size = 0
        
    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        for _ in range(n):
            self.size += 1
        


    def withdraw(self, n):
        for _ in range(n):
            if self.size < 0:
                raise ValueError("There isn't that many cookie.") 
            self.size -= 1

        
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, value):
        if int(value) < 0:
            raise ValueError("Capacity can't be negative.")
        self._capacity = value
    


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if int(n) > self.capacity:
            raise ValueError("You can't withdraw/deposit numbers bigger than capacity.")
        self._size = n

def main():
    j = Jar(10)
    j.deposit(5)
    j.withdraw(3)
    print(j)



if __name__ == "__main__":
    main()