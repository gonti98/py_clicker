import json
from pathlib import Path
from typing import Optional, Dict, Any
import time

from src.game.grinding import Grind
from src.game.buildings import Building, BUILDINGS

class SaveManager:
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    SAVE_GAME_FILE = PROJECT_ROOT / "data" / "save.json"
    VERSION = "0.1"

    @classmethod
    def save_game(cls, coins: int, grind: Grind, buildings: Dict[str, Building], total_playtime: float = 0):
        buildings_data = {name: building.to_dict() for name, building in buildings.items()}
        data = {
            "coins": coins,
            "grind": grind.to_dict(),
            "buildings": buildings_data,
            "metadata": {
                "version": cls.VERSION,
                "last_save": time.strftime("%Y-%m-%d %H:%M:%S"),
                "total_playtime": total_playtime,
                "player_name": "Anonymus",
                "achievements": []
            }
        }
        cls.SAVE_GAME_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(cls.SAVE_GAME_FILE, "w") as file:
            json.dump(data, file, indent=2)

    @classmethod
    def load_game(cls) -> Optional[Dict[str, Any]]:
        if not cls.SAVE_GAME_FILE.exists():
            return None
        try:
            with open(cls.SAVE_GAME_FILE, "r") as file:
                data = json.load(file)
            grind = Grind.from_dict(data.get("grind", {}))
            buildings = {name: building for name, building in BUILDINGS.items()}
            buildings_data = data.get("buildings", {})
            for name, building_data in buildings_data.items():
                if name in BUILDINGS:
                    template = BUILDINGS[name]
                    buildings[name] = Building.from_dict(
                        building_data,
                        template.tick_interval,
                        template.income_per_tick,
                        template.base_cost
                    )
            return {
                "coins": data.get("coins", 0),
                "grind": grind,
                "buildings": buildings,
                "metadata": data.get("metadata", {})
            }
        except (json.JSONDecodeError, KeyError, ValueError):
            return None
