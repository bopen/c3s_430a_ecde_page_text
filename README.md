# C3S 434 ECDE Page Text

To manage page text for the European Climate Data Explorer being developed by the C3S 434 project.


Example page for an ECDE indicator:
https://c3s.maris.nl/health/climatic-suitability-of-tiger-mosquito--season-length.html 

Existing method uses google docs to compile the text:  
https://docs.google.com/document/d/1U7znbhqq-xogrpcurqQOBQIh18SMNrdh4fXdNXZPo-s/edit 
These worked well when I was doing the thinking about what to include in the descriptions but they aren't suitable for managing the text as we make updates and scale up to include new indicators.

The new plan is to compile the indicator texts in a google sheet (like UKCP18) and then process the sheets to generate markdown text for the indicator pages.

Draft Google Sheet for ECDE indicators: https://docs.google.com/spreadsheets/d/1BHVHR1-3DC-AJ1ZQUtGUOs25fiGrt0adwmZcSNDFMk0/edit#gid=1104920491

## Usage ##

To download the google sheets data and parse it to JSON, run this command;

```bash
python code/gdoc_parser.py
```

The first time you run this, an exception will be raised and you will be prompted with a [link](https://developers.google.com/sheets/api/quickstart/python) in the terminal. Open the link in a web browser and go to step one where there is a button called `Enable the Google Sheets API`. Click this and follow the steps, call your project what you like (or just leave it as 'Quickstart') and choose `Desktop app`. You can then click `Download Client Configuration`. You will need to rename and move this file to this location;

```
{TOP_LEVEL_GIT_DIR}/client_secret.json
```

The next time you run `gdoc_parser.py` you'll be prompted with another link. Follow this and sign in with google, you'll be met with a page saying the `Google hasn't verified this app`, click `Advanced`, then `Go to Quickstart (unsafe)`. Then grant permission to view google spread sheets.


After that, `gdoc_parser.py` will have the information it needs to download the google sheets content.

<br />

To create the markdown files from the JSON, run this command;

```bash
python code/create_md_files.py
```