# Künstliche Intelligenz für das Schach-Endspiel

Im Schachspiel ist es möglich, für Stellungen, in denen nur noch wenige Figuren auf dem Spielfeld stehen, mithilfe einer
sogenannten Rückwärtsanalyse eine optimale Strategie zu berechnen.

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
2. Entpacken der heruntergeladenen Datei nach /stockfish
3. Umbenennen der stockfish_xxx.exe Datei in stockfish.exe

### Ausführen der Notebooks

1. Aktivieren der virtuellen Umgebung mit ``conda acctivate chess``
2. Aufrufen von Jupyter Notebook mit ``jupyter notebook``
3. Ausführen der Notebooks in Reihenfolge der Nummerierung
4. Nach der Bearbeitung beenden der virtuellen Umgebung mit ``conda deactivate``

## Ordnerstruktur

| Name         | Beschreibung                                                                                    |
|--------------|-------------------------------------------------------------------------------------------------|
| Played_Games | Alle Spiele mit deren Spielzüge, die gegen die KI bisher gespielt worden sind                   |
| S_n_Results  | Die $S_n$ Mengen lokal in Dateien für die unterschiedlichen Spielsituationen gespeichert.       |
| stockfish    | Der Ordner, in dem die Stockfish-Installation liegt.                                            |
| Tests        | Alle Tests, die bisher unter Verwendung der Stockfish-Engine durchgeführt worden sind.          |
| Util         | Ergänzende Notebooks, die grundlegende Funktionen und Importe für alle Notebooks bereitstellen. |

## Aufgabenstellung

### Ziel: Entwicklung einer Schach KI für vordefinierte Endspiel-Situationen

Beim Schach ist es für bestimmte Situationen möglich eine optimale Spielstrategie zu berechnen. Hierfür dürfen nur noch
wenige Spielfiguren auf dem Spielfeld vorhanden sein. Die Berechnung kann mit einer sogenannten Rückwärtsanalyse (eng.:
retrograde analysis) durchgeführt werden. Das Ziel dieses Repositories liegt in der implementierung einer künstlichen
Intelligenz, die am Ende dazu in der Lage ist für folgende Spielsituationen eine optimale Spielstrategie zu berechnen:

1. König und Dame gegen König
2. König und Turm gegen König
3. König und zwei Läufer gegen König
4. König, Läufer und Springer gegen König
5. König und Bauer gegen König

### Beschreibung der retrograde analysis

Da im Fokus der Implementierung die retrograde analysis steht, wird dieses hier kurz aufgeführt:

1. Zu Beginn werden alle zulässigen Stellungen für eine ausgewählte Spielsituation berechnet. Diese Menge an Stellungen
   werden als Menge S bezeichnet. Hierbei handelt es sich dann um eine zulässige Stellung, wenn der König des Spielers,
   der nicht am Zug ist, im Schach steht.
2. Als Nächstes werden alle Spielsituationen herausgesucht aus der Menge S herausgesucht, bei der der Spieler, der am
   Zug ist, schachmatt gestellt wurde. Für den Rahmen dieser Arbeit sind demnach nur die Stellungen interessant, bei
   denen der gegnerische König schachmatt ist. Diese Stellungen werden in der Menge S_0 zusammengefasst und aus der
   Menge S entfernt.
3. Der nächste Schritt bestimmt alle Stellungen aus S, in denen der Spieler den gegnerischen Spieler schachmatt setzen
   kann. Das bedeutet, dass von dieser Spielsituation aus mit einem Zug eine Stellung aus der Menge S_0 erreicht werden
   kann. Diese Situationen bezeichnen wir als S_1. Die Menge S_1 wird ebenfalls aus der Menge S entfernt.
4. Danach werden alle Spielsituationen berechnet, in denen der Spieler, der am Zug ist, mit seinem nächsten Zug in der
   Menge S_1 landet, also er selbst schachmatt gesetzt werden kann. Diese Stellungen werden als die Menge S_2 bezeichnet
   und aus der Menge S herausgenommen.
5. Durch die andauernde Wiederholung des Schrittes 4. wird eine Folge von Mengen S_n erstellt, für die folgende
   Regelungen gelten:
    * Für Stellungen aus den Mengen S_2n gilt: <br/>
      Diese Menge enthält alle Stellungen, in denen der Spieler, der gerade am Zug ist, nach spätestens n Zügen verloren
      hat. In diesem Fall würden hier alle Stellungen landen, bei denen der König am Zug ist. Dabei gilt zusätzlich,
      dass nach jedem Zug aus der Stellung S_2n in einer Stellung S_2k+1 landet, wobei k < n gilt.
    * Für Stellungen aus den Mengen S_2n+1 gilt: <br/>
      In dieser Menge sind alle Spielsituationen enthalten in denen der Spieler, der am Zug ist, mit einer optimalen
      Spielweise nach n Zügen gewinnt. Bei den Szenarien handelt es sich hierbei um die Farbe, die mehr als nur einen
      König mehr auf dem Spielfeld stehen haben. Bei diesen Stellungen führt mindestens ein Zug in eine Spielsituation
      S_2n.

   Die Spielsituationen, die in den Mengen S_2n und S_2n+1 landen, werden aus der Menge S entfernt.
6. Das Verfahren wird nach n+1 Schritten beendet, sobald die Menge S_n leer ist. Bei den übrigen Stellungen, die in der
   Menge S verblieben sind, handelt es sich um Spielsituationen, in denen keiner der Spieler einen Sieg erzwingen kann.
