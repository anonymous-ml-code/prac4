FILENAME = "subject_data.txt"

def main():
    data = load_data()
    display_subject_details(data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_list = []  # Initialize an empty list to store the nested lists
    with open(FILENAME, 'r') as input_file:  # Open the file
        for line in input_file:
            line = line.strip()  # Remove the \\n
            parts = line.split(',')  # Split the line into its parts
            parts[2] = int(parts[2])  # Convert the student number to an integer
            data_list.append(parts)  # Append the processed parts as a list to the main list
    return data_list

def display_subject_details(data):
    """Display subject details from the data."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")

main()
