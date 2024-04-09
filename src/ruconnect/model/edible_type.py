from enum import Enum

class EdibleType(Enum):
    MAIN_COURSE = "Prato principal"
    SIDE_DISH = "Acompanhamento"
    MEAT = "Carne"
    VEGETARIAN = "Vegetariano"
    JUICE = "Suco"
    DESSERT = "Sobremesa"