#generates fake data for prediction since real data is not avilible.

import csv
import random

import csv
import random
import argparse

def generate_einsatzmeldung():
    einsatzmeldungen = ["Brand", "Verkehrsunfall", "Baum auf Straße", "Überschwemmung"]
    return random.choice(einsatzmeldungen)

def generate_uhrzeit():
    stunden = random.randint(0, 23)
    minuten = random.randint(0, 59)
    return "{:02d}:{:02d}".format(stunden, minuten)

def generate_temperatur():
    min_temp = -20
    max_temp = 40
    return "{} - {}".format(random.randint(min_temp, max_temp), random.randint(min_temp, max_temp))

def generate_wetter():
    wetterbedingungen = ["sonnig", "bewölkt", "regnerisch", "windig"]
    return random.choice(wetterbedingungen)

def generate_ort():
    orte = ["Berlin", "Hamburg", "München", "Köln", "Frankfurt", "Stuttgart", "Düsseldorf", "Dortmund", "Essen", "Leipzig"]
    return random.choice(orte)

def generate_besonderheit():
    besonderheiten = ["Chef im Uhrlaub", "Stromabschaltung für nächsten Tag gemeldet", "Unwetterwarnung","",]
    return random.choice(besonderheiten)

def generate_fake_data(num_rows):
    with open("fake_data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["Einsatzmeldung", "Datum", "Uhrzeit", "Wetter", "Temperatur", "Ort", "Besonderheit"])
        for i in range(num_rows):
            einsatzmeldung = generate_einsatzmeldung()
            datum = "2023-04-03"
            uhrzeit = generate_uhrzeit()
            wetter = generate_wetter()
            temperatur = generate_temperatur()
            ort = generate_ort()
            besonderheit = generate_besonderheit()
            writer.writerow([einsatzmeldung, datum, uhrzeit, wetter, temperatur, ort, besonderheit])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--num-rows", type=int, default=1000, help="Number of rows to generate in the CSV file")
    args = parser.parse_args()

    generate_fake_data(args.num_rows)
    print("Generated {} rows of fake data in fake_feuerwehr_data.csv".format(args.num_rows))

if __name__ == "__main__":
    main()