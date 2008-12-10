from os import listdir, makedirs
from os.path import abspath, isdir, isfile, join, exists
from jinja2 import Environment, FileSystemLoader

def publish(template_dir, output_dir='./', config_file=None):
    
    # check values
    if not isdir(template_dir):
        raise Exception("Template path does not exist")
    if not isdir(output_dir):
        makedirs(output_dir)
    
    template_dir = abspath(template_dir)
    output_dir = abspath(output_dir)
    
    env = Environment(loader=FileSystemLoader(template_dir))
    
    if config_file:
        # parse extra variables out of config file
        pass
    
    def publishfile(path):
        print 'publishing ', path
        template = env.get_template(path)
        
        # open the file
        try:
            output = open(join(output_dir, path), 'w')
            output.write(template.render())
            output.close()
        except IOError:
            publishdir(path.rsplit('/', 1)[0])
        
    
    def publishdir(path):
        if not exists(join(output_dir, path)):
            makedirs(join(output_dir, path))
        current_dir = join(template_dir, path)
        for item in listdir(current_dir):
            if not(item.startswith('.') or item.startswith('_')):
                new_path = '%s/%s' % (path, item)
                new_abpath = join(template_dir, new_path)
                if isdir(new_abpath):
                    publishdir(new_path)
                elif isfile(new_abpath) and item.endswith('.html'):
                    publishfile(new_path)
    
    publishdir('./')
    

