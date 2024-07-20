"""Some functions for server.py that may """


import os

# Partially copied from bible_import.move_rvbible_propresenter_folder
def get_sideload_folder():
    if system_str == 'Windows':
        program_data = os.getenv('PROGRAMDATA')
        propresenter_bible_location = os.path.join(program_data,
                                                   'RenewedVision\ProPresenter\Bibles\sideload')
        os.makedirs(propresenter_bible_location, exist_ok=True)
    elif system_str == 'Darwin':
        propresenter_bible_location = '/Library/Application Support/RenewedVision/RVBibles/v2/'
    return propresenter_bible_location
