# Welcome to SE327BackEnd
### We compare Django, Flask, Fastapi, and Sanic to find out which one is best in term of code quality.
## To use the back end
### Easy steps
### 1. Run application.py
### Try to call backend using GET method
```
http://localhost:5000/get_csv_as_df
```
## Patch note version 0.1
1. Compile information gather from code analysis tools such as Sonarqube and Understand.
2. Create API using flask library (no biased associated, I just familiar with this package). :joy:

## Patch note version 0.2
1. Add more columns in the csv files to get more metrics to comparison.

## Patch note version 0.3
1. Add activeness of each project's author and number of test classes and kloc in the test folder.

## Patch note version 0.4
1. Add mathematic formula to calculate each metric from the project's scoring matrix.

## Patch note version 0.5 [23798e1](https://github.com/953327-Project/BackEnd/commit/23798e1055871504d46bad306b479f4f602d8c8e)
1. Changed variable "csv_data" to "Metrics_csv", variable "metric_csv_data" to "Scores_csv", variable "df" to "df_Metrics" and add "df_Scores" in Main.py line 8-11, 16, 19, 35 and 47
2. Added new sorted Endpoint for calling data from score_metrics.csv in Main.py line 23-29

## Patch note version 1.0
1. Release backend version 1.0
