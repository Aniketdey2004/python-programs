# Create a file and write some text
with open("sample.txt", 'w') as f:
    f.write("Hello World! This is a file.")

# Open the file in read and write mode
with open("sample.txt", 'r+') as f:
    # Show the initial content
    print("Original Content:", f.read())

    # Use tell() to show the current position of the file pointer
    print("Current file pointer position:", f.tell())

    # Use seek() to move the file pointer to the 6th byte (after 'Hello ')
    f.seek(6)
    print("File pointer moved to position:", f.tell())

    # Read the content after moving the pointer
    print("Content after moving the pointer:", f.read())

    # Truncate the file to 12 bytes (keeps only 'Hello World!')
    f.truncate(12)

# Open the file again to show the truncated content
with open("sample.txt", 'r') as f:
    print("\nContent after truncation:", f.read())
