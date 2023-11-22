from PySimpleGUI import FILE_TYPES_ALL_FILES
# Configuration options

database_file:str = ''
use_alt_description:bool = True
config_file:str = "config.ini"
single_user_mode:bool = True

logo_file:str = ''
use_logo:bool = True

put_contact_on_reports:bool = False

# User information

current_user = ''

class user:
    def __init__(self,f_name:str,l_name:str,username=None,tel:str='',email:str='') -> None:
        self.f_name = f_name
        self.l_name = l_name
        if single_user_mode == False:
            self.username = str(username)
        self.tel = tel
        self.email = email


# File extensions

excel_file_ext:tuple = (('Microsoft Excel 2007+ File','*.xlsx'),(FILE_TYPES_ALL_FILES[0]))
csv_file_ext:tuple = (('Comma Separated Values','*.csv'),(FILE_TYPES_ALL_FILES[0]))
pdf_file_ext:tuple = (("Adobe Acrobat File",'*.pdf'),(FILE_TYPES_ALL_FILES[0]))
img_file_ext:tuple = (("All supported formats",'*.png *.jpg *.bmp'),(FILE_TYPES_ALL_FILES[0]))
