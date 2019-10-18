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

    def update(self, predator, victims):
        """This method update victims and predator's coordinates
        """
        self.predator = predator
        self.victims = victims
    
    def show(self):     #Перед вызовом необходимо обновить поле
        """This method print field in ascii pseudographics 
        """
        field = []
        for i in range(self.max_field_y):
            field.append(['#' for i in range(self.max_field_x)])
        field[self.predator.y][self.predator.x] = '0'   #Будем обозначать '0' охотника
        for victim in self.victims:
            field[victim.y][victim.x] = 'x'     #Будем обозначать 'x' жертв
        print('\n'.join(''.join(line) for line in field))