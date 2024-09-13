import os

# Variable to track the total number of inputs read
input_count = 0


# Function to read inputs from the file and remove asterisks from previous entries
def read_input(file_name):
    global input_count
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            inputs = file.readlines()
        # Clean the inputs by stripping newlines and removing asterisks
        inputs = [item.strip().replace(" *", "") for item in inputs]
        # Update the total count of inputs read
        input_count += len(inputs)
        return inputs
    else:
        print("Error: file not found.")
        return []


# Function to save the updated inputs back to the file
def save_to_file(file_name, data):
    with open(file_name, 'w') as file:
        for item in data:
            file.write(item + '\n')


# Function to mark new inputs with an asterisk
def mark_new_inputs(old_inputs, new_inputs):
    updated_inputs = []
    for item in new_inputs:
        if item not in old_inputs:
            updated_inputs.append(item + " *")  # Mark new inputs with an asterisk
        else:
            updated_inputs.append(item)  # Keep existing inputs as they are
    return updated_inputs


# File name where the data is stored
file_name = 'data.txt'

# Step 1: Read the initial inputs from the file
print("Program starting, please wait while the inputs are read.")
initial_inputs = read_input(file_name)

# Show the inputs that have been read (optional)
print(f"Inputs read from the file: {initial_inputs}")
print(f"Total inputs read: {input_count}")

# Prompt the user to edit the file
print("You can now edit the file 'data.txt'. After finishing, press Enter to continue.")
input()  # Pauses to allow the user to edit the file

# Step 2: Read the updated inputs after the file has been edited
final_inputs = read_input(file_name)

# Step 3: Mark new inputs and prepare the updated list
updated_inputs = mark_new_inputs(initial_inputs, final_inputs)

# Step 4: Save the updated inputs back to the file
save_to_file(file_name, updated_inputs)

print("The new inputs have been marked with an asterisk in the file.")
