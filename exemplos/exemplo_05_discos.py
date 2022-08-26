from psutil import disk_usage, disk_partitions, disk_io_counters

'''
Informações de uso do disco selecionado
sdiskusage(
    total=492211896320,
    used=124208533504,
    free=368003362816,
    percent=25.2
)
'''
print(disk_usage('C:'))

'''
Informações sobre as partições do computador
[
    sdiskpart(
        device='C:\\',
        mountpoint='C:\\',
        fstype='NTFS',
        opts='rw,fixed',
        maxfile=255,
        maxpath=260
    ),
    sdiskpart(
        device='D:\\',
        mountpoint='D:\\',
        fstype='',
        opts='cdrom',
        maxfile=255,
        maxpath=260
    ),
    ...
]
'''
print(disk_partitions())

'''
Saber quantos bytes foram escritos no disco
sdiskio(
    read_count=3154111, # Leituras
    write_count=1995081, # Escrituras
    read_bytes=119522288640, # Bytes Lidos
    write_bytes=84288272896, # Bytes Escritos
    read_time=7190, # Milissegundos Lendo
    write_time=1029 # Milissegundos Escrevendo,
    bust_time=905390 # Tempo gasto em Entrada / Saida
)
'''
print(disk_io_counters())

# Saber quantos bytes foram escritos por disco
print(disk_io_counters(perdisk=True))

