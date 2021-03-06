import datetime, os
from pathlib import Path
import numpy as np

def day_folder(root_folder):
    return os.path.join(root_folder, datetime.datetime.now().strftime("%Y_%m_%d"))

def second_folder(day_folder):
    return os.path.join(day_folder, datetime.datetime.now().strftime("%H-%M-%S"))

def create_day_folder(root_folder):
    Path(day_folder(root_folder)).mkdir(parents=True, exist_ok=True)

def create_second_folder(day_folder):
    Path(second_folder(day_folder)).mkdir(parents=True, exist_ok=True)
    
def generate_filename_path(root_folder,
                           filename = '', extension='txt',
                           with_microseconds=False):

    Day_folder = day_folder(root_folder)
    Second_folder = second_folder(Day_folder)
    
    if not os.path.exists(Day_folder):
        print('creating the folder "%s"' % Day_folder)
        Path(Day_folder).mkdir(parents=True, exist_ok=True)
    
    if not os.path.exists(Second_folder):
        print('creating the folder "%s"' % Second_folder)
        Path(Second_folder).mkdir(parents=True, exist_ok=True)
        
    if not extension.startswith('.'):
        extension='.'+extension
    
    return os.path.join(Second_folder, filename+extension)

#########################################################
#### NPZ files
#########################################################

def save_dict(filename, data):

    if '.npz' not in filename:
        print('/!\ The filename need to have the "npz" extension')
        print('        ------- renamed to:', filename+'.npz')
        np.savez(filename+'.npz', **data)
    else:
        np.savez(filename, **data)

def load_dict(filename):

    data = np.load(filename, allow_pickle=True)
    output = {}
    for key in data.files:
        output[key] = data[key]

        if type(output[key]) is np.ndarray:
            try:
                output[key] = output[key].item()
            except ValueError:
                pass
        
    return output


if __name__=='__main__':


    
    # print(filename_with_datetime('', folder='./', extension='.npy'))
    # print(filename_with_datetime('', folder='./', extension='npy'))
    
    create_day_folder('/home/yann/DATA/')
    fn = generate_filename_path('/home/yann/DATA/', 'visual-stim.npz')
    print(fn)
