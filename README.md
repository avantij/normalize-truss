# Normalize CSV

## Requirements
- Python 3
- Linux
- pip
  
## Environment
Run following commands to setup environment
```
python3 -m venv virtualenv
source virtualenv/bin/activate
pip install -r requirements.txt
```

## Running Normalizer

```
python3 run_normalizer.py < input_data.csv > output_data.csv
```

## Tests
To run tests:

```
python3 TestNormalize.py 
```