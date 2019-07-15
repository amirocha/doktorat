Projekt o UV - redukcja danych
/źródła: Serpens SMM1 i SMM34, B1b, NGC1333 I2A i I4AB
/linie: HCN(1-0), CN(F1)(1-0), CS(3-2), C34S(3-2), H13CN(1-0), H13CN(2-1)
/surowe dane = spectraOdp.30m
/środek: RA = 18:29:49.6 DEC = 01:15:20.5


### REDUKCJA ###

1) obejrzeć widma "ręcznie", wpisując komendy w CLASSie:
>file in [surowe dane]
>find /all

>list /toc  - podejrzenie danych (opcjonalne)

>set source [źródło]   \\wg nazw z 'list toc'
>set line [linia]
>find /all

>average /nocheck    - uświednia widmo
>plot

/jeśli się nie uśrednia: -sprawdzić, czy komendy wpisane poprawnie (pamiętać o 'find /all'   - dla niektórych linii trzeba zawęzić zakres częstotliwości do uśredniania możliwie dużo wokół częstotliwości danej linii

Na uśrednionym widmie często są spiki (pionowe linie - błędy instrumentalne). Należy znaleźć nr "zepsutego" kanału i go usunąć.
>set unit c - zmiana jednostek osi X na kanały
>plot  /lub 'p'
>set mode x [początkowy kanał] [kanał końcowy] - zoom na część widma w tym zakresie  // podobnie działa >set mode y 
>plot
>draw kill [nr zepsutego kanału]
>p
>set mode x tot - odzoomowanie
 
czynność powtarzamy, aż do momentu, gdy widmo wyda się dobre (kwestia dość uznaniowa, ale zbyt dokładne czyszczenie psuje mapy końcowe)
"zepsute" kanały wpisujemy w plik redukcyjny w miejsca 'draw kill' i 'draw fill' (opis poniżej).

Uruchamianie skryptu .class
>@[nazwa skryptu]


2) Plik redukcyjny:
map_red_[źródło]_[molekuła].class
- wejście: surowe dane /zmodyfikować ścieżkę
- skrypt Larsa
- modyfikacja źródła (w 3 miejscach!!) i linii oraz nazwy pliku wynikowego
- dopasowuje dane z dwóch obszarów (SMM1 i SMM34): trik z let l_new lambda*12/pi
- pamiętać o zmianie wiązki wg tabelki na dole
- wpisać ręcznie draw kill i draw fill (numery zepsutych kanałów)
- możliwość wykonania mapki lmv (odkomentować !table serpens_cs32 new !xy_map serpens_cs32)
- wyjście: [źródło]_[molekuła]_red.30m

jeśli linia jest nie uśrednia się prawidłowo (błąd: index is inconsistent), należy zawęzić częstotliwość lub spróbować uśredniać z opcją /res

!!!Opcja:
Pliki CO z APEXa wydają się być poredukowane, ale mają zły poziom kontinuum. Do redukcji tych danych wystarczy plik map_red_serpens_co.class ze zmianą pliku wejściowego (różne molekuły) i wyjściowego. Ten skrypt dopasowuje tylko kontinuum do każdego skanu. W przypadku C18O najlepiej zadziałała opcja "base 2".


### KONWOLUCJA ###
Przy konwolucji traktuje się mapę HCN 1-0 jako referencyjną.

1) Trzeba sprawdzić jaka jest rozdzielczość przestrzenna dla HCN 1-0
(ang. spatial resulution)

W tym celu należy otworzyć zredukowany plik HCN 1-0:

LAS> file in [źródło]_hcn10_red.30m
LAS> find /all

Potem wpisujemy komendę:

LAS> let map%reso 0

Narazie została wpisana wartość zero bo to mapa referencyjna.

2) Tworzenie mapę LMV:

LAS> table [źródło]_hcn10_conv_tab new
LAS> xy_map [źródło]_hcn10_conv_tab new

Po komendzie XY_MAP pojawi się lista z różnymi wartościami, m.in.
rozmiar piksela, beamu oraz
to czego potrzebujemy, czyli spatial resolution. W tym przypadku wynosi
29.3".

3) Jak już wartość spatial resolution jest znana to możemy usunąć
wszystkie powstałe
pliki przy okazji tworzenia mapy LMV, czyli plik .lmv, .tab, .wei.


TERAZ PORA NA ZASADNICZĄ KONWOLUCJĘ. Poprzednie kroki trzeba powórzyć,
ale tym razem
zamiast RESO 0 wpisujemy wartość spatial resolution.

1) Wczytujemy ponownie zredukowany plik HCN 1-0:

LAS> file in [źródło]_hcn10_red
LAS> find /all

TUTAJ POJAWIA SIĘ ZMIANA Z 0 na 29.3:

LAS> let map%reso 29.3

------------
!!!Ważne!!!!
Jeśli chcemy porównywać mapy - dzielić flux lub nakładać je na siebie mapę referencyjną robimy normalnie, a w tej, którą chcemy dopasować, należy dopisać:
let map%like <mapa_referencyjne_conv_tab.lmv>
------------

2) Tworzymy mapę LMV:

LAS> table [źródło]_hcn10_conv_tab new
LAS> xy_map [źródło]_hcn10_conv_tab new

3) Zapisujemy dane do pliku .30m:

LAS> file out [źródło]_hcn10_conv.30m s
LAS> lmv [źródło]_hcn10_conv_tab


I to cała konwolucja. Można teraz wczytać plik po konwolucji:

LAS> file in [źródło]_hcn10_conv.30m
LAS> find/all

Dla HCN 1-0 w Serpensie powinien znaleźć 541 obserwacji!

W przypadku innych molekuł kroki są takie same, ale nie musisz już
powtarzać etapu 1-go
ze sprawdzaniem spatial resolution, a od razu dajesz let map%reso 29.3 i
kontynuujesz resztę.

Dla niektórych molekuł tj. C34S 3-2 oraz H13CN 1-0 o komendzie table ...
pojawia się problem
tzw. "index consistency".

Udało mi się naprawić ten problem przez usunięcie kilku skanów ze
zredukowane pliku
przed rozpoczęciem konwolucji tj. przed LET MAP%RESO, używając komendy DROP:

Z tego co pamiętam to DROP usuwa pojedynczą obserwację (np. drop 1609).
Usunięte obserwacje/skany to:

1609-1620
3223-3230
dla Serpensa!



### MAPKI ###


1) wczytujemy plik z daną linią i źródłem po konwolucji 
>file in [źródło]_[molekuła]_conv.30m
LAS> find /all

uśrednianie widma
>average /nocheck /weight equal
/po konwolucji CLASS pogubił trochę informacji i nie chciał uśredniać profili przy użyciu AVERAGE /NOCHECK. Okazuje się, że CLASS uśrednia dane na kilka sposobów i domyślnie jest TIME. Po konwolucji działa tylko EQUAL.
>p

Jeśli widać spiki, zawęzić obszar komendą 'set mode x' (najpierw set unit v)
> zawęzić okno komendą 'set window -50 50' (lub inny zakres w zależności, gdzie mamy emisję)

>base 0 - dopasowanie continuum (linia prosta) /można tez wyższego rzędu base 1, itp.

spisujemy wartość rms i wkopiujemy do pliku [źródło]_[molekuła]_3sigma.py (wiersz 28)

2) wyciągamy uśrednione widmo na zewnątrz CLASSa za pomocą skrypt class2ascii.class (przy zakomentowanym 'set range' i 'smooth').
- jeśli zawężaliśmy w poprzednim kroku, w kodzie trzeba zmienić 'set mode x tot' na zadany wcześniej zakres
- zmieniamy plik wynikowy [źródło]_[molekuła]_ave_spec.txt

3) W pliku [źródło]_[molekuła]_3sigma.py:
- w linii 32 oraz 125 (tam, gdzie zczytuje dane) podmieniamy nazwę pliku na [źródło]_[molekuła]_ave_spec.txt
- zmieniamy nazwę pliku wynikowego (linia 14)
- wykonaj plik: python3 [źródło]_[molekuła]_3sigma.py
- przejrzyj wynikowy eps
- po pierwszym odpaleniu skryptu wartości 3sigma (czerowne linie) i 1sigma (zielone linie) będą w złym miejscu. Na podstawie rysunku, zmień zakres w kodzie [źródło]_[molekuła]_3sigma.py (linie 36 i 67)
- wykonaj plik ponownie

4) W terminalu pojawią się zakresy 3sigma (x1 i x2) oraz 1sigma (x3 i x4). W zależności od potrzeb wpisujemy je w ostatnią linię skryptu resample_ave_spec_3sigma.class po komendzie 'print area':
- odkomentować tę linię
- zmienić nazwę pliku wyjściowego [źródło]_[molekuła]_int.txt
- zmienić nazwę pliku wejściowego [źródło]_[molekuła]_conv
- ewentualnie zmienić 'set window' do zakresu 3 sigma
- zmienić 'let NX' na odpowiednią wartość wg komentarza
- upewnić się, że 'set range' jest zakomentowane (bo mapujemy całość)

!!!Opcja:
4a) w przypadku map w CO z APEXa występują dodatkowe dane wysoko nad naszym obiektem. Prawdopodobnie jest to jakiś błąd instrumentalny. Aby usunąć dodatkowe dane, należy zastosować skrypt CO_printarea_corrections.py:
- zmienić nazwę pliku wejściowego [źródło]_[molekuła]_int.txt
- zmienić nazwę pliku wyjściowego [źródło]_[molekuła]_cut.txt
dalej postępujemy z plikiem "*_cut.txt" tak jakby był "*_int.txt"


5) plik map_[molekuła]_positions.class:
- zmienić nazwę pliku wejściowego w liniach 25 i 32 (greg\column x 2 y 3 z 4 /file [źródło]_[molekuła]_int.txt)
- zmienić tytuł mapy np. greg\draw text 80 230 "NGC1333 HCN J=1-0"
- zmienić nazwę pliku wyściowego [źródło]_[molekuła].eps w dwóch ostatnich liniach
- wykonać skrypt w CLASSie
- sprawdzić obrazek i można wtedy regulować zakresy konturów, zmieniając 'let up [numer]' (wiersz 5)
- można dodać nazwy i pozycje protogwiazd i wypływów
- zmiana umiejscowienia tytułu = linia 'greg\draw text 80 230 "NGC1333 HCN J=1-0"' + manewrowanie cyframi


### WIDMA ###

Znająć pozycję źródła i zakres wiązki dla danej molekuły, możemy wyciągnąć uśrednione widmo z danej pozycji.

1) class2ascii.class:
- zmienić nazwę pliku wejściowego [źródło]_[molekuła]_conv
- odkomentowujemy 'set range' i wpisujemy pozycje źródła. Format: x1 x2 y1 y2
- zmienić nazwę pliku wyjściowego [źródło]_[molekuła]_[pozycja].txt
- zmienić 'let NX' zgodnie z opisem (linia 30)
- dla molekuły H13CN(2-1) odkomentowujemy także 'smooth'

2) do wykonania skryptu serpens_1-7_ave_spectra_vel_resam.py potrzebujemy 7 pozycji we wszystkich molekułach (poza H13CN(2-1))



NOTATKI:
- NGC1333 nie uśrednia się linia C32S(3-2) -> należy odkomentować 'set 146916 147022'
- NGC1333 linia H13CN(1-0) spiki na środku emisji - widmo nie nadaje się do obróbki


