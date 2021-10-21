# Aufgabe
## Entwicklung einer KI für das Schach-Endspiel

Im Schachspiel ist es möglich, für Stellungen, in denen nur noch wenige
Figuren auf dem Spielfeld stehen, mit Hilfe einer sogenannten
Rückwärtsanalyse (Englisch: retrograde analysis) eine optimale Strategie zu berechnen.
Das genaue Verfahren ist grob wie folgt:

1. Zunächst wird die Menge aller möglichen zulässigen Stellungen berechnet. Diese Menge
    bezeichnen wir mit S. (Eine Stellung ist unzulässig, wenn der König des Spielers,
    der nicht am Zug ist, im Schach steht.)

2. Anschließend werden alle Stellungen aus der Menge S gesucht, in denen der Spieler, der am Zug ist,
    schachmatt ist. Diese Stellungen werden zu einer Menge S_0 zusammengefasst. Außerdem werden diese
    Stellungen aus der Menge S entfernt.

3. Nun werden alle Stellungen aus S berechnet, in denen der Spieler mit seinem nächsten Zug
   den Gegner Matt setzen kann, d.h. eine Stellung aus der Menge S_0 erreichen kann.
   Diese Stellungen werden zu einer Menge S_1 zusammen gefasst und aus der Menge S entfernt.
   S_1 enthält also alle die Stellungen, in denen der Gegner unmittelbar matt
   gesetzt werden kann.

4. Danach werden alle Stellungen aus S berechnet, in denen der Spieler, der am Zug ist,
   mit jedem seiner Züge in einer Stellung aus der Menge S_1 landet, also matt gesetzt
   werden kann.
   Diese Stellungen werden zu einer Menge S_2 zusammen gefasst und aus S entfernt.
   S_2 enthält also die Stellungen, in denen der Spieler der am Zug ist, im nächsten Zug
   matt gesetzt werden kann, unabhängig davon, wie er selber zieht.

5. Insgesamt wird eine Folge von Mengen S_n erstellt, für die folgendes gilt:
   * S_2n enthält alle die Stellungen, in denen das Spiel für den Spieler, der am Zug ist,
   spätestens nach n Zügen verloren ist.
   Konkret enthält die Menge S_2n alle die Stellungen, in denen jeder Zug, den der ziehende
   Spieler machen kann, zu einer Stellung aus einer Menge S_2k+1 führt, wobei k < n ist.
   Diese Stellungen werden aus S entfernt.

   * S_2n+1 enthält alle die Stellungen, in denen der Spieler, der am Zug ist, bei optimalem
   Spiel nach spätestens n Zügen gewinnt.
   Die Menge S_2n+1 enthält alle die Stellungen, in denen mindestens ein Zug existiert,
   der zu einer Stellung aus der Menge S_2n führt. Diese Stellungen werden aus S entfernt.

6. Das Verfahren bricht nach n+1 Schritten ab, wenn die Menge S_n leer ist. Alle dann noch
   in der Menge S verbleibenden Stellungen sind dann Stellungen, in denen keiner der Spieler
   einen Sieg erzwingen kann.

Als Ergebnis soll ein Programm erstellt werden, das die folgenden Endspiel-Situationen beherrscht:
1. König und Turm gegen König
2. König und zwei Läufer gegen König
3. König, Läufer und Springer gegen König
4. König und Bauer gegen König.

Das Programm soll mithilfe der Bibliothek

```
https://pypi.org/project/python-chess/
```

entwickelt werden. In dieser Bibliothek sind bereits die Regeln für das Schachspiel implementiert.
Diese Bibliothek liefert ebenfalls eine GUI für das Spiel.

Das Programm soll als Jupyter Notebook implementiert werden.

Dieses Thema kann von 2 Studierenden bearbeitet werden.

Erforderliche Vorkenntnisse: Gute Kenntnissen in Python und Jupyter Notebooks.