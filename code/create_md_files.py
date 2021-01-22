from mdutils.mdutils import MdUtils
import os
import simplejson


def write_md_files():
    with open('content/json/Consolidated.json') as reader:
        texts = simplejson.load(reader)

        for text in texts:
            title = text['Indicator']
            file_name = title.replace(' ', '_')
            base_path = f'content/markdown/consolidated'

            if not os.path.exists(base_path):
                os.makedirs(base_path)

            mdFile = MdUtils(file_name=os.path.join(base_path, file_name), title=title)
            
            mdFile.new_header(level=1, title='Main')
            mdFile.new_paragraph(text['ConsolidatedText_Main'])

            mdFile.new_header(level=1, title='Explore')
            mdFile.new_paragraph(text['ConsolidatedText_Explore'])

            mdFile.create_md_file()


if __name__ == '__main__':
    write_md_files()