from apiclient import discovery
from credentials import get_credentials
import httplib2
import simplejson

SPREAD_SHEET = '1BHVHR1-3DC-AJ1ZQUtGUOs25fiGrt0adwmZcSNDFMk0'
WORK_SHEETS = ['MainElements', 'ExploreElements', 'Filters', 'Consolidated']

def dict_from_sheet_values(rows):
    records = []
    headers = rows[0]

    for row in rows[1:]:
        record = {}

        for i, header in enumerate(headers):
            try:
                value = row[i]
            except IndexError:
                value = ""
            record[header] = value
        
        records.append(record)

    return records
            

def parse_google_spreadsheet():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
    service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)

    for work_sheet in WORK_SHEETS:
        result = service.spreadsheets().values().get(
            spreadsheetId=SPREAD_SHEET, 
            range=work_sheet
        ).execute()
        values = result.get('values', [])

        if not values:
            raise exception(f'No data found for {work_sheet}')

        records = dict_from_sheet_values(values)

        with open(f'content/json/{work_sheet}.json', "w") as writer:
            simplejson.dump(records, writer, indent=4, sort_keys=True)


if __name__ == '__main__':
    parse_google_spreadsheet()
