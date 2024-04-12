from abc import ABC, abstractmethod

class Movable(ABC):
    @abstractmethod
    def move(self) -> None:
        pass

class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self) -> None:
        pass

class Part(Displayable):
    def __init__(self, partno: int, price: float) -> None:
        self.__partno = partno
        self.__price = price

    @property
    def partno(self) -> int:
        return self.__partno
    
    @partno.setter
    def partno(self, value):
        self.__partno = value

    @property
    def price(self) -> float:
        return self.__price
    
    @price.setter
    def price(self, value):
        self.__price = value

    def __str__(self) -> str:
        return f"partno = {self.__partno}\nprice = {self.__price}"

    def display(self) -> None:
        print(self)

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Part):
            return self.__partno == __value.__partno
        else:
            return False

class MovablePart(Part, Movable):
    def __init__(self, partno: int, price: float, part_type: str) -> None:
        Part.__init__(self, partno, price)
        self.part_type = part_type

    def move(self) -> None:
        print(f"partno: {self.partno} is moving fast!")

    def display(self) -> None:
        super().display()
        print(f"type = {self.part_type}\n")

class Machine(Displayable):
    def __init__(self, machine_name):
        self.__machine_name = machine_name
        self.parts = []

    @property
    def machine_name(self):
        return self.__machine_name
    
    @machine_name.setter
    def machine_name(self, value):
        self.__machine_name = value

    def add_part(self, part):
        self.parts.append(part)

    def remove_part(self, partno):
        self.parts = [part for part in self.parts if part.partno != partno]

    def find_duplicated_parts(self):
        part_counts = {}
        for part in self.parts:
            part_counts[part.partno] = part_counts.get(part.partno, 0) + 1
        return {partno: count for partno, count in part_counts.items() if count > 1}
    
    def display(self):
        print(f"Machine Name: {self.__machine_name}")
        print("Parts:")
        for part in self.parts:
            part.display()

    def dowork(self):
        pass

    def __iter__(self):
        return iter(self.parts)

class JetFighter(Displayable, Flyable):
    def __init__(self, model: str, speed: int) -> None:
        self.__model = model
        self.__speed = speed

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        self.__speed = value

    def fly(self) -> None:
        pass

    def __str__(self) -> str:
        return f"model = {self.__model}\nspeed = {self.__speed}"

    def display(self) -> None:
        print(self)

        
class Robot(Machine, JetFighter):
    def __init__(self, machine_name: str, cpu: str, model: str, speed: int) -> None:
        Machine.__init__(self, machine_name)
        JetFighter.__init__(self, model, speed)  
        self.__cpu = cpu

    def get_model(self) -> str:
        return self.get_model()

    def get_speed(self) -> int:
        return self.get_speed()

    def fly(self) -> None:
        print(f"The JetFighter {self.model} is flying in the sky!")
        print(f"The JetFighter {self.machine_name} is flying over the ocean!")

    def dowork(self) -> None:
        print(f"The robot {self.machine_name} is assembling a big truck.")

    def get_expensive_parts(self, price_threshold):
        return [part for part in self.parts if part.price >= price_threshold]
    
    def get_movable_parts_bytype(self):
        parts_by_type = {}
        for part in self.parts:
            if isinstance(part, MovablePart):
                if part.part_type not in parts_by_type:
                    parts_by_type[part.part_type] = [part]
                else:
                    parts_by_type[part.part_type].append(part)
        return parts_by_type
    
    def get_movable_parts(self):
        movable_parts = []
        for part in self.parts:
            if isinstance(part, Movable):
                movable_parts.append(part)
        return movable_parts
    
    
    def display(self):
        print(f"cpu= {self.__cpu}")
        print(f"Machine Name: {self.machine_name}")
        print("The machine has these parts:")
        for part in self.parts:
            part.display()
        print(f"model = {self.model}")
        print(f"speed = {self.speed}")

    def __detail_str__(self):
        print("The machine has these parts:")
        for part in self.parts:
            part.display()

def main():
    robo = Robot('MTX', 'M1X', 'F-16', 10000)
    robo.add_part(Part(111, 100))
    robo.add_part(Part(222, 200))
    robo.add_part(Part(333, 300))
    robo.add_part(Part(222, 300))
    robo.add_part(MovablePart(555, 300, "TypeA"))
    robo.add_part(Part(111, 100))
    robo.add_part(Part(111, 100))
    robo.add_part(MovablePart(777, 300, "TypeB"))
    robo.add_part(MovablePart(655, 300, "TypeA"))
    robo.add_part(MovablePart(755, 300, "TypeA"))
    robo.add_part(MovablePart(977, 300, "TypeB"))
    robo.display()
    print()

    print("\nRobot test flight----")
    robo.fly()

    print("\nRobot dowork() test ----")
    robo.dowork()

    print("\nDuplicated part list----")
    partfreq = robo.find_duplicated_parts()
    for partno in partfreq.keys():
        print(partno,'=>', partfreq[partno], 'times')

    print("\nExpensive part list----")
    expensive_parts = robo.get_expensive_parts(200)
    for part in expensive_parts:
        part.display()

    print("\nMovable part list----")
    movable_parts = robo.get_movable_parts_bytype()
    for type, parts in movable_parts.items():
        print("type =", type)
        for part in parts:
            part.display()
        print()

    print("\nAsk movable to move----")
    movable_parts = robo.get_movable_parts()
    for part in movable_parts:
        part.move()

    print("\nTest remove_part() ----")
    robo.remove_part(333)
    for part in robo:
        if part.partno == 333:
            print(f"Found 333")
            break

    print("\nParts list after remove:")
    robo.__detail_str__()

if __name__ == "__main__":
    main()