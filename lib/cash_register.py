#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = None

  def add_item(self, title, price, quantity=1):
        item_price = price * quantity
        self.total += item_price
        self.items.extend([title] * quantity)
        self.last_transaction = (title, item_price)

  def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

  def void_last_transaction(self):
        if self.last_transaction:
            last_item_title, last_item_price = self.last_transaction
            self.total -= last_item_price
            self.items.remove(last_item_title)
            self.last_transaction = None
