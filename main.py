import csv


def create_institution_file(file_name):
    """
    Creates a new csv file named "Institutions.csv". This file contains information about each distinct institution in
    the csv file.
    :param file_name: the math contest csv file.
    """
    institutions = {}
    institution_id = 1
    # Open the file.
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        # Get the data from each column and assign to the appropriate variable.
        for row in reader:
            institution_name = row['Institution']
            city = row['City']
            state_province = row['State/Province']
            country = row['Country']
            # Add the institution to the dictionary if it's not already present.
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

    # Create a new csv file with the proper institution information.
    with open('Institutions.csv', 'w', newline='') as csvfile:
        # Column header names.
        headers = ['Institution ID', 'Institution Name', 'City', 'State/Province', 'Country']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        # Write out the data to the new csv file.
        for institution_id, details in institutions.items():
            writer.writerow(details)


def create_team_file(file_name):
    """
    Creates a new csv file named "Teams.csv". This file contains information about each distinct team in the csv file.
    :param file_name: the math contest csv file.
    """
    institutions = {}
    # Open and read the institutions file to get the Institution ID based on the name.
    with open('Institutions.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            institutions[row['Institution Name']] = row['Institution ID']
    # Open and read the original "year.csv" math file.
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)

        with open('Teams.csv', 'w', newline='') as csvfile:
            # Column header names.
            headers = ['Team Number', 'Advisor', 'Problem', 'Ranking', 'Institution ID']
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()

            # Write each team to the new csv file,
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
