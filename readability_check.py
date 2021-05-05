import os
import textstat
import tika
from tika import parser
import pandas as pd
import glob

os.environ['TIKA_SERVER_JAR'] = '\tika-server-1.24.1.jar'
tika.TikaClientOnly = True

def main():
    df = pd.DataFrame(columns=['Utility','FK Score', 'FK Grade Level'])
    
    for x in glob.glob('pdfs/*.pdf'):
        try:
            text = parser.from_file(x)
            df = df.append({'Utility' : str(x).split('\\')[1].split('.')[0],
                       'FK Score': textstat.flesch_reading_ease(text['content']),
                       'FK Grade Level': textstat.flesch_kincaid_grade(text['content'])
                      }, ignore_index=True)
        except:
             df = df.append({'Utility' : str(x).split('\\')[1].split('.')[0],
                       'FK Score': 'N/A',
                       'FK Grade Level': 'N/A'
                      }, ignore_index=True)

    df.to_csv('data/results/readability_results.csv', encoding='utf-8')
    
if __name__ == "__main__":
    main()
