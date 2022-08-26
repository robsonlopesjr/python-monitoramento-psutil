from psutil import cpu_freq, cpu_count, cpu_percent, cpu_times


def mega_to_gigas(value):
    return f'{value / 1000: .2f}GHz'


def seconds_to_minutes(value):
    return divmod(value, 60)


def minutes_to_hours(value):
    return divmod(value, 60)


'''
* Médida de todos os núcleos
scpufreq(
    current=3600.0, # Frequencia atual
    min=0.0, # Frequencia Mínima
    max=3600.0 # Frequencia máxima
)
'''
print(cpu_freq())  # Dados são em MHz

print(mega_to_gigas(cpu_freq().current))

# Pegar a frequência por núcleo caso tenha mais de um
print(cpu_freq(percpu=True))

# Núcleos físicos e lógicos
print(cpu_count())

# Somente núcleos físicos
print(cpu_count(logical=False))

# Porcentagem de uso do CPU
print(cpu_percent())

# Calcula o valor por um tempo determinado
print(cpu_percent(interval=1))

# Todos os núcleos (F + L)
print(cpu_percent(percpu=True))

'''
* Metricas gerais desde que o computador foi ligado
scputimes(
    user=20034.171875, # Tempo gasto pelo usuário no sistema (dado em Segundos)
    system=11998.25, # tempo gasto com o sistema
    idle=174578.359375, # tempo gasto sem fazer nada (Tempo que o processador ficou ocioso)
    ...
)
'''
print(cpu_times())
