import time
from math import pow
from typing import Dict


GROWTH_RATE = 1.15


class Grind:
    def __init__(self):
        self.cooldown = 1.0
        self.income_per_click = 1
        self.last_click_time = time.time()
        self.income_upgrade_count = 0
        self.base_income_upgrade_cost = 50
        self.cooldown_upgrade_count = 0
        self.base_cooldown_upgrade_cost = 100

    @property
    def is_ready(self) -> bool:
        return time.time() - self.last_click_time >= self.cooldown

    @property
    def next_income_upgrade_cost(self) -> int:
        return int(self.base_income_upgrade_cost * pow(GROWTH_RATE, self.income_upgrade_count))

    @property
    def next_cooldown_upgrade_cost(self) -> int:
        return int(self.base_cooldown_upgrade_cost * pow(GROWTH_RATE, self.cooldown_upgrade_count))

    def click(self, coins: int) -> int:
        if not self.is_ready:
            return coins
        self.last_click_time = time.time()
        return coins + self.income_per_click

    def income_upgrade(self, coins: int) -> int:
        cost = self.next_income_upgrade_cost
        if coins >= cost:
            self.income_per_click = (self.income_per_click + 0.2) * 1.1
            self.income_upgrade_count += 1
            return coins - cost
        return coins

    def cooldown_upgrade(self, coins: int) -> int:
        cost = self.next_cooldown_upgrade_cost
        if coins >= cost:
            self.cooldown *= 0.9
            self.cooldown_upgrade_count += 1
            return coins - cost
        return coins

    def to_dict(self) -> dict:
        data = self.__dict__.copy()
        data.pop('last_click_time', None)
        data.pop('base_income_upgrade_cost', None)
        data.pop('base_cooldown_upgrade_cost', None)
        return data

    @classmethod
    def from_dict(cls, data: dict) -> 'Grind':
        grind = cls()
        for key, value in data.items():
            setattr(grind, key, value)
        grind.last_click_time = time.time()
        return grind
