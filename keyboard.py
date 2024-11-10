#!/usr/bin/env python
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import json

dicio_keys= {
    'a': {'A'}, 'b': {'B'}, 'c': {'C'}, 'ç': {'Ç'}, 'd': {'D'}, 'e': {'E'}, 'f': {'F'}, 'g': {'G'}, 'h': {'H'}, 'i': {'I'}, 'j': {'J'}, 'k': {'K'}, 'l': {'L'}, 'm': {'M'}, 'n': {'N'}, 'o': {'O'}, 'p': {'P'}, 'q': {'Q'}, 'r': {'R'}, 's': {'S'}, 't': {'T'}, 'u': {'U'}, 'v': {'V'}, 'w': {'W'}, 'x': {'X'}, 'y': {'Y'}, 'z': {'Z'},
    'A': {'A', 'SHIFT_L'}, 'B': {'B', 'SHIFT_L'}, 'C': {'C', 'SHIFT_L'}, 'Ç': {'Ç', 'SHIFT_L'}, 'D': {'D', 'SHIFT_L'}, 'E': {'SHIFT_L', 'E'}, 'F': {'F', 'SHIFT_L'}, 'G': {'G', 'SHIFT_L'}, 'H': {'SHIFT_L', 'H'}, 'I': {'I', 'SHIFT_L'}, 'J': {'J', 'SHIFT_L'}, 'K': {'K', 'SHIFT_L'}, 'L': {'L', 'SHIFT_L'}, 'M': {'M', 'SHIFT_L'}, 'N': {'SHIFT_L', 'N'}, 'O': {'O', 'SHIFT_L'}, 'P': {'P', 'SHIFT_L'}, 'Q': {'Q', 'SHIFT_L'}, 'R': {'R', 'SHIFT_L'}, 'S': {'S', 'SHIFT_L'}, 'T': {'T', 'SHIFT_L'}, 'U': {'SHIFT_L', 'U'}, 'V': {'V', 'SHIFT_L'}, 'W': {'W', 'SHIFT_L'}, 'X': {'X', 'SHIFT_L'}, 'Y': {'Y', 'SHIFT_L'}, 'Z': {'Z', 'SHIFT_L'},
    "Key.backspace": {"BACKSPACE"},
    "Key.up": {'UP'},
    "Key.left": {'LEFT'},
    "Key.right": {'RIGHT'},
    "Key.down": {'DOWN'},
    "Key.alt": {'ALT_L'},
    "Key.enter": {'ENTER'},
    "Key.tab": {'TAB'},
    "Key.space": {"SPACE"},
    "Key.ctrl": {"CTRL"},
    "Key.cmd": {"SUPER"},
    "Key.shift_r": {"SHIFT_R"},
    "Key.shift": {"SHIFT_L"},
    "Key.page_up": {"PAGE UP"},
    "Key.page_down": {"PAGE DOWN"},
    "Key.esc": {"ESC"},
    "Key.delete": {"DEL"},
    "Key.home": {"HOME"},
    "Key.media_volume_up":   {"VOL UP"},
    "Key.media_volume_down": {"VOL DOWN"},
    "Key.media_volume_mute": {"MUTE"},
    "Key.media_play_pause":  {"PAUSE/PLAY"},
    "<269025045>":           {"STOP"},
    "Key.media_previous":    {"PREVIOUS"},
    "Key.media_next":        {"NEXT"},
    "Key.caps_lock": {"CAPSLOCK"},
    "Key.end": {"END"},
    "Key.ctrl_r": {"CTRL_R"},
    "Key.print_screen": {"PRNT SCRN"},
    "Key.insert": {"INS"},
    "Key.num_lock": {"NUM LOCK"},
    "Key.f1": {"F1"},
    "Key.f2": {"F2"},
    "Key.f3": {"F3"},
    "Key.f4": {"F4"},
    "Key.f5": {"F5"},
    "Key.f6": {"F6"},
    "Key.f7": {"F7"},
    "Key.f8": {"F8"},
    "Key.f9": {"F9"},
    "Key.f10": {"F10"},
    "Key.f11": {"F11"},
    "Key.f12": {"F12"},
    "Key.cmd": {"WIN"},
    "[^]": {"^"},
    "[~]": {"~"},
    "\\\\": {"\\"},
    "\"\"": {"`"},
    "<65027>": {"ALT_R"},
    "<269025027>": {"DISPLAY BRIGHT DOWN"},
    "<269025026>": {"DISPLAY BRIGHT UP"},
    "<269025053>": {"CALCULATOR"},
    "<269025066>": {"POWER"},
    "[¨]": {'"'},
}
# Carrega os dados do JSON
with open("key_usage.json", "r") as file:
    key_frequencies = json.load(file)

usages = {}
for w_k in key_frequencies.keys():
    if w_k in dicio_keys.keys():
        for val in dicio_keys[w_k]:
            if not val in usages.keys():
                usages[val] = 0
            usages[val] += key_frequencies[w_k]
    else:
        usages[w_k] = key_frequencies[w_k]
# Normalizar as frequências para o intervalo [0, 1]
key_frequencies = usages
max_freq = max(key_frequencies.values())
key_frequencies_normalized = {key: value / max_freq for key, value in key_frequencies.items()}

# Layout do teclado US
keyboard_layout = [
    ['MUTE','VOL DOWN', 'VOL UP','PAUSE/PLAY','PRNT SCRN','POWER'],
    ['ESC', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12'],
    ['"','!','@','#','$','%','&','*','(',')','_','+','DEL'],
    ['\'', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'BACKSPACE'],
    ['TAB', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '\'', '`','[','{' ],
    ['CAPSLOCK', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ç','~', '^',']', '}', 'ENTER'],
    ['SHIFT_L', '\\','|','Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '<','.', '>', ';', ':', 'SHIFT_R'],
    ['CTRL', 'WIN', 'ALT_L', 'SPACE', 'ALT_R', '/','?'],
    ['HOME', 'END', 'PAGE UP', 'PAGE DOWN'],
    ['LEFT', 'DOWN', 'RIGHT', 'UP']
]

# Configurações do layout do gráfico
key_size = (0.9, 0.8)
key_SPACE_size = (5.2, 0.8)
fig, ax = plt.subplots(figsize=(17,10))
ax.set_xlim(0, 17)
ax.set_ylim(-5, 7)
ax.axis('off')

# Mapeamento de teclas para coordenadas
for row_index, row in enumerate(keyboard_layout):
    x = 0
    for key in row:
        # Frequência normalizada ou zero se a tecla não está presente
        frequency = key_frequencies_normalized.get(key, 0)
        color_intensity = plt.cm.Reds(frequency)  # Cor com base na frequência

        # Desenho da tecla
        if 'SPACE' == key:
            rect = patches.Rectangle((x, 5 - row_index), *key_SPACE_size, linewidth=1, edgecolor='black', facecolor=color_intensity)
        else:
            rect = patches.Rectangle((x, 5 - row_index), *key_size, linewidth=1, edgecolor='black', facecolor=color_intensity)
        ax.add_patch(rect)

        # Nome da tecla
        if not key_frequencies.get(key):
            print(f"\t miss key freq.: {key}")
        
        ax.text(x + key_size[0] / 2, 5 - row_index + key_size[1] / 2, f"{key}\n", ha='center', va='center', fontsize=10, color="black")
        ax.text(x + key_size[0] / 2, 5 - row_index + key_size[1] / 2, f"\n({key_frequencies.get(key,0)})", ha='center', va='center', fontsize=8, color="black", style="italic")
        # Avançar posição da tecla
        x += key_size[0] if key != 'SPACE' else key_size[0] * 5

plt.tight_layout()
plt.show()
