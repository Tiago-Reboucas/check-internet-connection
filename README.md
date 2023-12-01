# Checar Conexão de Internet

Uma historinha interessante para se entreter:

Imagine que você contratou "aquela" internet que você diz: "Agora sim vou ter uma internet arretada, vai ser um '*ping*' baixo e alta velocidade!". Você está empolgado que vai ter uma internet que não vai dar lag e poder jogar, assistir filme, fazer vídeo-chamada e tudo mais!

Aí eles instalam tudo bonitinho e você vai testar em um jogo, a animação está nas alturas e você não consegue se controlar mais! Quando se conecta no servidor e entra na partida o '*ping*' está ótimo e você sente uma diferença grande da sua internet antiga. Mas aí seu personagem 'patina' no chão e os adversários se teletransportam ao seu redor... Tudo bem, pode acontecer de vez em quando... Mas isso se repete e se repete, a um ponto que acontece pelo menos 5 vezes por minuto... chato né?

Nesses momentos você tem perda de pacote e o '*ping*' vai lá para cima, algo está muito errado com sua conexão. Depois da assistência técnica ter passado mil e uma instruções por telefone, ter feito mais de uma visita para trocar modem, verificar cabos e poste, o problema ainda persiste.

Poderia ser que o sinal da provedora já estivesse vindo com interferência e sem estabilidade. Neste ponto você pensa: "Vou fazer um programa para verificar o '*ping*' a cada segundo e mostrar um '*log*' da data e hora que aconteceram os momentos da variação do '*ping*'", como qualquer pessoa normal faria. Depois de mostrar o '*log*' para a assistência técnica eles dizem que não fazem qualquer tipo de verificação de sinal em tempo real e que nada mais poderiam fazer por mim... :neutral_face:

Foi triste... cancela esse contrato e faz com uma nova provedora :wink:

### Funcionalidade
Este programa verifica o '*ping*' a cada segundo e salva um '*log*' com as informações de data, hora, local, ping e grupo de aceitação.

### Módulos necessários
- subprocess
- time
- datetime
- signal

### Como usar
- Abra com seu editor o `ping_checker.py`, das linhas 9 a 16 é onde você pode editar:
    - `lang`: língua de exibição do programa, `'en'` para Inglês e `'br'` para Português Brasileiro;
    - `file_name`: nome do arquivo a ser salvo na pasta (com a devida extensão - padrão: '.csv');
    - `host`: website ou IP para testar o '*ping*' (deve ser um site com conexão confiável);
    - `delay`: tempo entre testes de '*ping* (segundos);
    - `threshold`: limite mínimo de aceitação de '*ping*';
    - `lag`: limite máximo de aceitação de '*ping*' (valor em que começa a apresentar lag);
    - `unreachable`: valor para ser usado quando não conseguir alcançar o destino ou tempo limite excedido.

- Depois de editado, rode `ping_checker.py`;
- Se já tiver um arquivo '*log*', o programa irá exibir as localidade que o programa já fora usado;
- Caso seja a primeira vez, um arquivo '.csv' será criado na mesma pasta do executável;
- Será requisitado que insira seu local (para o caso de teste em diferentes localidades);
- O programa irá ler o ping com o `host` em tempo real;
- Quando for identificado um valor acima do `threshold`, será exibido na tela a **data**, **hora** e o '***ping***';
- Todos os dados serão salvos no formato: 'DataHora,Data,Hora,Local,Ping,Grupo' (para fácil uso em análise de dados).

OBS: pressione <Ctrl+C> para pausar.

---

# Check Internet Connection

An interesting story to keep you entertained:

Imagine that you contracted "that" internet and you say: "Now I'm gonna have lightspeed internet, it'll have low '*ping*' and high speed!". You're excited that you'll have an internet that won't lag and be able to play games, watch movies, make video calls and everything else!

Then they install everything beautifully and you go to test it in a game, the excitement goes through the roof and you can't control yourself anymore! When you connect to the server and enter the game the '*ping*' is great and you feel a big difference from your old internet. But then your character 'slides' on the ground and opponents teleport around you... Okay, it can happen from time to time... But this repeats itself over and over to a point where it happens at least 5 times per minute... frustrating, right?

In these moments you experience package loss and the '*ping*' tilt up, something is very wrong with your connection. After technical assistance gave a thousand instructions over the phone, made more than one visit to change the modem, check cables and poles, the problem still persists.

It could be that the provider's signal was already coming with interference and no stability. At this point you think: "I'm going to write a program to check the '*ping*' every second and show a '*log*' of the date and time when the '*ping*' variation occurred", like any normal person would do. After showing the '*log*' to the technical support they say that they don't do any type of signal check in real time and that they couldn't do anything else for me... :neutral_face:

So... move on... cancel that contract and do it with a new provider :wink:

### Functionality
This program checks the '*ping*' every second and saves a '*log*' with date, time, location, ping and acceptance group information.

### Required modules
- subprocess
- time
- datetime
- signal

### How to use
- Open `ping_checker.py` with your editor, you can edit from lines 9 to 16:
    - `lang`: program display language, `'en'` for English and `'br'` for Brazilian Portuguese;
    - `file_name`: name of the file to be saved in the folder (with the appropriate extension - default: '.csv');
    - `host`: website or IP to test '*ping*' (must be a website with a reliable connection);
    - `delay`: time between '*ping* tests (seconds);
    - `threshold`: minimum acceptance limit for '*ping*';
    - `lag`: maximum acceptance limit for '*ping*' (value at which lag begins);
    - `unreachable`: value to be used when unable to reach the destination or timeout.

- After editing, run `ping_checker.py`;
- If you already have a '*log*' file, the program will display the locations that the program has already used;
- If it is the first time, a '.csv' file will be created in the same folder as the executable;
- You will be asked to enter your location (in case of testing in different locations);
- The program will read the ping from the `host` in real time;
- When a value above the `threshold` is identified, the **date**, **time** and '***ping***' will be displayed on the screen;
- All data will be saved in the format: 'DateTime,Date,Time,Location,Ping,Group' (for easy use in data analysis).

OBS: press <Ctrl+C> to pause.
