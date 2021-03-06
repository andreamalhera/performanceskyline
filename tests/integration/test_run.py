from processmining.run import run_processmining, longestSubstring
import pandas as pd
import os

def test_run_processmining():
    LUIGI_LOG_PATH = './tests/data/input_test_run_processmining'
    run_processmining(LUIGI_LOG_PATH)
    files = [file for file in os.listdir(LUIGI_LOG_PATH) if file.endswith('.log')]
    process_name = longestSubstring(files[0].split('.log')[0],files[-1].split('.log')[0])
    csv_path = LUIGI_LOG_PATH+'/'+str(process_name)+'.csv'

    assert not pd.read_csv(csv_path).empty