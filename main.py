from dashing import HSplit, VSplit, VGauge, HGauge, Text
from psutil import (
    virtual_memory,
    swap_memory,
    cpu_percent,
    sensors_temperatures,
    sensors_battery,
    disk_io_counters,
    disk_partitions,
    disk_usage
)
from time import sleep


def bytes_to_gigas(value):
    return value / 1024 / 1024 / 1024


ui = HSplit(  # ui
    HSplit(  # ui.items[0]
        VGauge(title='RAM'),  # ui.items[0].items[0]
        VGauge(title='SWAP'),  # ui.items[0].items[1]
        title='Memória',
        border_color=3
    ),
    VSplit(  # ui.items[1]
        HGauge(title='CPU %'),
        HGauge(title='CPU_0'),
        HGauge(title='CPU_1'),
        HGauge(title='CPU_2'),
        HGauge(title='CPU_3'),
        HGauge(title='CPU Temp'),
        title='CPU',
        border_color=5
    ),
    VSplit(  # ui.items[2]
        Text(
            ' ',
            title='Outros',
            border_color=4
        ),
        Text(
            ' ',
            title='Disco',
            border_color=6
        ),
    ),
)

while True:
    # Memoria
    mem_tui = ui.items[0]

    # Ram
    ram_tui = mem_tui.items[0]
    ram_tui.value = virtual_memory().percent
    ram_tui.title = f'RAM {ram_tui.value}%'

    # Swap
    swap_tui = mem_tui.items[1]
    swap_tui.value = swap_memory().percent
    swap_tui.title = f'SWAP {swap_tui.value}%'

    # CPU
    cpu_tui = ui.items[1]

    # CPU %
    cpu_percent_tui = cpu_tui.items[0]
    ps_cpu_percent = cpu_percent()
    cpu_percent_tui.value = ps_cpu_percent
    cpu_percent_tui.title = f'CPU {ps_cpu_percent}%'

    # Porcentagem dos Núcleos
    cores_tui = cpu_tui.items[1:5]
    ps_cpu_percent = cpu_percent(percpu=True)
    for i, (core, value) in enumerate(zip(cores_tui, ps_cpu_percent)):
        core.value = value
        core.title = f'CPU_{i} {value}%'

    # Temperatura do CPU
    cpu_temp_tui = cpu_tui.items[5]
    ps_cpu_temp = sensors_temperatures()['coretemp'][0]
    cpu_temp_tui.value = ps_cpu_temp.current
    cpu_temp_tui.title = f'CPU Temp {ps_cpu_temp.current}C'

    # Outros
    orther_tui = ui.items[2].items[0]
    orther_tui.text = f'Bateria {sensors_battery().percent}%'

    # Disco
    disk_tui = ui.items[2].items[1]
    partitions = disk_partitions()
    counters = disk_io_counters(perdisk=True)

    disk_tui.text = f"{'Partição':<10}{'Uso':<6}{'Lido':<6}{'Escrito'}"

    for partition in partitions:
        # Windows
        # partition_name_counter = partition.device.split('\\')[0]

        # Linux
        partition_name_counter = partition.device.split('/')[-1]

        disk_bytes = counters[partition_name_counter]

        disk_tui.text += '\n{:<10}{:<6}{:<6:.2f}{:.2f}'.format(
            partition.mountpoint,
            disk_usage(partition.mountpoint).percent,
            bytes_to_gigas(disk_bytes.read_bytes),
            bytes_to_gigas(disk_bytes.write_bytes),
        )

    try:
        ui.display()
        sleep(.5)  # Diminuir a taxa de atualização
    except KeyboardInterrupt:
        break
