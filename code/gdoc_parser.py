from apiclient import discovery
from credentials import get_credentials
import httplib2
import simplejson

SPREAD_SHEET = '1BHVHR1-3DC-AJ1ZQUtGUOs25fiGrt0adwmZcSNDFMk0'
WORK_SHEETS = ['MainElements', 'ExploreElements', 'FilterElements', 'Consolidated', 'FiltersConsol', 'PUPlotsConsol']

def empty_dict_check(dictionary):
    for value in dictionary.values():
        if value:
            return False
    
    return True

def dicts_from_sheet_values(rows):
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

def filters_consol_dicts_from_values(rows):
    records = []
    headers = [rows[0][0], rows[0][1], rows[0][4]]
    sub_headers = {headers[1]: rows[1][1:4], headers[2]: rows[1][4:7]}

    record = {}
    for row in rows[2:]:
        if row[0]:
            records.append(record)
            record = {}
            record[headers[0]] = row[0]
            record[headers[1]] = []
            record[headers[2]] = []
        
        main_dict = {}
        for i, main_sub_header in enumerate(sub_headers[headers[1]]):
            try:
                value = row[i+1]
            except IndexError:
                value = ""
            main_dict[main_sub_header] = value

        if not empty_dict_check(main_dict):
            record[headers[1]].append(main_dict)

        explore_dict = {}
        for i, explore_sub_header in enumerate(sub_headers[headers[2]]):
            try:
                value = row[i+4]
            except IndexError:
                value = ""
            explore_dict[explore_sub_header] = value

        if not empty_dict_check(explore_dict):
            record[headers[2]].append(explore_dict)

    return records[1:]


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
        
        if work_sheet == 'FiltersConsol':
            records = filters_consol_dicts_from_values(values)
        elif work_sheet == 'PUPlotsConsol':
            continue
        else:
            records = dicts_from_sheet_values(values)

        with open(f'content/json/{work_sheet}.json', "w") as writer:
            simplejson.dump(records, writer, indent=4, sort_keys=True)


if __name__ == '__main__':
    parse_google_spreadsheet()
