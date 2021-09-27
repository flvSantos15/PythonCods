from tqdm import tqdm

import requests
link = 'https: //cep.awesomeapi.com.br/json/05424020'

# passo 1: pegar a lista de ceps
with open("ceps.txt", "r") as arquivo:
    ceps = arquivo.read()
ceps = ceps.split("\n")

# passo 2: pegar as informações de cada cep
enderecos_entregas = []
for cep in tqdm(ceps):
    link = f'https: //cep.awesomeapi.com.br/json/{cep}'

    # passo 3: verificar se a cidade é Rio de Janeiro
    requisicao = requests.get(link)
    resposta = requisicao.json()
    cidade = resposta['city']
    bairro = resposta['district']

    # passo 4: printar o cep e o bairro
    if cidade == "Rio de Janeiro":
        enderecos_entregas.append((cep, bairro))
print(enderecos_entregas)
