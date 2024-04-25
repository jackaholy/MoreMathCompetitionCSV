import csv


def calculate_average_number_of_teams(file_name):
    institutions = {}
    total_teams = 0
    # Open the file.
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        # Get data from each row.
        for row in reader:
            institution_name = row['ï»¿Institution']
            # Add the institution to the dictionary if it's not already present.
            if institution_name not in institutions:
                institutions[institution_name] = {
                    'Institution Name': institution_name,
                }
            total_teams += 1

    total_institutions = len(institutions)

    if total_institutions == 0:
        return 0
    else:
        return total_teams / total_institutions


def institution_data_to_dict(file_name):
    """
    Creates a new csv file named "Institutions.csv". This file contains information about each distinct institution in
    the csv file.
    :param file_name: the math contest csv file.
    :return a dictionary with information about the institutions.
    """
    institutions = {}
    institution_id = 1
    # Open the file.
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        # Get the data from each column and assign to the appropriate variable.
        for row in reader:
            institution_name = row['ï»¿Institution']
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
    return institutions


def main(file_name):
    with open('ordered_file.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Average Teams per Institution:', calculate_average_number_of_teams(file_name)])
        writer.writerow([''])


if __name__ == '__main__':
    main("data/2015.csv")
