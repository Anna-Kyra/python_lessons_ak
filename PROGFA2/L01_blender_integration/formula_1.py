# ==== names ====
names = ["Lando Norris","Max Verstappen","Oscar Piastri","George Russell","Charles Leclerc","Lewis Hamilton","Kimi Antonelli","Alexander Albon","Carlos Sainz Jr","Fernando Alonso","Isack Hadjar","Nico Hulkenberg","Oliver Bearman"]
# ==== teams ====
teams = ["McLaren","Red Bull Racing","McLaren","Mercedes","Ferrari","Ferrari","Mercedes","Williams","Williams","Aston Martin","Racing Bulls","Sauber","Haas"]
medals = '🥇', '🥈', '🥉'

for medal, (index, (name, team)) in zip(medals, enumerate(zip(names, teams), start=1)):
    print(f"{medal} - {name} ({team})")
    print(index)
    if index >= 4:
        print(f"[{index}] - {name} ({team})")
