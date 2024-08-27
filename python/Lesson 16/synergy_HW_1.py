class CashRegister:
  def __init__(self):
    self.balance = 0
  def top_up(self, X):
    self.balance += X
    print(f"Касса пополнена на {X} рублей. Текущий баланс: {self.balance} рублей.")
  def count_1000(self):
    thousands = self.balance // 1000
    return f"В кассе осталось {thousands} тысяч рублей."
  def take_away(self, X):
    if X > self.balance:
      print(f"Недостаточно денег в кассе! Доступно только {self.balance} рублей.")
    else:
      self.balance -= X
      print(f"Из кассы изъято {X} рублей. Текущий баланс: {self.balance} рублей.")

register = CashRegister()

register.top_up(5000)
print(register.count_1000())
register.take_away(3000)
print(register.count_1000())
register.take_away(3000)