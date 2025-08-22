import requests

country_name = input("Introdu numele unei tari: ")

REST_URL = f"https://restcountries.com/v3.1/name/{country_name}"

print("Se cauta informatii...")
response = requests.get(REST_URL)

if response.status_code == 200:
    print("Tara gasita! Procesam datele...")
    data = response.json()
    info_tara = data[0]
    capitala = info_tara.get('capital')[0]
    populatie = info_tara.get('population')
    print(f"\nCapitala: {capitala}")
    print(f"Populatie: {populatie}")

else:
    print(f"Eroare: Nu am putut gasi tara. Cod de status: {response.status_code}")