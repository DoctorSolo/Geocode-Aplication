from geopy.geocoders import Nominatim   # Vou utilizar um metodo do geopy para me retornar a localização


class SearchLocal:
    geolocator = Nominatim(user_agent="local") # A biblioteca exirge uma instancia para acessar o banco de dados
    
    
    def __init__(self, latitude:float, longitude:float):    # O construtor recebe os paremetros x(latitude) e y(longetude),
            self.latitude   = latitude                      # Os parametros já são definidos para converter qualquer
            self.longitude  = longitude                     # tipo para (float) para evitar erro
    
    
    def __str__(self) -> str:
         return f'{self.latitude}, {self.longitude}'
    
    
    # Esta função sera usada para retornar a localização do banco de dados
    def search_summary(self):
        
        try:    # Caso a localização exista ele retorna todos os dados do local
            location = self.geolocator.reverse(f"{self.latitude}, {self.longitude}")
            return location.address
        
        except:
            return 'The location does not exist'
