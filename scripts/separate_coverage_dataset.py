import os


def separate_dataset(dataset_path):
    # Get all files in dataset directory
    files = os.listdir(dataset_path)

    for file in files:
        file_name = os.path.splitext(file)[0]

        if file_name[-1] == "t":
            os.rename(dataset_path + file,
                      os.path.join(dataset_path, "..", "tampered", file))
        else:
            os.rename(dataset_path + file,
                      os.path.join(dataset_path, "..", "authentic", file))

    print("Dataset separated successfully!")


if __name__ == "__main__":
    separate_dataset("")
