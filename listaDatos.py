import os

import infoTab


class lista_datos:

    def organize_by_weight(self, ruta):

        tamaño_carpeta = get_weight(ruta)

        archivos = []
        if tamaño_carpeta < 1000000:
            print(f"Carpeta: {ruta} - Tamaño: {tamaño_carpeta} bytes")


        else:
            for dirpath, _, filenames in os.walk(ruta):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    archivos.append((filename, get_weight(filepath)))

            archivos.sort(key=lambda x: x[1], reverse=True)
            return archivos

def get_weight(ruta):
    if os.path.isfile(ruta):
        return os.path.getsize(ruta)
    elif os.path.isdir(ruta):
        total_size = 0
        for dirpath, _, filenames in os.walk(ruta):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        return total_size
    else:
        return 0