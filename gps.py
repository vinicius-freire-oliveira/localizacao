from geopy.geocoders import Nominatim  # Importa a classe Nominatim da biblioteca geopy para geocodificação

# Inicialize o geocoder com um agente de usuário personalizado
geolocator = Nominatim(user_agent="my_geocoder")

# Função para obter coordenadas a partir de um endereço
def obter_coordenadas(endereco):
    try:
        location = geolocator.geocode(endereco)  # Tenta obter a localização a partir do endereço
        if location:
            return location.latitude, location.longitude  # Se a localização for encontrada, retorna latitude e longitude
        else:
            return None, None  # Se a localização não for encontrada, retorna None para ambos
    except Exception as e:
        print("Ocorreu um erro:", e)  # Imprime a mensagem de erro, se houver
        return None, None  # Retorna None para latitude e longitude em caso de erro

# Função para obter endereço a partir de coordenadas
def obter_endereco(latitude, longitude):
    try:
        location = geolocator.reverse((latitude, longitude))  # Tenta obter o endereço a partir das coordenadas
        if location:
            return location.address  # Se a localização for encontrada, retorna o endereço
        else:
            return None  # Se a localização não for encontrada, retorna None
    except Exception as e:
        print("Ocorreu um erro:", e)  # Imprime a mensagem de erro, se houver
        return None  # Retorna None para o endereço em caso de erro

# Exemplo de uso: geocodificação (obter coordenadas a partir de um endereço)
endereco = "Praça do Marco Zero, Recife/PE"
latitude, longitude = obter_coordenadas(endereco)  # Obtém as coordenadas para o endereço fornecido
if latitude and longitude:
    print("Endereço:", endereco)
    print("Latitude:", latitude)
    print("Longitude:", longitude)
else:
    print("Endereço não encontrado.")  # Mensagem exibida se o endereço não for encontrado

print()

# Exemplo de uso inverso: reverso (obter endereço a partir de coordenadas)
latitude_exemplo = -7.120284
longitude_exemplo = -34.880096
endereco_inverso = obter_endereco(latitude_exemplo, longitude_exemplo)  # Obtém o endereço para as coordenadas fornecidas
if endereco_inverso:
    print("Coordenadas:", (latitude_exemplo, longitude_exemplo))
    print("Endereço:", endereco_inverso)
else:
    print("Coordenadas não encontraram um endereço.")  # Mensagem exibida se o endereço não for encontrado para as coordenadas
