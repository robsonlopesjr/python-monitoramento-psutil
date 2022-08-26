from psutil import sensors_fans, sensors_battery, sensors_temperatures

# Velocidade em RPM do cooler
# Não está disponível para windows
# https://psutil.readthedocs.io/en/latest/#sensors
print(sensors_fans())

# Porcentagem da bateria (notebooks)
print(sensors_battery())

# Não está disponível para windows
print(sensors_temperatures())
'''
    acpitz => Zona termal, pode ser qualquer sensor (Ex: Se o HD SSD tiver um medidor de temperatura, irá aparecer aqui)
    pch_skylake => Platform Controller Hub (Específico da Intel, quem tem processador do skylake para cima)
    iwlwifi_1 => Temperatura da placa do Wifi
    coretemp => Temperatura do processador (Não considera os núcleos lógicos)
'''
