import pandas as pd
import numpy as np
from datetime import datetime,timedelta
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

# Daten einlesen
df = pd.read_csv('data.csv', delimiter=';')

# Liste für Vorhersagen
predictions_list = []

# Daten aufbereiten
df['datum'] = pd.to_datetime(df['datum'], format='%d.%m.%Y')
df['datum'] = df['datum'].apply(lambda x: x.strftime("%d.%m.%Y"))

df['einsatz'] = df['einsatz'].astype(str)

# Feature-Extraction und Modellierung
text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('clf', LogisticRegression())
])

# Training und Testen des Modells
X_train, X_test, y_train, y_test = train_test_split(df['datum'], df['einsatz'], test_size=0.4)
text_clf.fit(X_train, y_train)
print("Score:" + str(text_clf.score(X_test, y_test)))

# Vorhersagefunktion
def get_possible_times(date):
   # pred = text_clf.predict_proba(pd.Series(date))[0]
    pred = text_clf.predict_proba(pd.Series(date.strftime('%Y-%m-%d %H:%M:%S')))[0]

    times = pd.date_range(date, periods=24*60, freq='T')
    result = {}
    for idx, p in enumerate(pred):
        time = times[idx]
        hour, minute = time.hour, time.minute
        result[f'{hour}:{minute:02d}'] = p
    return result

def predict_next_14_days():
    today = datetime.today()
    today.strftime("%d/%m/%Y ")
    predictions_list = []
    for i in range(14):
        date = today + timedelta(days=i)
        print(f'Vorhersage {date.strftime("%d.%m.%Y")}:')
        times = get_possible_times(date)
        highest_prob = max(times.values())
        datarow = [date.strftime("%d.%m.%Y")]
        for time, prob in times.items():
            if prob == highest_prob:
                prob_percent = round(prob * 100, 2)
                print(f'{prob_percent}% Einsatzwahrscheinlichkeit ')
                datarow.append(prob_percent)
        predictions_list.append(datarow)
    return predictions_list

predict_next_14_days()

