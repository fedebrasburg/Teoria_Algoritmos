class ResultadoDFS:

    def __init__(self, tiempo_visitado, tiempo_finalizado, bosque, puntos_artic):
        self.bosque = bosque
        self.tiempo_finalizado = tiempo_finalizado
        self.tiempo_visitado = tiempo_visitado
        self.puntos_artic = puntos_artic

    def get_tiempo_visitado(self):
        return self.tiempo_visitado

    def get_tiempo_finalizado(self):
        return self.tiempo_finalizado

    def get_bosque_DFS(self):
        return self.bosque

    def get_puntos_artic(self):
        return self.puntos_artic