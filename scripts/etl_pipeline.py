import subprocess

print("Step 1: Running Data Ingestion...")
subprocess.run(
    ["python", "data_ingestion.py"],
    check=True
)

print("Step 2: Cleaning NAV History...")
subprocess.run(
    ["python", "clean_nav_history.py"],
    check=True
)

print("Step 3: Cleaning Performance Data...")
subprocess.run(
    ["python", "clean_performance.py"],
    check=True
)

print("Step 4: Cleaning Transaction Data...")
subprocess.run(
    ["python", "clean_transactions.py"],
    check=True
)

print("Step 5: Loading Data to SQLite...")
subprocess.run(
    ["python", "load_to_sqlite.py"],
    check=True
)

print("\nETL Pipeline Completed Successfully!")