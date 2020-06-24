from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pandas as pd
# install with this command pip install --upgrade oauth2client PyOpenSSL gspread

def data_append_row(hearder, full_data):
    print("==============data_append_row================")
    data = {}
    for row in full_data:
        item = {}
        
        for column_number in range(len(header)-1):
            item[header[column_number]] = row[column_number]

        data[item["รหัสสินค้า"]] = item
    return data

# for read-and-write access, use this line
#scope = ["https://www.googleapis.com/auth/spreadsheets"]
# for read-only access, use this line
scope = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('keytypeForGoogleSheet\\mcochai-dropship-c544f4aebe63.json', scope)
gc = gspread.authorize(credentials)

sheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/1ZbMoqi2SzsE4-Vf2RmIcERd7IiSVStiTuhF6wMb_RCk/edit#gid=0")
googlesheet_data = sheet.get_worksheet(0).get_all_values()
header = googlesheet_data.pop(0)
pandas_data = pd.DataFrame(googlesheet_data, columns=header)

dictionary_data = []
print(data_append_row(header, googlesheet_data))

"""dictionary_data.append(
    {
        "ลำดับ":pandas_data["ลำดับ"].loc[4],
        "รหัสสินค้า":pandas_data["รหัสสินค้า"].loc[4],
        "ชื่อสินค้า":pandas_data["ชื่อสินค้า"].loc[4],
        "จำนวนสินค้าพร้อมส่ง":pandas_data["จำนวนสินค้าพร้อมส่ง"].loc[4],
        "ราคา":pandas_data["ราคา"].loc[4],
        "น้ำหนัก":pandas_data["น้ำหนัก"].loc[4],
        "ขนาด":pandas_data["ขนาด"].loc[4]
    }
)
print(dictionary_data)"""

# print(pandas_data)
