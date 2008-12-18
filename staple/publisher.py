from os import listdir, makedirs
from os.path import abspath, isdir, isfile, join, exists
from jinja2 import Environment, FileSystemLoader
import logging

log = logging.getLogger('staple.publisher')

class Publisher:
    
    def __init__(self, template_dir, output_dir='./', config_file=None):
        # check values
        if not isdir(template_dir):
            raise Exception("Template path does not exist: %s" % template_dir)
        if not isdir(output_dir):
            makedirs(output_dir)
        
        self.template_dir = abspath(template_dir)
        self.output_dir = abspath(output_dir)
        
        self.template_env = Environment(loader=FileSystemLoader(template_dir))
        
        if config_file:
            # parse extra variables out of config file
            pass
    
    def __call__(self):
        self.publishdir('./')
    
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
    
    
    def publishdir(self, path):
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
    

