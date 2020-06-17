import os
import textstat
import tika
from tika import parser
import pandas as pd
import glob

os.environ['TIKA_SERVER_JAR'] = 'C:\\Users\\William Nicholas\\Documents\\Temp\\tika-server-1.24.1.jar'
tika.TikaClientOnly = True

def main():
    df = pd.DataFrame(columns=['Utility','FK Score', 'FK Grade Level', 'Text Standard'])
    
    for x in glob.glob('pdfs/*.pdf'):
        text = parser.from_file(x)
        df = df.append({'Utility' : str(x).split('\\')[1].split('.')[0],
                   'FK Score': textstat.flesch_reading_ease(text['content']),
                   'FK Grade Level': textstat.flesch_kincaid_grade(text['content']),
                   'Text Standard': textstat.text_standard(text['content'])
                  }, ignore_index=True)

    df.to_csv('readability_results.csv', encoding='utf-8')
    
if __name__ == "__main__":
    main()