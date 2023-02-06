class Robot:
    def __init__(self):
        self.name = input("What is your name: ")

    def greet(self):
        print(f"Hello {self.name}\nThis is Robot")


robot1 = Robot()
robot1.greet()

