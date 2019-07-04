import requests

def get_pokemones(url='https://pokeapi.co/api/v2/pokemn/', offset=0):
    count = int(input('¿Cuantos pokemons desea mostrar?'))
    args = {'offset':offset, 'limit':count} if offset else {'limit':count}
    response = requests.get(url, params=args)
     
    if response.status_code == 200:
        payload = response.json()
        pokemones = payload.get('results', [])

        for pokemon in pokemones:
            name_pokemon = pokemon['name']
            print(name_pokemon)

        next_pokemon = input('¿Desea mostrar mas pokemons?').lower()
        if next_pokemon == 'y':
            get_pokemones(offset=offset+count)
    else:
        print('No se pudo realizar el request, !Error¡ 404')
    
    


if __name__ == '__main__':
    get_pokemones()
    



