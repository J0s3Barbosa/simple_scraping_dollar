import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup

from file_utils import FileUtils

class DollarQuotation:
    """
     Get quotation. This is a property for the Quotation object
     
     @param self - reference to the instance of this class
     
     @return value of the quotation
    """
    def get_quotation(self):
             
        file_name = 'DollarQuotation.csv'
        path_file_name = FileUtils.get_file(file_name)

        field_names = ["Date", "Buy Rate", "Sell Rate"]
        dict = {field_names[0]: [], field_names[1]: [], field_names[2]: []}

        try:
            df = pd.read_csv(path_file_name)
            print("CSV file already exists")
        except FileNotFoundError:
            df = pd.DataFrame(dict)
            df.to_csv(path_file_name, index=False)
            print("CSV file created successfully")

        url = "https://ptax.bcb.gov.br/ptax_internet/consultarUltimaCotacaoDolar.do"

        # Make a GET request to fetch the raw HTML content
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "html5lib")

        data = []
        table = soup.find(
            "table", attrs={"summary": "Cotação de fechamento do Dólar americano"}
        )
        table_body = table.find("tbody")
        rows = table_body.find_all("tr")
        for row in rows:
            td = row.find_all("td")
            td = [ele.text.strip() for ele in td]
            data.append([ele for ele in td if ele])  # Get rid of empty values
        finalData = [x for x in data if x]
        retrieved_data = {field_names[0]: [finalData[0][0]], field_names[1]:[finalData[0][1]], field_names[2]: [finalData[0][2]]}
        
        treated_data = pd.DataFrame(retrieved_data)
        final_result = df.append(treated_data)
        print(final_result)
        print(finalData[0][0])
        print(finalData[0][1])
        print(finalData[0][2])

        final_result.to_csv(path_file_name, index=False)
        
