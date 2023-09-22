import os
# import aspose.words as aw

# Define the function to convert and save the document in separate directories for each iteration
def convert_and_save(file_path , id_):
    print("File path: " , file_path)
    # Load the document from the disk
    doc = aw.Document(file_path)

    # Create a directory for this iteration
    directory_path = f"documents/iteration_{id_}"
    os.makedirs(directory_path, exist_ok=True)

    # Define the output path for the markdown file
    # output_file_name = os.path.basename(file_path).replace(".docx", "_output.md")
    output_path = os.path.join(directory_path, 'output.md')

    # Save the document to Markdown format
    doc.save(output_path)
    print("Doc saved")

    # Return the directory path
    return directory_path

# Example usage

