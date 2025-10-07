# Create an empty list
my_list = []

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Extend with another list
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find and print the index of 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)

# (Optional) Print final list to verify
print("Final list:", my_list)


#Calculate_discount
def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = (discount_percentage / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price, discount_percentage)

# Display the result
if discount_percentage >= 20:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The price remains: ${final_price:.2f}")


# file_handling
def read_and_modify_file():
    try:
        # Ask the user for the filename
        file_path = input("Enter the filename to read: ")

        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Print the content
        print("\nFile Content:")
        print(content)

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write modified content to a new file
        new_file_path = "modified_" + file_path
        with open(new_file_path, 'w') as new_file:
            new_file.write(modified_content)

        print(f"\nModified content written to {new_file_path}")

    except FileNotFoundError:
        print(f"❌ The file '{file_path}' was not found.")
    except PermissionError:
        print(f"⚠️ Permission denied while accessing '{file_path}'.")
    except Exception as e:
        print(f"⚡ An unexpected error occurred: {e}")


# Run the function
read_and_modify_file()
