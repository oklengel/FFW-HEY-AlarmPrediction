# FFW-HEY-AlarmPrediction
 Versuchsweise Einsatzvorhersage für die Feuerwehr

Einsätze sind mehr oder weniger schwer vorhersehbar. Zwar steigt die Wahrscheinlichkeit einer Alarmierung wenn z.b. ein Unwetter mit 3000l/Minute vorhergesagt ist, aber um jeden Einsatz zu erfassen müsste man jede Person und jedes Objekt genaustens überwachen. Dies ist der Versuch das Bauchgefühl von "Heute könnte noch was kommen" oder "wir hatten lange nichts" zu quantifizieren.

Echte Einsatzdaten sind und bleiben unter Verschluss.

Momentan stützt sich die Vorhersage nur auf das Datum. Die Vorhersage einer Uhrzeit wird zu ungenau, die Uhrzweit hat auch Einfluss auf den Einsatztyp. Eine Implementierung von Wetterdaten spielt noch keine Rolle, da abgesehen von Unwettern, welche sich nicht vorhersehen lassen, das Wetter auf Einsätze kaum Einfluss hat. Zumindest nach der Statistik.

Ergebnisse:

Mit ziemlich hoher Präzession werden Nachbarwehren alarmiert, wenn der Algorithmus eine Einsatzwahrscheinlichkeit von mehr als 60 % angibt. Ob wir alamiert werden hängt von der schwere und des Ortes des Einsatzes ab. Sollten für eine Reihe von Vohersagen die Werte allesamt im Bereich <>9% legen und die Daten aber heterogen sind, v1.py erneut ausführen. 

Es ist zu beachten das dieses Programm für eine kleine FFW geschrieben wurde, welche 24-33 Einsätze pro Jahr hat. Für Größere Wehren bzw. Einsatzgebiete mit 10 Einsätzen pro Tag wird dieses Script nicht unbedingt funktionieren.