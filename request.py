import requests
from colorama import Fore, Style


# to use change the name of json in the url bellow
# with one of rarity.tools website nft collection
# it will print and save in a txt the traits
# it's usefull to analyse diferent collecttions rarity by traits

nft = 'punkcats'

url = f'http://projects.rarity.tools/static/staticdata/{nft}.json'

r = requests.get(url)
atributos = r.json()['basePropDefs']

lines = [nft]
traits = 0

print(Fore.GREEN + nft)

traits_total_list = []
for atributo in atributos:
    try:
        
        count_traits = 0

        for item in atributo['pvs']:
            count_traits += item[1]
                    
        traits_total_list.append(count_traits)
        
    except:
        pass

print(traits_total_list)
for atributo in atributos:
    try:
        traits += 1
        raridade = 0
        print()
        print(Fore.GREEN + str(traits) + ': ' +atributo['name'].upper())
        print(Style.RESET_ALL)
        lines.append(str(traits) + ': ' +atributo['name'].upper())
        lines.append('')
        for item in atributo['pvs']:
            
            quantidade = item[1]
            raridade = quantidade / traits_total_list[traits-1]
            item.append(raridade)

            nome_atributo = item[0]
            quantidade_atributo = item[1]
            raridade = item[-1]
            
            print(nome_atributo, quantidade_atributo, raridade)
            lines.append(f'{nome_atributo}: {raridade}')
        
        lines.append(f'Total de atributos: {len(atributo["pvs"])}')
        print(f'Total de atributos: {len(atributo["pvs"])}')
        lines.append('')

    except:
        pass

lines.append(f'Total de traits: {traits}')

print(f'\nTotal de traits: {traits}')

with open(f'{nft.lower()}_atributos.txt', 'w') as f:
    for line in lines:
        f.write(str(line) + '\n')
