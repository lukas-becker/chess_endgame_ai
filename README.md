# Künstliche Intelligenz für das Schach-Endspiel

Im Schachspiel ist es möglich, für Stellungen, in denen nur noch wenige
Figuren auf dem Spielfeld stehen, mithilfe einer sogenannten
Rückwärtsanalyse eine optimale Strategie zu berechnen.

## Schnellstart
### Installation mit Anaconda
1. Erstellen einer neuen virtuellen Umgebung ``chess`` mit dem Befehl ``conda create -n chess``
2. Aktivieren der virtuellen Umgebung mit ``conda activate chess``
3. Installieren von Jupyter Notebook durch ``conda install -c anaconda jupyter``
4. Installieren der restlichen benötigten Packages mit ``pip install -r requirements.txt``

### Optional
Sofern das Testen der KI ebenfalls verwendet werden möchte, wird eine Installation der Stockfish-Engine benötigt. Die gelingt mit folgenden Schritten:
1. Engine auf der offiziellen [Projektseite](https://stockfishchess.org/download/) herunterladen.
2. Entpacken der heruntergeladenen Datei nach /stockfish
3. Umbennen der stockfish_x_x... Datei in stockfish.exe

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
