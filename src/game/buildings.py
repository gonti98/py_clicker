import time
from math import pow
from typing import Dict


GROWTH_RATE = 1.15


class Building:
    def __init__(self, tick_interval: float, income_per_tick: int, base_cost: int):
        self.count = 0
        self.tick_interval = tick_interval
        self.income_per_tick = income_per_tick
        self.base_cost = base_cost

    def get_cost(self) -> int:
        return int(self.base_cost * pow(GROWTH_RATE, self.count))

    def buy(self, coins: int) -> int:
        cost = self.get_cost()
        if coins >= cost:
            self.count += 1
            return coins - cost
        return coins

    def get_income_per_tick(self) -> int:
        return self.count * self.income_per_tick

    def get_income_per_second(self) -> float:
        return self.get_income_per_tick() / self.tick_interval

    def to_dict(self) -> dict:
        return {
            "count": self.count
        }

    @classmethod
    def from_dict(cls, data: dict, tick_interval: float, income_per_tick: int, base_cost: int) -> 'Building':
        building = cls(tick_interval, income_per_tick, base_cost)
        building.count = data.get("count", 0)
        return building

BUILDINGS = {
    "meadow": Building(1.0, 1, 100),
    "grove": Building(2.0, 10, 1000),
    "forge": Building(3.0, 100, 10000),
    "tower": Building(8.0, 2000, 200000),
    "alchemist": Building(10.0, 20000, 2000000),
    "portal": Building(12.0, 200000, 20000000),
    "dragon": Building(21.0, 3000000, 300000000),
    "citadel": Building(24.0, 30000000, 3000000000),
    "worldtree": Building(27.0, 300000000, 30000000000),
}
