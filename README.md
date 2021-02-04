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

The first time you run this you will be prompted with a link in the terminal. Open the link in a web browser and login with google. You might be met with a warning afterwards, if so click 'Advanced' and continue through to the site. From here you can download the necessary secrets file. You will need to rename and move this file to this location;

```
{TOP_LEVEL_GIT_DIR}/client_secret.json
```

After that, `gdoc_parser.py` will have the information it needs to download the google sheets content.

<br />

To create the markdown files from the JSON, run this command;

```bash
python code/create_md_files.py
```