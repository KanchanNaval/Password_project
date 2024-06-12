import pikepdf

# Open the existing PDF
old_pdf = pikepdf.Pdf.open("MY_RESUME.pdf")

# Define the permissions to disable text extraction
no_extr = pikepdf.Permissions(extract=False)

# Save the new PDF with encryption and the specified permissions
old_pdf.save("pro_new.pdf", encryption=pikepdf.Encryption(
    user="123asd",
    owner="resume",
    allow=no_extr
))
