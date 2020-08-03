*** To jest coś, co Michał właśnie zainstalował i jest to najlepsza rzecz, jaka mnie spotkała, z wyjątkiem Michała.

** Nowa instalacja:
**** Na nowym ubuntu zainstalować:
- `sudo apt-get install git`
- `sudo apt-get install make`
- `sudo apt-get install pip3`
- `sudo apt-get install python3-venv`

**** Wejść na GitHub, skopiować kod do klonowania repozytorium. Następnie w terminalu:
- `git clone ` i wkleić url

**** Dodać aliasy
- `gedit ~/.bash_aliases`
- wpisać tam:
`alias python="python3"
alias ve="source env/bin/activate"
alias doc="cd ~/doktorat && ve"`

Przeładować terminal i potem można z dowolnego miejsca polecieniem `doc` przejść do doktoratu z aktywnym wirtualnym środowiskiem

** Wirtualne środowisko
**** Nowe biblioteki dodawać do pliku `libraries.txt` a następnie instalować polecieniem `make install`. Dzięki temu będzie dla potomności wiadomo, co jest potrzebne w projekcie

** GIT
- sprawdzenie, jakie zmiany zaszły od ostatniego wpisu: `git status`
- nowy plik `touch <nazwa_pliku>`
- zapis pliku w repozyturium: `git add <nazwa_pliku>` //  wielu plików `git add -A`
- dodanie wpisu (czyli co sie zmieniło): `git commit -m "wiadomość"`
- `git push`
- ściąganie plików z neta: `git pull`
