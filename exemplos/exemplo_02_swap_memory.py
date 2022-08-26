from psutil import swap_memory


def bytes_to_gigas(value):
    return f'{value / 1024 / 1024 / 1024: .2f}GB'


# Total de memoria
print(bytes_to_gigas(swap_memory().total))

# Total de memoria usada
print(bytes_to_gigas(swap_memory().used))

# SIN = Número de bytes que já foram escritos na swap
print(bytes_to_gigas(swap_memory().sin))

# SOUT = Número de bytes que foram tirados da swap
print(bytes_to_gigas(swap_memory().sout))
