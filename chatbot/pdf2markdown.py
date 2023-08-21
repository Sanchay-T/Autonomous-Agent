import os
import aspose.words as aw

# Define the function to convert and save the document in separate directories for each iteration
def convert_and_save(file_path, iteration_number):
    # Load the document from the disk
    doc = aw.Document(file_path)

    # Create a directory for this iteration
    directory_path = f"documents/iteration_{iteration_number}"
    os.makedirs(directory_path, exist_ok=True)

    # Define the output path for the markdown file
    output_file_name = os.path.basename(file_path).replace(".docx", "_output.md")
    output_path = os.path.join(directory_path, output_file_name)

    # Save the document to Markdown format
    doc.save(output_path)

    # Return the directory path
    return directory_path

# Example usage
file_path = "path/to/your/file.docx"
iteration_number = 1
directory_path = convert_and_save(file_path, iteration_number)
