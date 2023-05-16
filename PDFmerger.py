import os
from PyPDF2 import PdfMerger
from natsort import natsorted


def merge_pdfs(path):
    count = 0
    merged_files = []  # Add a list to store the names of merged files
    try:
        merger = PdfMerger()

        # Get all the pdf filenames from downloads folder mac
        pdfs = [f for f in os.listdir(path) if f.endswith('.pdf')]

        # sort the pdfs in natural order
        sorted_pdfs = natsorted(pdfs)

        # Loop through all the pdfs and append them to the merger object
        for pdf in sorted_pdfs:
            merger.append(path + pdf)
            count += 1
            # Add the pdf name to the merged_files list
            merged_files.append(pdf)

        # Write all the files into a file which is named as shown below
        merger.write(path + "merged.pdf")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        merger.close()
        return count, merged_files  # Return the count and the list of merged files


if __name__ == "__main__":
    path = '/Users/markcederborg/Downloads/input/'
    merged_count, merged_files = merge_pdfs(
        path)  # Capture the returned values

    # Print the count and the list of merged files
    print(f"{merged_count} PDFs were merged:")
    for file_name in merged_files:
        print(file_name)
