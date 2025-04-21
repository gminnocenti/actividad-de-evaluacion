import pyodbc
import textwrap
from dotenv import load_dotenv
import os
import pandas as pd

#cargar archivo.env
load_dotenv()
# conseguir variables de entorno
server_name = os.getenv("SERVER")  
database = os.getenv("DATABASE")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
driver = '{ODBC Driver 17 for SQL Server}'

server = f'tcp:{server_name}.database.windows.net,1433'

# Construir la cadena de conexión
cnxnection_string = textwrap.dedent(f'''
    Driver={driver};
    Server={server};
    Database={database};
    Uid={username};
    Pwd={password};
    Encrypt=yes;
    TrustServerCertificate=no;
    cnxnection Timeout=30;
''')

# cnxnect
cnxn = pyodbc.connect(cnxnection_string)
cursor = cnxn.cursor()
query = "SELECT * FROM SalesLT.customer"

# Execute the query using the existing cnxnection
cursor = cnxn.cursor()
cursor.execute(query)

# Fetch all rows and create a DataFrame
rows = cursor.fetchall()
columns = [column[0] for column in cursor.description]
df_customers = pd.DataFrame.from_records(rows, columns=columns)

print(f"Retrieved {len(df_customers)} customer records")
print("\nFirst 5 customers:")
print(df_customers.head())
cursor.close()

# save df to csv for easier
#df_customers.to_csv("customers.csv", index=False)
