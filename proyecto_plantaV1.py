# Simulador de Planta Industrial
# Proyecto del Plan Carrera - Programación Orientada a Objetos

import random  # Se utiliza para simular las mediciones de sensores y tanques


class Planta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def Mostrar_info(self):
        print(f"========================================\n {self.nombre}\n========================================")

        for equipo in self.equipos:
            equipo.Mostrar_info()


class Motor:
    def __init__(self, id, velocidad, estado):
        self.id = id
        self.velocidad = velocidad
        self.estado = estado

    def Mostrar_info(self):
        print(f"[{self.id}] Motor - Estado: {self.estado} - Velocidad: {self.velocidad}")


class Sensor:
    def __init__(self, id, estado, valor):
        self.id = id
        self.estado = estado
        self.valor = valor

    def leer(self):
        self.valor = random.randint(0, 100)
        return self.valor

    def Mostrar_info(self):
        print(f"[{self.id}] Sensor - Estado: {self.estado} - Valor: {self.valor}")


class Valvula:
    def __init__(self, id, estado):
        self.id = id
        self.estado = estado

    def Mostrar_info(self):
        print(f"[{self.id}] Valvula - Estado: {self.estado}")


class Tanque:
    def __init__(self, id, estado, producto, capacidad):
        self.id = id
        self.estado = estado
        self.producto = producto
        self.capacidad = capacidad
        self.nivel = 0

    def leer(self):
        self.nivel = random.randint(0, 100)
        return self.nivel

    def Mostrar_info(self):
        print(f"[{self.id}] Tanque - Estado: {self.estado} - Producto: {self.producto} - Nivel: {self.nivel}% - Capacidad: {self.capacidad} L")


def main():
    planta = Planta("FINCA BUGA")

    motor1 = Motor("TRA001", 100, "Andando")
    sensor1 = Sensor("HL_001", "Inactivo", 0)
    valvula1 = Valvula("Val_001", "Cerrada")
    tanque1 = Tanque("TQ_001", "Lleno", "Agua", 1000)

    sensor1.leer()
    tanque1.leer()

    planta.agregar_equipo(motor1)
    planta.agregar_equipo(sensor1)
    planta.agregar_equipo(valvula1)
    planta.agregar_equipo(tanque1)

    planta.Mostrar_info()


if __name__ == "__main__":
    main()