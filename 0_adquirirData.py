import json
import requests
import sys

def getTVMAZE(date_var:str):
    
    url = 'http://api.tvmaze.com/schedule/web?date='
    url += date_var
    responseTVMAZE = requests.get(url)
    
    if responseTVMAZE.status_code == 200:
        data = responseTVMAZE.json()
        with open(f'datos_{date_var}.json', 'w', encoding='utf-8') as archivo:
            json.dump(data, archivo, indent=2, ensure_ascii=False)
            print(f'El json fue almacenado con el nombre de datos_{date_var}')
            print(f'Elementos en el json: {len(data)}')
    else: return 'Error'
    
def main():
    if len(sys.argv) < 2:
        print("Por favor, proporciona una fecha en formato YYYY-MM-DD")
        print("Ejemplo: python 0_adquirirData.py 2024-01-01")
        return
        
    getTVMAZE(sys.argv[1])

if __name__ == "__main__":
    main()