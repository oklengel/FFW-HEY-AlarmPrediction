# FFW-HEY-AlarmPrediction
 Versuchsweise* Einsatzvorhersage für die Feuerwehr

Einsätze sind mehr oder weniger schwer vorhersehbar. Zwar steigt die Wahrscheinlichkeit einer Alarmierung wenn z.b. ein Unwetter mit 3000l/Minute vorhergesagt ist, aber um jeden Einsatz zu erfassen müsste man jede Person und jedes Objekt genaustens überwachen. Dies ist der Versuch das Bauchgefühl von "Heute könnte noch was kommen" oder "wir hatten lange nichts" zu quantifizieren.

Echte Einsatzdaten sind und bleiben unter Verschluss.

Momentan stützt sich die Vorhersage nur auf das Datum. Die Vorhersage einer Uhrzeit wird zu ungenau, die Uhrzweit hat auch Einfluss auf den Einsatztyp. Eine Implementierung von Wetterdaten spielt noch keine Rolle, da abgesehen von Unwettern, welche sich nicht vorhersehen lassen, das Wetter auf Einsätze kaum Einfluss hat. Zumindest nach der Statistik.

Ergebniss:
Mit zihmlich hoher Präzesion werden Nachbarwehren Alamiert, wenn der Algorithmus eine Einsatzwahrscheinlichkeit von mehr als 60% angibt. Für uns hat das noch nicht korrekt funktioniert. Dies liegt auch an dem Einsatztyp und der Schwere des Einsatzes. 