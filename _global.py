from PySimpleGUI import FILE_TYPES_ALL_FILES
# Configuration options

database_file = None
use_alt_description = True
config_file = "config.ini"

single_user_mode = True

# File extensions

excel_file_ext = (('Microsoft Excel 2007+ File','*.xlsx'),(FILE_TYPES_ALL_FILES[0]))
csv_file_ext = (('Comma Separated Values','*.csv'),(FILE_TYPES_ALL_FILES[0]))
pdf_file_ext = (("Adobe Acrobat File",'*.pdf'),(FILE_TYPES_ALL_FILES[0]))
img_file_ext = (("All supported formats",'*.png *.jpg *.bmp'),(FILE_TYPES_ALL_FILES[0]))
