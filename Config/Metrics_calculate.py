import math
import pandas as pd
def get_code_comprehen(df):
    for index, row in df.iterrows():
        cognitive = row['cog_complexity']
        comment = row['comment_per_loc']
        result = round((2*comment)/math.log(cognitive, 10), 3)
        print(row['project_name'], result)
    return

def get_doc_comprehen(df):
    for index, row in df.iterrows():
        density = row['density%']
        files = row['number_of_files']
        comment = row['comment_per_loc']
        comment_cover = row['comment_coverage%']/100
        result = round(((comment * comment_cover * (math.log(files, 20)))/density), 4)
        print(row['project_name'], result)
    return

def get_code_reusability(df):
    for index, row in df.iterrows():
        bug = row['bugs']
        cyclo_complex = row['cyclo_complexity']
        result = round(1/(math.log(cyclo_complex, 10)+bug), 3)
        print(row['project_name'], result)
    return
def get_built_reusability(df):
    for index, row in df.iterrows():
        crit_issue = row['critical_issue%']
        security_hotspot = row['security_hotspot']
        result = round(1/math.log((crit_issue+security_hotspot), 2), 3)
        print(row['project_name'], result)
    return
def get_test_quality(df):
    for index, row in df.iterrows():
        case_per_funct = row['test_case_per_funct']
        test_kloc_ratio = row['test_kloc_per_src_kloc']
        result = round(case_per_funct+(test_kloc_ratio/2), 2)
        print(row['project_name'], result)
    return

def get_team_activeness(df):
    for index, row in df.iterrows():
        pull_req = row['github_closed_pull_request']
        commit = row['number_of_commits']
        age = row['repo_age']
        result = round((pull_req*math.log(commit, 10))/age, 2)
        print(row['project_name'], result)
    return
if __name__ == '__main__':
    # Run the Flask app
    df = pd.read_csv("../Material/api_lib_metrics.csv")
    get_code_comprehen(df)
    print('-------------------')
    get_doc_comprehen(df)
    print('-------------------')
    get_code_reusability(df)
    print('-------------------')
    get_built_reusability(df)
    print('-------------------')
    get_test_quality(df)
    print('-------------------')
    get_team_activeness(df)