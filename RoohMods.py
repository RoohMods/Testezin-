import json

file = 'RoohJson.json'

with open(file, "r") as arquivo:
    base = json.load(arquivo)

print(base)
base.append("Rooh Mods")

with open(file, "w") as dados:
    json.dump(base, dados)