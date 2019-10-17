from objects import * # Animal, Predator, Victim, ...


class Field():
    # Объявим по дефолту пустую доп. инициализацию:
    field_additional_init = lambda self: None

    def __init__(self, max_field_x, max_field_y):
        self.max_field_x = max_field_x
        self.max_field_y = max_field_y
        self.predator = objects[Predator][0]
        self.victims = objects[Victim]
        '''
        Initializes a `Field` object
                Parameters:
                    max_field_x (integer, obligatory):
                        A x axis field size 
                    max_field_y (integer, obligatory):
                        A y axis field size   
        '''
    def show(self):     #Перед вызовом необходимо обновить поле
        field = []
        for i in self.max_field_y:
            field.append('#'*self.max_field_x)      #Будем обозначать '#' пустую клетку
        field[self.predator.y][self.predator.x] = '0'   #Будем обозначать '0' охотника
        for victim in self.victims:
            field[victim.y][victim.x] = 'x'     #Будем обозначать 'x' жертв
        print(field)
        '''
            This method print field in ascii pseudographics 
        '''

    def update(self):
        self.predator = objects[Predator][0]
        self.victims = objects[Victim]
        '''
            This method update victims and predator's coordinates
        '''