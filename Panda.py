class Panda:
    def __init__(self, name, age, weight, health_status):
        self.name = name
        self.age = age
        self.weight = weight
        self.health_status = health_status

    def display(self):
        return f"{self.name} is a {self.age} year old, {self.health_status} panda, weighing {self.weight} kg"

    def check_health(self):
        return f"{self.name} is currently {self.health_status}."


