"""
TODO: to be sure if you didnt miss any column, check the column from the following post
https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede
Because a few columns are allowable, and if you were checking the columns from the zero element, then you may miss some.
I have done it for, but it should be done for the others
I have manually checked that I'm not missing any data
"""
import csv
import glob
import os
import xml.etree.ElementTree as ET
from concurrent.futures import ProcessPoolExecutor

os.chdir('/Users/aadityabhatia/Documents/GitHub/SE_Bugs_vs_Features/')


def xml_to_csv(xml_file):
    csv_file = xml_file.replace('.xml', '.csv')
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # The first child of the root should correspond to the file name
    first_child_tag = xml_file.split("/")[-1].split(".xml")[0].lower()
    first_child = root.find(first_child_tag)

    # If the first child of root has no children, then use the attributes of the root's first child
    if first_child_tag == "posts":
        header = ['Id', 'PostTypeId', "AcceptedAnswerId", "ParentId", 'CreationDate', "DeletionDate", 'Score',
                  'ViewCount', 'Body', 'OwnerUserId', 'LastEditorUserId', 'LastEditDate', 'LastActivityDate', 'Title',
                  'Tags', 'AnswerCount', 'CommentCount', "FavouriteCount", 'ClosedDate', 'ContentLicense']
    elif not list(root[0]):
        header = list(root[0].attrib.keys())
    else:
        print(f"XML structure of {xml_file} is not supported. Skipping.")
        return

    # Open a CSV file for writing
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)

        # Write the data rows
        for row in root:
            csvwriter.writerow([row.get(column, '') for column in header])

    print(f"Processed {xml_file} into {csv_file}")


def main():
    xml_files = glob.glob('data/meta.stackexchange.com/*.xml')

    # Using multiprocessing to process files in parallel
    with ProcessPoolExecutor() as executor:
        executor.map(xml_to_csv, xml_files)


if __name__ == "__main__":
    main()
