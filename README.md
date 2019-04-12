# Currency Crawler by Python
Use python 3.7 to crawl currency data and import to MongoDB under pipenv virtual environment

## Installation
```
pipenv install --dev
```

## Set Crontab on Linux
Run the job every day
```
01 01 * * * cd /path/to/your/project && /home/username/.local/bin/pipenv run /home/username/.virtualenvs/project/bin/python run.py USD AUD >> /path/to/your/log 2&>1
```
