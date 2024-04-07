from view.card.card import Card
import tkinter as tk

class FoodCard(Card):
    def __init__(self,
                 data : dict):
        super().__init__("Comida", data)