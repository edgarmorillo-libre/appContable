print(" ***** Bienvenido al sistema de compras ****")
compras = float(input("Ingrese el monto de la compra: "))
iva = compras * 0.12
total = compras + iva
print("El monto de la compra es: ", compras)
print("El IVA es: ", iva)
print("El total a pagar es: ", total)