import csv


def create_institution_file(file_name):
    institutions = {}
    institution_id = 1
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            institution_name = row['Institution']
            city = row['City']
            state_province = row['State/Province']
            country = row['Country']
            # Adding institution to the dictionary if not already present
            if institution_name not in institutions:
                institutions[institution_name] = {
                    'Institution ID': institution_id,
                    'Institution Name': institution_name,
                    'City': city,
                    'State/Province': state_province,
                    'Country': country
                }
                # The next institution entered should have a new ID number.
                institution_id += 1

    # Create a new csv file with the proper institution information
    with open('Institutions.csv', 'w', newline='') as csvfile:
        headers = ['Institution ID', 'Institution Name', 'City', 'State/Province', 'Country']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for institution_id, details in institutions.items():
            writer.writerow(details)


def create_team_file(file_name):
    institutions = {}
    with open('Institutions.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            institutions[row['Institution Name']] = row['Institution ID']

    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)

        with open('Teams.csv', 'w', newline='') as csvfile:
            headers = ['Team Number', 'Advisor', 'Problem', 'Ranking', 'Institution ID']
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()

            # Write each team to the file
            for row in reader:
                writer.writerow({
                    'Team Number': row['Team Number'],
                    'Advisor': row['Advisor'],
                    'Problem': row['Problem'],
                    'Ranking': row['Ranking'],
                    'Institution ID': institutions.get(row['Institution'])
                })


def main(file_name):
    create_institution_file(file_name)
    create_team_file(file_name)


if __name__ == "__main__":
    main("data/2015.csv")
