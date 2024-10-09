# TODO Найдите количество книг, которое можно разместить на дискете
stranic=100
strok=50
simvol=25
disketa=1.44*1024*1024
vsegosimvoly=strok*stranic*simvol

knig=disketa/(vsegosimvoly*4)
print("Количество книг, помещающихся на дискету:", round(knig))
