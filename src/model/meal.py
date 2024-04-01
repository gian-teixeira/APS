from food import Food, FoodType

class Meal:
    #def __init__(self,main_course,dessert,juice,salad,side_dish):
            #self._main_course = main_course
            #self._dessert = dessert
            #self._juice = juice
            #self._salad = salad
            #self._side_dish = side_dish

    def __init__(self,foods):
        for food in foods:
            type = food.Type
            if(type == FoodType.MAIN_COURSE):
                self._main_course = food
            elif(type == FoodType.DESSERT):
                self._dessert = food
            elif(type == FoodType.JUICE):
                self._juice = food
            elif(type == FoodType.SALAD):
                self._salad = food
            elif(type == FoodType.SIDE_DISH):
                self._side_dish = food

    #GETTERS
        
    @property
    def main_course(self):
        return self._main_course

    @property
    def dessert(self):
        return self._dessert
    
    @property
    def juice(self):
        return self._juice
    
    @property
    def salad(self):
        return self._salad
    
    @property
    def side_dish(self):
        return self._side_dish
    
    # SETTERS
    
    @main_course.setter
    def main_course(self, value : Food):
        if value.type == FoodType.MAIN_COURSE:
            self._main_course = value

    @dessert.setter
    def dessert(self, value : Food):
        if value.type == FoodType.DESSERT:
            self._dessert = value
    
    @juice.setter
    def juice(self, value : Food):
        if value.type == FoodType.JUICE:
            self._juice = value
    
    @salad.setter
    def salad(self, value : Food):
        if value.type == FoodType.SALAD:
            self._salad = value
    
    @side_dish.setter
    def side_dish(self, value : Food):
        if value.type == FoodType.SIDE_DISH:
            self._side_dish = value
    