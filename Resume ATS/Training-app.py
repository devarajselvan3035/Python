paragraph = """


Responsibilities


    As a Software Engineer, you will work on developing features for Mach1ML platform, support customers in model deployment using Mach1ML platform on GCP and On-prem
    You will work on the cutting-edge technologies such as GCP, Kubernetes, Docker, Seldon, Tekton, Airflow, Rally, etc.


Qualifications


    python programming experience, Experience with Python and has used Machine Learning tools (pytorch, TensorFlow, xgboost etc.
    GCP services (airflow, bigquery,cloudrun etc.)
    MLops atleast basics.
    Experience working with container technology, docker files, docker images, GitHub, CI/CD concepts
    BI, ETL, Reporting /Visualization/Dashboards
    Must be comfortable for Chennai Location.


    Experience applying Agile practices to solution delivery.
    Must be a self-starter to understand existing bottlenecks and come up with innovative solutions.
    Strong communication and presentation skills, ability to share/teach others, work collaboratively with others.
    Flexibility to explore and work with newer technologies and tools.


"""

import pandas as pd
paragraph = paragraph.replace("\n", ' ')
paragraph = paragraph.replace("\t", ' ')
words_count = {}
remove_list = ['', 'is', 'the', 'you', 'on', 'for', 'and', 'with', 'as', 'to', 'a', 'will', 'must']

for word in paragraph.split(' '):
    word = word.lower()
    if word in words_count.keys():
        words_count[word] += 1
    else:
        words_count[word] = 1
for word in remove_list:
    try:
        del words_count[word]
    except KeyError:
        pass

df = pd.DataFrame(words_count.items(), columns=['Word', 'Count'])
df = df.sort_values(by='Count', ascending=False)
print(df)
