from objects import Animal, Predator


class Field():
    def __init__(self, max_field_x, max_field_y):
        """Initializes a `Field` object
                Parameters:
                    max_field_x (integer, obligatory):
                        A x axis field size 
                    max_field_y (integer, obligatory):
                        A y axis field size   
        """
        self.max_field_x = max_field_x
        self.max_field_y = max_field_y
        self.predator = objects[Predator][0]
        self.victims = objects[Victim]

    def update(self):
        """This method update victims and predator's coordinates
        """
        self.predator = objects[Predator][0]
        self.victims = objects[Victim]
    
    def show(self):     #Перед вызовом необходимо обновить поле
        """This method print field in ascii pseudographics 
        """
        field = []
        for i in self.max_field_y:
            field.append('#'*self.max_field_x)      #Будем обозначать '#' пустую клетку
        field[self.predator.y][self.predator.x] = '0'   #Будем обозначать '0' охотника
        for victim in self.victims:
            field[victim.y][victim.x] = 'x'     #Будем обозначать 'x' жертв
        print(field)