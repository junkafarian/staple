from os import listdir, makedirs, walk
from os.path import abspath, isdir, isfile, join, exists
# from ConfigParser import ConfigParser
import logging

# dependencies
from jinja2 import Environment, FileSystemLoader

log = logging.getLogger('staple.publisher')

class Publisher:
    
    def __init__(self, template_dir, config_file=None):
        # check values
        if not isdir(template_dir):
            raise Exception("Template path does not exist: %s" % template_dir)
        
        self.template_dir = abspath(template_dir)
        
        self.template_env = Environment(loader=FileSystemLoader(self.template_dir))
        
        if config_file:
            # config = ConfigParser(
            #         {''}
            #     )
            # 
            # self.config = config
            # parse extra variables out of config file
            pass
    
    def __call__(self, output_dir='./'):
        if not isdir(output_dir):
            makedirs(output_dir)
        self.output_dir = abspath(output_dir)
        # publish the root
        #self.publishdir('./')
        
        for path, dirnames, filenames in walk(self.template_dir):
            relative_path = path.replace(self.template_dir, '')
            # make sure we have a value for the root folder
            if not relative_path.startswith('/'):
                relative_path = '/' + relative_path
            # make it relative for os.path.join
            relative_path = '.' + relative_path
            for d in dirnames:
                if not isdir(join(relative_path, d)) and not d.startswith(('.','_')):
                    makedirs(join(relative_path, d))
            for f in filenames:
                if not f.startswith(('.','_')) and f.endswith('.html'):
                    self.publishfile(join(relative_path, f))
            
    
    def publishfile(self, path):
        log.debug('publishing file %s' % path)
        template = self.template_env.get_template(path)
        
        # open the file
        try:
            output = open(join(self.output_dir, path), 'w')
            #print >>output, template.render()
            output.write(template.render())
            output.close()
        except IOError:
            self.publishdir(path.rsplit('/', 1)[0])
    
    
    def publishdir(self, path): # depricated
        log.debug('publishing directory %s' % path)
        if not exists(join(self.output_dir, path)):
            makedirs(join(self.output_dir, path))
        current_dir = join(self.template_dir, path)
        for item in listdir(current_dir):
            if not(item.startswith('.') or item.startswith('_')):
                new_path = '%s/%s' % (path, item)
                new_abpath = join(self.template_dir, new_path)
                if isdir(new_abpath):
                    self.publishdir(new_path)
                elif isfile(new_abpath) and item.endswith('.html'):
                    self.publishfile(new_path)
    

