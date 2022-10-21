API initial Url: https://api.football-data.org/

API account name: testing.data999@gmail.com

API token information: 

Please modify your client to use a HTTP header named "X-Auth-Token" with the underneath personal token as value.
Your token: 12abfbaacdab48bc8948ed6061925e1f

----(Implementation)----

# Data Engineer (Python) Test
Create a visualization illustrating the comparative performance of soccer teams in
2020, 2021 and 2022 in the English Premier League. The KPIs they are
looking for are derived from games won, drawn, lost, goals for and goals
against, for the EPL teams in the desired timeframe.

## Getting started

### Create a virtual environment and activate
```bash
python3 -m venv venv
source ./venv/bin/activate
```
### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the script
```bash
python main.py
```
Will run the script with default arguments
Or use ```--help``` to see usage
```
python main.py --help

usage: main.py [-h] [-s SEASONS] [-o OUTPUT_DIR]

options:
  -h, --help            show this help message and exit
  -s SEASONS, --seasons SEASONS
                        A list of season years e.g:"['2020','2021','2022']"
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
                        Specify the path of the output directory default = ./data/
```

## Runing tests

### Test the creation of csv files

```bash
python tests/test_csvs.py
```

### Test clubs that have played for each season

```bash
python tests/test_season.py
```

### Test matches won by a specific club for each season

```bash
python tests/test_club.py
```

## Run the benchmark
```bash
python benchmark/time.py
```
It will print out the number of seconds the script took to execute

## Project Structure
```
project
│   README.md
│   main.py
│   requirements.txt
│   .env
│   .gitignore
│   .pre-commit-config.yaml
│   .pylintrc
└── benchmark
│   │   time.py
|   |   profiler.py
└── data
│   │   season-{year}.csv
│   │	...
└── models
│   │   club.py
│   │   premier_league.py
│   │   season.py
└── repositories
│   │   season_repository.py
└── tests
│   │   test_club.py
│   │   test_csvs.py
│   │   test_season.py
└── utils
│   │   main_lib.py
└── venv
```
## Benchmarking
Execution time(s): 4.779070354

Profiling: `python benchmark/profiler.py`

## Naming Convention
https://google.github.io/styleguide/pyguide.html#316-naming
> module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name, query_proper_noun_for_thing, send_acronym_via_https.

## Linting
To run the linter run
```bash
pylint main.py
```
> Output: `Your code has been rated at 10.00/10`

## Pre-commit
To manually run pre-commit on all files run
```bash
pre-commit run --all-files
```

## Modules
- requests
- pylint
- python-dotenv
- pre-commit

## Sample CSV Output

![Output image](./images/output.png "Output image")
