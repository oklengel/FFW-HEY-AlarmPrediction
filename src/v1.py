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
X_train, X_test, y_train, y_test = train_test_split(df['datum'], df['einsatz'], test_size=0.2)
text_clf.fit(X_train, y_train)
print(text_clf.score(X_test, y_test))

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

def predict_next_5_days():
    today = datetime.today()
    today.strftime("%d/%m/%Y ")
    predictions_list = []
    for i in range(5):
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

               

#predictions = 
predict_next_5_days()
#for i, date in enumerate(pd.date_range('today', periods=5)):
    #print(f"Vorhersage {date.strftime('%d.%m.%Y')}: {predictions[i]}")


#Kontrolle
'''
def predict_multiple(num_predictions):
    predictions_list = []
    for i in range(num_predictions):
        date = pd.Timestamp.now() + pd.Timedelta(minutes=2) + pd.Timedelta(seconds=np.random.randint(1, 180))
        predictions = predict_next_5_days()
        for prediction in predictions:
            datarow = [i] + prediction
            predictions_list.append(datarow)
    df = pd.DataFrame(predictions_list, columns=['id', 'datum', 'einsatzwahrscheinlichkeit_0', 'einsatzwahrscheinlichkeit_1', 'einsatzwahrscheinlichkeit_2', 'einsatzwahrscheinlichkeit_3', 'einsatzwahrscheinlichkeit_4', 'einsatzwahrscheinlichkeit_5', 'einsatzwahrscheinlichkeit_6', 'einsatzwahrscheinlichkeit_7', 'einsatzwahrscheinlichkeit_8', 'einsatzwahrscheinlichkeit_9', 'einsatzwahrscheinlichkeit_10', 'einsatzwahrscheinlichkeit_11', 'einsatzwahrscheinlichkeit_12', 'einsatzwahrscheinlichkeit_13', 'einsatzwahrscheinlichkeit_14', 'einsatzwahrscheinlichkeit_15', 'einsatzwahrscheinlichkeit_16', 'einsatzwahrscheinlichkeit_17', 'einsatzwahrscheinlichkeit_18', 'einsatzwahrscheinlichkeit_19', 'einsatzwahrscheinlichkeit_20', 'einsatzwahrscheinlichkeit_21', 'einsatzwahrscheinlichkeit_22', 'einsatzwahrscheinlichkeit_23'])
    df.to_csv('predictions.csv')


predict_multiple(10000)
'''