import requests, pandas as pd, time

rows = []
romer = {"i":1,"ii":2,"iii":3,"iv":4,"v":5,"vi":6,"vii":7,"viii":8,"ix":9}  
for i in range(1, 1026):
    p = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}").json()
    s = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{i}").json()
    stats = {st["stat"]["name"]: st["base_stat"] for st in p["stats"]}
    evo = s["evolves_from_species"]
    rows.append({
        "id": i,
        "name": p["name"],
        "height_m": p["height"] / 10,     # desimeter -> meter
        "weight_kg": p["weight"] / 10,    # hektogram -> kg
        "type1": p["types"][0]["type"]["name"],
        "type2": p["types"][1]["type"]["name"] if len(p["types"]) > 1 else None,
        **stats,
        "generation": romer[s["generation"]["name"].split("-")[1]],
        "capture_rate": s["capture_rate"],
        "evolves_from_id": int(evo["url"].rstrip("/").split("/")[-1]) if evo else None,
        "is_baby": s["is_baby"], 
        "is_legendary": s["is_legendary"],
        "is_mythical": s["is_mythical"],
        "capture_rate": s["capture_rate"],
    })

pd.DataFrame(rows).to_csv("pokemon.csv", index=False)
