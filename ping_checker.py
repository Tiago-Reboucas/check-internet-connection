import subprocess
import time
from datetime import datetime
import signal

# ========================== EDIT HERE ==========================
# English    - 'en'
# Brasileiro - 'br'
lang = 'en'

file_name = 'ping_log.csv' # File to be save in local drive
host = '8.8.8.8'           # Website or ip to test your ping
delay = 1                  # Time between tests (seconds)
threshold = 100            # Minimun acceptable ping value
lag = 150                  # Ping value where the 'lag' starts
unreachable = 5000         # Value to be used if couldn't reach destination
# ================================================================

# Groups
if lang == 'br':
    a = f'Aceitável ({threshold}-{lag})'
    b = f'Lag (>{lag})'
    c = 'Inacessível (>5000)'
else:
    a = f'Acceptable ({threshold}-{lag})'
    b = f'Lag (>{lag})'
    c = f'Unreachable (>{unreachable})'

# Handle exit signal
def handler(signum, frame):
    while True:
        if lang == 'br': sure = input('Tem certeza que deseja sair (s/n)? ').lower()
        else: sure = input('Are you sure you want to quit (y/n)? ').lower()

        if sure == 'y' or sure == 's': quit()
        elif sure == 'n': break
        else: continue   

signal.signal(signal.SIGINT, handler)


def time_now(lang:str):
    now = datetime.now()
    date = str(now.date())
    hour = now.strftime('%H:%M:%S')

    if lang == 'br':
        date = now.strftime('%d/%m/%Y')
        now = str(datetime.strptime(date+hour, '%d/%m/%Y%H:%M:%S'))
        return now, date, hour

    now = str(datetime.strptime(date+hour, '%Y-%m-%d%H:%M:%S'))

    return now, date, hour


def save_log(group:str, value:int):
    global location, lang, unreachable

    now, date, hour = time_now('en')
    write_data('\n{},{},{},{},{},{}'.format(now, date, hour, location, value, group))

    now, date, hour = time_now(lang)

    if value == unreachable:
        if lang == 'br': print(f"{date} {hour} - Tempo limite esgotado ou não conseguiu chegar ao destino.")
        else: print(now + " - Timeout or destination unreachable.")
    else:
        if lang == 'br': print('{} {} - Variação de ping : {}ms.'.format(date, hour, value))
        else: print('{} - Ping variation: {}ms.'.format(now, value))


def ping(host:str, delay:float, threshold:int, lag:int):
    global lang

    output = None
    group = None
    try:
        output = str(subprocess.check_output('ping -n 1 {}'.format(host), shell=True))[1:]
    except:
        group = c
        value = unreachable
        save_log(group, value)
        time.sleep(delay)
        return
    
    init = output.rfind(' ') + 1
    end = output.rfind('\\r') - 2
    try:
        value = int(output[init:end])
    except:
        group = c
        value = unreachable
    
    if group is None:
        if threshold <= value <= lag: group = a
        elif value > lag: group = b
    
    if value >= threshold:
        save_log(group, value)

    time.sleep(delay)


def check_locations():
    first = True
    loc = list()
    for line in f_handler:
        if first: first = False
        else:
            line_loc = line.split(',')[3].capitalize()
            if line_loc not in loc:
                loc.append(line_loc)

    if loc == [] or loc == ['']:
        if lang == 'br': print('Não há registro de "Local".\n')
        else: print('There are no "Location" records.\n')
    else:
        loc.sort()
        word_size = 30

        if lang == 'br': full_str = 'Estes são os locais em seu arquivo:\n'
        else: full_str = 'Those are the locations in the local file:\n'

        i = 0
        for l in loc:
            full_str += f'"{l[:word_size]}"'
            full_str += (word_size - len(l)) * ' ' if len(l) < word_size else ''
            full_str += '  '
            i += 1

            if i == 3: full_str += '\n'

        print(full_str + '\n')


def write_data(data:str):
    global file_name

    with open(file_name, mode='at') as file:
        file.write(data)


try:
    f_handler = open(file_name)
    check_locations()
except:
    if lang == 'br':
        write_data('DataHora,Data,Hora,Local,Ping,Grupo')
        print(f'Criado arquivo "{file_name}".')
        print('Não há registro de "Local".\n')
    else:
        write_data('DateTime,Date,Time,Location,Ping,Group')
        print(f'Created "{file_name}" file.')
        print('There are no "Location" records.\n')

if lang == 'br': location = input("Insira seu local: ").strip()
else: location = input("Insert your location: ").strip()

while True:
    ping(host, delay, threshold, lag)
