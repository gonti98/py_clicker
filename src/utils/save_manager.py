import json
from pathlib import Path
from typing import Optional
import time

from src.game.grinding import Grind

class SaveManager:
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    SAVE_GAME_FILE = PROJECT_ROOT / "data" / "save.json"
    VERSION = "0.1"

    @classmethod
    def save_game(cls, coins: int, grind: Grind, total_playtime: float = 0):
        data = {
            "coins": coins,
            "grind": grind.to_dict(),
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
            return {
                "coins": data.get("coins", 0),
                "grind": Grind.from_dict(data.get("grind", {})),
                "metadata": data.get("metadata", {})
            }
        except (json.JSONDecodeError, KeyError, ValueError):
            return None
