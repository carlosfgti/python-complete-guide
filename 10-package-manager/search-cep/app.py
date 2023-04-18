import requests

cep = input("CEP: ")
headers = {
    "Content-Type": "application/json"
}
response = requests.get(
    url=f"https://viacep.com.br/ws/{cep}/json",
    headers=headers
)
if (response.status_code == 200):
    json_data = response.json()
    cep = json_data.get("cep")
    logradouro = json_data.get("logradouro")
    complemento = json_data.get("complemento")
    bairro = json_data.get("bairro")
    localidade = json_data.get("localidade")
    print(cep, logradouro, complemento, bairro, localidade)
else:
    print("Error")