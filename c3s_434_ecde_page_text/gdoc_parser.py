from apiclient import discovery
from credentials import get_credentials
import httplib2
import simplejson

SHEET = ('1BHVHR1-3DC-AJ1ZQUtGUOs25fiGrt0adwmZcSNDFMk0', 'MainElements')


def dict_from_sheet_values(rows):
    records = []
    headers = rows[0]

    for row in rows[1:]:
        record = {}

        for i, header in enumerate(headers):
            value = row[i]
            record[header] = value
        
        records.append(record)

    return records
            

def parse_google_spreadsheet(sheet):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
    service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)

    result = service.spreadsheets().values().get(
        spreadsheetId=SHEET[0], 
        range=SHEET[1]
    ).execute()
    values = result.get('values', [])

    if not values:
        raise exception('No data found')

    records = dict_from_sheet_values(values)

    with open('outputs/json/records.json', "w") as writer:
        simplejson.dump(records, writer, indent=4, sort_keys=True)


if __name__ == '__main__':
    parse_google_spreadsheet(SHEET)
