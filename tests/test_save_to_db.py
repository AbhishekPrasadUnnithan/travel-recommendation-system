import os
import pandas as pd
from sqlalchemy import create_engine

def test_save_to_db_creates_table_and_data():
    data = [
        {"Name": "Test Hotel", "Rating": 4.5, "Address": "123 Test St", "City": "TestCity", "Map Link": "http://testlink"}
    ]
    test_db_path = "sqlite:///test_hotels.db"
    df = pd.DataFrame(data)

    engine = create_engine(test_db_path)

    try:
        df.to_sql("hotels", engine, if_exists="replace", index=False)
        result_df = pd.read_sql("SELECT * FROM hotels", engine)

        assert not result_df.empty
        assert result_df.iloc[0]["Name"] == "Test Hotel"

    finally:
        engine.dispose()
        if os.path.exists("test_hotels.db"):
            os.remove("test_hotels.db")

def test_db_duplicate_insert_does_not_crash():
    data = [
        {"Name": "Hotel X", "Rating": 4.0, "Address": "Addr X", "City": "X", "Map Link": "link"}
    ]
    df = pd.DataFrame(data)
    test_db_path = "sqlite:///test_hotels_dup.db"
    engine = create_engine(test_db_path)

    try:
        # Save twice to simulate duplicates
        df.to_sql("hotels", engine, if_exists="replace", index=False)
        df.to_sql("hotels", engine, if_exists="append", index=False)

        result_df = pd.read_sql("SELECT * FROM hotels", engine)
        assert len(result_df) >= 1

    finally:
        engine.dispose()
        if os.path.exists("test_hotels_dup.db"):
            os.remove("test_hotels_dup.db")
