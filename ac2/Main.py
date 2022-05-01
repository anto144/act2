from ManejadorViajero import ManejadorViajero
from ViajeroFrecuente import Viajero
import os

if __name__=='__main__':
    lista = ManejadorViajero()
    lista.GenerarLista()
    lista.ListarViajeros()
    NroViaj= int(input("Ingrese nro de viajero del cual desea consultar\n"))
    Viajero= lista.buscar(NroViaj)
    
    continuar = True

    while continuar:
        print("MENU".center(20,"-"))
        print("[1] Para consultar cantidad de millas")
        print("[2] Para acumular millas")
        print("[3] Para canjear millas")
        print("[0] Para SALIR del menu")

        op = int( input("INGRESE OPCION POR TECLADO\n"))
        os.system("cls")
        if ( op == 1):
            print("".center(20,"-"))
            print("Consultar cantidad de millas\n")
            print(Viajero.cantidadMillas())
        elif(op == 2):
            acum = int(input("Ingrese cantidad de millas que desea acumular\n"))
            Viajero.acumularMillas(acum)
        elif(op == 3):
            canje = int(input("Ingrese millas que desea canjear\n"))
            Viajero.canjearMillas(canje)
        elif(op == 0):
            continuar = not continuar