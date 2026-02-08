import pandas as pd
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_raw_data():

    train_path = os.path.join(BASE_DIR, "data", "raw", "train.csv")
    test_path = os.path.join(BASE_DIR, "data", "raw", "test.csv")

    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

    return train_df, test_df


if __name__ == "__main__":
    train, test = load_raw_data()

    print("Train shape:", train.shape)
    print("Test shape:", test.shape)
