from matplotlib.colorbar import Colorbar



cadena = 'WBWBWWWB'
Filas = 2
Columnas = 4

posx = 0
posy = 0


for c in cadena:
    print(c, "(",posx,",",posy,")")
    posx +=1


# for y in range(Filas):
#     posy += 1
#     for x in range(Columnas):
#         posx += 1
#         print('(',posx,',',posy,')', end="")
#     posx = 0
#     print('')
    
