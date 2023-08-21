
@pip install aspose-words

import aspose.words as aw

# Load the document from the disc.
doc = aw.Document("user.pdf")

# Save the document to HTML format.
doc.save("output.md")