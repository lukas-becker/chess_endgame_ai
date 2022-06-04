# Künstliche Intelligenz für das Schach-Endspiel

Im Schachspiel ist es möglich, für Stellungen, in denen nur noch wenige Figuren auf dem Spielfeld stehen, mithilfe einer
sogenannten Rückwärtsanalyse eine optimale Strategie zu berechnen.

## Ordnerstruktur

| Name          | Beschreibung                                                                              |
|---------------|-------------------------------------------------------------------------------------------|
| gaviota       | Die heruntergeladenen Gaviota-Tabellen für den Vergleich.                                 |
| Images        | Der Ordner, in dem die Stockfish-Installation liegt.                                      |
| Played_Games* | Alle Spiele mit deren Spielzüge, die gegen die KI bisher gespielt worden sind             |
| S_n_Results*  | Die $S_n$ Mengen lokal in Dateien für die unterschiedlichen Spielsituationen gespeichert. |
| stockfish     | Der Ordner, in dem die Stockfish-Installation liegt.                                      |
| syzygy        | Die heruntergeladenen Syzygy-Tabellen für den Vergleich.                                  |
| Tests*        | Alle Tests, die bisher unter Verwendung der Stockfish-Engine durchgeführt worden sind.    |

\* Diese Ordner müssen gegebenenfalls noch von dem Anwender erstellt werden.

## Aufgabenstellung

### Ziel: Entwicklung einer Schach KI für vordefinierte Endspiel-Situationen

Beim Schach ist es für bestimmte Situationen möglich eine optimale Spielstrategie zu berechnen. Hierfür dürfen nur noch
wenige Spielfiguren auf dem Spielfeld vorhanden sein. Die Berechnung kann mit einer sogenannten Rückwärtsanalyse (eng.:
retrograde analysis) durchgeführt werden. Das Ziel dieses Repositories liegt in der Implementierung einer künstlichen
Intelligenz, die am Ende dazu in der Lage ist für folgende Spielsituationen eine optimale Spielstrategie zu berechnen:

1. König und Dame gegen König
2. König und Turm gegen König
3. König und zwei Läufer gegen König
4. König, Läufer und Springer gegen König
5. König und Bauer gegen König

## Schnellstart

### Installation mit Anaconda

1. Erstellen einer neuen virtuellen Umgebung ``chess`` mit dem Befehl ``conda create -n chess``
2. Aktivieren der virtuellen Umgebung mit ``conda activate chess``
3. Installieren von Jupyter Notebook durch ``conda install -c anaconda jupyter``
4. Installieren der restlichen benötigten Packages mit ``pip install -r requirements.txt``

### Optional

Sofern das Testen der KI ebenfalls verwendet werden möchte, wird eine Installation der Stockfish-Engine benötigt. Die
gelingt mit folgenden Schritten:

1. Engine auf der offiziellen [Projektseite](https://stockfishchess.org/download/) herunterladen.
2. Entpacken der heruntergeladenen Datei nach `\stockfish`.
3. Umbenennen der stockfish_xxx.exe Datei in stockfish.exe.

Für weitere Vergleiche werden zusätzlich gaviota-Tabellen benötigt. 
Die Einrichtung kann in insgesamt zwei Schritten erfolgen.

1. Die erwünschten gaviota-Tabellen von der [Projektseite](https://chess.cygnitec.com/tablebases/gaviota/) herunterladen.
2. Die Tabellen in dem Ordner `\gaviota` hinterlegen.

Gleichermaßen können auch die syzygy-Tabellen für eine weitere Vergleichsmethode heruntergeladen werden:

1. Die erwünschten syzygy-Tabellen von der [Projektseite](https://syzygy-tables.info/) herunterladen.
2. Die Tabellen in dem Ordner `\syzygy` hinterlegen.

#### Alternative

Unter diesem [Link](https://drive.google.com/file/d/1AwMUGTEsFGLw5NCMUP9eLcU7BZlbnhql/view?usp=drivesdk) werden alle notwendigen Endspieltabellen und Engines für die Nutzung dieses Repositories bereitgestellt.

### Ausführen der Notebooks

1. Aktivieren der virtuellen Umgebung mit ``conda acctivate chess``
2. Aufrufen von Jupyter Notebook mit ``jupyter notebook``
3. Ausführen der Notebooks in Reihenfolge der Nummerierung
4. Nach der Bearbeitung beenden der virtuellen Umgebung mit ``conda deactivate``

