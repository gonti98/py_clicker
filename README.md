# py_clicker

To jest Opis po co jak gdzie i co

## Requirements

* `Python` >= 3.14.3

### Nice to have

* GPU acelerated terminal emulator like Alacritty or Ghostty
* Nerd Fonts

## How to run

Teraz na razie `./init.sh`

## Struktura

├── assets
│   ├── logo.py
│   └── style.tcss
├── data
├── init.sh
├── README.md
├── requirements.txt
└── src
    ├── main.py
    ├── screens
    │   ├── game_screen.py
    │   └── main_menu.py
    └── utils
        └── temp_save_load.py

## TODO

* Dobrze działające menu główne oraz gry głównej
* Mechanizma zapisywania/wczytywania:
  * może rózne save'y
* Settings:
  * buttony z pliku
* Podstawowa logika gry:
  * ograniczona predkość klikania żeby zodobyć punkt
  * pasek pokazujący kiedy można znów kliknąć (jeśli można)
  * pierwszy budynek
  * podstawowe upgrad'y

## Idea

Może przekazywać zapis z main_menu do game_screen jako argument tak żeby continue odpalało z zapisem, a new game zawsze od zera.
