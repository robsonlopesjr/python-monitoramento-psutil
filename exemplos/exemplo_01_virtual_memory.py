from psutil import virtual_memory


# O total mostrado é na medida bytes
# total / 1024 = KB
# total / 1024 / 1024 = MB
# total / 1024 / 1024 / 1024 = GB
# print(virtual_memory())

def bytes_to_gigas(value):
    return f'{value / 1024 / 1024 / 1024: .2f}GB'


# Total de memoria
print(bytes_to_gigas(virtual_memory().total))

# Total de memoria usada
print(bytes_to_gigas(virtual_memory().used))
