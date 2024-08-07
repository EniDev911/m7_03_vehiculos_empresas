from .models import Vehiculo, Chofer, RegistroContabilidad


def crear_vehiculo(patente, marca, modelo, year):
    return Vehiculo.objects.create(
        patente=patente, marca=marca, modelo=modelo, year=year
    )


def crear_chofer(rut, nombre, apellido, creacion, vehiculo):
    chofer = Chofer(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        creacion_registro=creacion,
        vehiculo=vehiculo,
    )
    chofer.save()


def crear_registro_contable(fecha_compra, valor, vehiculo):
    RegistroContabilidad(
        fecha_compra=fecha_compra, valor=valor, vehiculo=vehiculo
    ).save()


def deshabilitar_chofer(chofer):
    chofer = Chofer.objects.get(pk=chofer.rut)
    chofer.activo = False
    chofer.save()


def deshabilitar_vehiculo(vehiculo):
    vehiculo = Vehiculo.objects.get(pk=vehiculo.patente)
    vehiculo.activo = False
    vehiculo.save()


def habilitar_chofer(chofer):
    chofer = Chofer.objects.get(pk=chofer.rut)
    chofer.activo = True
    chofer.save()


def habilitar_vehiculo(vehiculo):
    vehiculo = Vehiculo.objects.get(pk=vehiculo.patente)
    vehiculo.activo = True
    vehiculo.save()


def obtener_vehiculo(vehiculo):
    return Vehiculo.objects.get(pk=vehiculo.patente)


def obtener_chofer(chofer):
    return Chofer.objects.get(pk=chofer.rut)


def asignar_chofer_a_vehiculo(chofer, vehiculo):
    try:
        actualizado = Chofer.objects.filter(rut=chofer.rut).update(vehiculo=vehiculo)
        if actualizado == 1:
            print("Se actualizo correctamente")
    except Exception as e:
        print(e)


def imprimir_datos_vehiculos():
    print("== Vehículos actuales ==")
    for vehiculo in Vehiculo.objects.all():
        print(vehiculo)
