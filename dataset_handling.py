# Importing Dataset

import os
import pandas as pd


def place_in_folder(file, foldername, folderdir):

    """
    This functuin will take file name, folder name and folder dir (train, val) and change location of image from /jpg folder (default dataset folder from oxford)
    to the information passed
    """

    # creating folder if it does not exist

    if not os.path.exists(os.path.join(folderdir, foldername)):
        os.makedirs(os.path.join(folderdir, foldername))

    # changing image path
    os.rename(
        os.path.join(dirname, file),
        os.path.join(
            "/Users/harshit/Downloads/oxford-102-flowers/" + folderdir, foldername, file
        ),
    )


# importing csv file to extract image tables and adding type dir (train or val)
labels_train = pd.read_csv("train.csv")
labels_train.insert(2, "folderdir", "train")

labels_valid = pd.read_csv("valid.csv")
labels_valid.insert(2, "folderdir", "val")

# merging labes
labels = pd.concat([labels_train, labels_valid], ignore_index=True)


dirname = "/Users/harshit/Downloads/oxford-102-flowers/jpg"

""" iterating through all the images present in the dataset, based on the file name its label is extracted and is placed in folder and dir of appropriate value """

if os.path.isdir(dirname):
    for filename in os.listdir(dirname):
        foldername = str(
            labels[labels["Name"] == str("jpg/" + filename)]["Label"].values[0]
        )

        folderdir = str(
            labels[labels["Name"] == str("jpg/" + filename)]["folderdir"].values[0]
        )

        place_in_folder(filename, foldername, folderdir)
