#Writing function to read and sort the names alphabetically from file
def sort_names(input_file, output_file):
    with open(input_file, 'r') as f:
        names = f.read().splitlines()
        sorted_names = sorted(names)
#Opening file in write mode to write the sorted name list
    with open(output_file, 'w') as fw:
        fw.write('\n'.join(sorted_names))

# Asking user to enter file name
input_file = input("Enter file name: ")
output_file = input("Enter file name to save the sorted content: ")
sort_names(input_file, output_file)
print(f"Names are sorted and saved to {output_file}")
