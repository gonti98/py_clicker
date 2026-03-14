import time

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
            self.income_per_click += 1
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
        return {
            "income_per_click": self.income_per_click,
            "cooldown": self.cooldown,
            "income_upgrade_count": self.income_upgrade_count,
            "cooldown_upgrade_count": self.cooldown_upgrade_count,
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Grind':
        grind = cls()
        grind.income_per_click = data.get("income_per_click", 1)
        grind.cooldown = data.get("cooldown", 1.0)
        grind.income_upgrade_count = data.get("income_upgrade_count", 0)
        grind.cooldown_upgrade_count = data.get("cooldown_upgrade_count", 0)
        return grind
