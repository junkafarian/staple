from os import listdir, makedirs
from os.path import abspath, isdir, isfile, join, exists
from jinja2 import Environment, FileSystemLoader

def generator(output_dir, config_file):
    
    output_dir = abspath(output_dir)
    
    

