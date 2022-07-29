class Car:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.self = self
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.color = color
        self.max_speed = max_speed
    def start_enjine(self):
        print(f"Enjine on Title{self.title}Model{self.model}started!")
    def stop_enjine(self):
        print(f"Enjine on Title{self.title}Model{self.model}started!")
    def info(self):
        print(f"All info Title{self.title}\nmodel:{self.model}\nweight:{self.weight}\n")
        print(f"hp:{self.hp}\nnm:{self.nm}\ncolor:{self.color}\nmax_speed:{max_speed}")
mers = Car('mersedes', '/Maybach', '2800 kg', '530', '1500 nm', '320km\h', 'black')
mers.start_enjine()
mers.stop_enjine()
mers.info()
bmw = Car('BMW', 'e30', '1300 kg', '104 hp' '410nm', '250km\h', 'red')
bmw.start_enjine()
bmw.stop_enjine()