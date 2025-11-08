import datetime
import os
import subprocess

dir = 'data/raw'
folder = datetime.date.today().strftime('%Y-%m-%d')
new_data_dir = os.path.join(dir, folder)
data = 'rishavdash/retail-demand-forecasting-dataset'

try:
    result = subprocess.run(
        ['kaggle', 'datasets', 'download', '-d', data, '--unzip', '-p', new_data_dir],
        text=True,
        capture_output=True,
        check=True
    )
    print(f'data set downloaded {result.stdout}')

except subprocess.CalledProcessError as e:
    print(f' Kaggle command fails: {e.stderr}')
except Exception as e:
    print(f'unknown error: {e}')