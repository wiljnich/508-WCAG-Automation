from bs4 import BeautifulSoup as bs
import pandas as pd
import glob

def main():
    df = pd.DataFrame(columns=['Utility','Pages','Total Tests','Failed','Warning','Passed','User Verify','Not Applicable',
                               '1','2','3','4','5','6','7','8','9','10',
                               '11','12','13','14','15','16','17','18','19','20',
                               '21','22','23','24','25','26','27','28','29','30',
                               '31','32','33','34','35','36','37','38','39','40',
                               '41','42','43','44','45','46','47','48','49','50',
                               '51'])
    
    for x in glob.glob('pdfs/*.html'):
        file = open(str(x), encoding="utf16")     
        soup = bs(file, features="lxml")
        file.close()
        
        name = str(x).split('\\')[1].split('.')[0]
        
        even = []
        odd = []
        table = soup.find(attrs={'id' :'GridView2'})
        for x in table.findAll(attrs={'class':'grid_row'}):
            odd.append(x.findAll('td')[5].text)
        for x in table.findAll(attrs={'class':'grid_alt_row'}):
            even.append(x.findAll('td')[5].text)
        
        df = df.append({'Utility' : name,
                   'Pages': soup.find(attrs={'class':"p", 'id':"RPT_NUM_PAGES_LBL"}).text.split(': ')[1],
                   'Total Tests': soup.find(attrs={'class':"p", 'id':"RPT_NUM_TESTS_LBL"}).text.split(': ')[1],
                   'Failed': soup.find(attrs={'class':"p", 'id':"RPT_NUM_FAILED_LBL"}).text.split(': ')[1],
                   'Warning': soup.find(attrs={'class':"p", 'id':"RPT_NUM_WARNING_LBL"}).text.split(': ')[1],
                   'Passed': soup.find(attrs={'class':"p", 'id':"RPT_NUM_PASSED_LBL"}).text.split(': ')[1],
                   'User Verify': soup.find(attrs={'class':"p", 'id':"RPT_NUM_USER_VERIFY_LBL"}).text.split(': ')[1],
                   'Not Applicable': soup.find(attrs={'class':"p", 'id':"RPT_NUM_NA_LBL"}).text.split(': ')[1],
                    '1' : odd[0],
                    '2' : even[0],
                    '3' : odd[1],
                    '4' : even[1],
                    '5' : odd[2],
                    '6' : even[2],
                    '7' : odd[3],
                    '8' : even[3],
                    '9' : odd[4],
                    '10' : even[4],
                    '11' : odd[5],
                    '12' : even[5],
                    '13' : odd[6],
                    '14' : even[6],
                    '15' : odd[7],
                    '16' : even[7],
                    '17' : odd[8],
                    '18' : even[8],
                    '19' : odd[9],
                    '20' : even[9],
                    '21' : odd[10],
                    '22' : even[10],
                    '23' : odd[11],
                    '24' : even[11],
                    '25' : odd[12],
                    '26' : even[12],
                    '27' : odd[13],
                    '28' : even[13],
                    '29' : odd[14],
                    '30' : even[14],
                    '31' : odd[15],
                    '32' : even[15],
                    '33' : odd[16],
                    '34' : even[16],
                    '35' : odd[17],
                    '36' : even[17],
                    '37' : odd[18],
                    '38' : even[18],
                    '39' : odd[19],
                    '40' : even[19],
                    '41' : odd[20],
                    '42' : even[20],
                    '43' : odd[21],
                    '44' : even[21],
                    '45' : odd[22],
                    '46' : even[22],
                    '47' : odd[23],
                    '48' : even[23],
                    '49' : odd[24],
                    '50' : even[24],
                    '51' : odd[25]
                    }, ignore_index=True)

    df.to_csv('access_report_results.csv', encoding='utf-8')
    
if __name__ == "__main__":
    main()