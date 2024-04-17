import csv


def create_institution_file(file_name):
    institutions = {}
    institution_id = 1
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        # next(reader)  # Ignore the header

        for row in reader:
            institution_name = row['Institution']
            city = row['City']
            state_province = row['State/Province']
            country = row['Country']
            # Adding institution to the dictionary if not already present
            if (institution_name, city, state_province, country) not in institutions.values():
                institutions[institution_id] = {
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
            details['Institution Name'] = institution_name
            writer.writerow(details)


def create_team_file(file_name):
    institutions = {}
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        next(reader)  # Ignore the header
        for row in reader:
            team_number = row['Team Number']
            advisor = row['Advisor']
            problem = row['Problem']
            ranking = row['Ranking']

    with open('Teams.csv', 'w') as csvfile:
        headers = ['Team Number', 'Advisor', 'Problem', 'Ranking', 'Institution ID']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        # Write each team to the file
        with open(file_name) as csvfile:
            reader = csv.DictReader(csvfile)
            next(reader)  # Ignore the header
            for row in reader:
                writer.writerow({
                    'Team Number': team_number,
                    'Advisor': advisor,
                    'Problem': problem,
                    'Ranking': ranking,
                })


def main(file_name):
    create_institution_file(file_name)
    create_team_file(file_name)


if __name__ == "__main__":
    main("data/2015.csv")
