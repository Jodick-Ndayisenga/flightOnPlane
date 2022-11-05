# the code will check if there is any place available on plane and add if yes

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.people = []

    def check_place(self):
        per = input('what is your name? ')
        if len(self.people) < 5:
            self.add_passenger(per)
            for name in self.people:
                print(f'We have on the flight: {name}')
            print(f'And we have only {5-len(self.people)} places available')
            # print(self.people)
        else:
            print(f'I am sorry, we could not add {per}')
            quit()

    def add_passenger(self, x):
        self.people.append(x)


flight = Flight(5)
while True:
    flight.check_place()
