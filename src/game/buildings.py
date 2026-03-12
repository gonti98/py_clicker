import time
from math import pow

GROWTH_RATE = 1.15

class Building:
    def __init__(self, tick_interval: float, income_per_sec: int, base_cost: int):
        self.tick_interval = tick_interval
        self.income_per_sec = income_per_sec
        self.base_cost = base_cost
        self.count = 0
        self.last_income_time = time.time()

    @property
    def income_per_sec_total(self) -> int:
        return (self.income_per_sec * self.count) / self.tick_interval

    @property
    def next_cost(self) -> int:
        return int(self.base_cost * pow(GROWTH_RATE, self.count))

    def generate_income(self, coins: int) -> int:
        now = time.time()
        if now - self.last_income_time >= self.tick_interval:
            elapsed_secs = now - self.last_income_time
            income = int(elapsed_secs * self.income_per_sec_total)
            self.last_income_time = now
            return coins + income
        return coins

    def buy(self, coins: int) -> int:
        cost = self.next_cost
        if coins >= cost:
            self.count += 1
            return coins - cost
        return coins
