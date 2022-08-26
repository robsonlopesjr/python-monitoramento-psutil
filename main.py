from dashing import HSplit, VSplit, VGauge, HGauge
from psutil import (
    virtual_memory,
    swap_memory,
    cpu_percent,
)
from time import sleep

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
        title='CPU',
        border_color=5
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

    try:
        ui.display()
        sleep(.5)  # Diminuir a taxa de atualização
    except KeyboardInterrupt:
        break
