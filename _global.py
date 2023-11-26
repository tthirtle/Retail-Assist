from PySimpleGUI import FILE_TYPES_ALL_FILES
# Configuration options

database_file:str = ''
use_alt_description:bool = True
config_file:str = "config.ini"
single_user_mode:bool = True

logo_file:str = ''
use_logo:bool = True

put_contact_on_reports:bool = False

# User information - no passwords are stored

current_user = None

class user:
    def __init__(self,f_name:str,l_name:str,suffix:str=None,username=None,tel:str='',email:str='') -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.suffix = suffix
        if single_user_mode == False:
            self.username = str(username)
        self.tel = tel
        self.email = email
    def get_f_name(self):
        return self.f_name
    def get_l_name(self):
        return self.l_name
    def  get_suffix(self):
        return self.suffix
    def get_name(self):
        return f"{self.f_name} {self.l_name} {self.suffix}"
    def get_username(self):
        return self.username
    def get_tel(self):
        return self.tel
    def get_tel_print(self):
        return f"tel: {self.tel}"
    def get_email(self):
        return self.email
    def get_email_print(self):
        return self.email
    

# Item information

current_item = None

class item:
    def __init__(self,desc:str,upc:str,alt_desc:str=None,num:str=None,alt_lookup:str=None,brand:str=None,size:str=None,units:str=None) -> None:
        self.desc = desc
        self.upc = upc
        self.alt_desc = alt_desc
        self.num = num # Internal reorder number if diffrent from UPC
        self.alt_lookup = alt_lookup
        self.brand = brand
        self.size = size # Numeric size
        self.units = units # Units (gal,Oz,g...)
    def get_descript_display(self):
        return self.desc
    def get_descript_alt(self):
        return self.alt_desc
    def get_upc(self):
        return self.upc
    def get_num(self):
        return self.num
    def get_alt_lookup(self):
        return self.alt_lookup
    def get_brand(self):
        return self.brand
    def get_size(self):
        return self.size
    def get_units(self):
        return self.units

# Store information

current_store = None

class store:
    def __init__(self,name:str,number:str,add1:str=None,add2:str=None,city:str=None,state:str=None,zip:str=None) -> None:
        self.name = name
        self.number = number
        self.add1 = add1
        self.add2 = add2
        self.city = city
        self.state = state
        self.zip = zip
    def get_name(self):
        return self.name
    def get_number(self):
        return self.number
    def get_add1(self):
        return self.add1
    def get_add2(self):
        return self.add2
    def get_city(self):
        return self.city
    def get_state(self):
        return self.state
    def get_zip(self):
        return self.zip
    def get_address_full(self):
        return f"{self.add1}\n{self.add2}\n{self.city} {self.zip}"


# File extensions

excel_file_ext:tuple = (('Microsoft Excel 2007+ File','*.xlsx'),(FILE_TYPES_ALL_FILES[0]))
csv_file_ext:tuple = (('Comma Separated Values','*.csv'),(FILE_TYPES_ALL_FILES[0]))
pdf_file_ext:tuple = (("Adobe Acrobat File",'*.pdf'),(FILE_TYPES_ALL_FILES[0]))
img_file_ext:tuple = (("All supported formats",'*.png *.jpg *.bmp'),(FILE_TYPES_ALL_FILES[0]))

