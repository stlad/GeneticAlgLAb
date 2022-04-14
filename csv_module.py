import csv


history = []


def save_csv(filename):
    with open(filename,'w', newline='') as csvfile:
        fieldnames= history[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()

        for row in history:
            writer.writerow(row)
    history.clear()
