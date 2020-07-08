from bs4 import BeautifulSoup as bs
import pandas as pd
import glob

def main():
    df = pd.DataFrame(columns=['Utility','Pages','Total Tests','Failed','Warning','Passed','User Verify','Not Applicable'])
    
    for x in glob.glob('pdfs/*.html'):
        file = open(str(x), encoding="utf16")     
        soup = bs(file, features="lxml")
        file.close()
        
        name = str(x).split('\\')[1].split('.')[0]
        
        df = df.append({'Utility' : name,
                        'Pages': soup.find(attrs={'class':"p", 'id':"RPT_NUM_PAGES_LBL"}).text.split(': ')[1],
                        'Total Tests': soup.find(attrs={'class':"p", 'id':"RPT_NUM_TESTS_LBL"}).text.split(': ')[1],
                        'Failed': soup.find(attrs={'class':"p", 'id':"RPT_NUM_FAILED_LBL"}).text.split(': ')[1],
                        'Warning': soup.find(attrs={'class':"p", 'id':"RPT_NUM_WARNING_LBL"}).text.split(': ')[1],
                        'Passed': soup.find(attrs={'class':"p", 'id':"RPT_NUM_PASSED_LBL"}).text.split(': ')[1],
                        'User Verify': soup.find(attrs={'class':"p", 'id':"RPT_NUM_USER_VERIFY_LBL"}).text.split(': ')[1],
                        'Not Applicable': soup.find(attrs={'class':"p", 'id':"RPT_NUM_NA_LBL"}).text.split(': ')[1]
                        }, ignore_index=True)

    df.to_csv('access_report_results.csv', encoding='utf-8')
    
if __name__ == "__main__":
    main()