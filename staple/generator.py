from os import listdir, makedirs
from os.path import abspath, isdir, isfile, join, exists
import shutil
import logging

log = logging.getLogger('staple.generator')

class Generator:
    
    def __init__(self, output_dir, config_file):
        
        if not isdir(output_dir):
            makedirs(output_dir)
        
        self.output_dir = abspath(output_dir)
        ##TODO: provide support for custom template dir
        self.template_dir = abspath('%s/templates' % __file__.rsplit('/',1)[0])
        cf = open(config_file, 'r')
        self.urls = cf.readlines()
        cf.close()
    
    def __call__(self):
        self.generate_layout_files(('/master.layout',))
        self.generate_template_files(self.urls)
        
    
    def generate_layout_files(self, urls):
        log.debug('generating layout files %s' % urls)
        generated_files = []
        for url in urls:
            # try:
                url = url.replace('\n','').lstrip('/')
                shutil.copy('%s/master.layout' % self.template_dir, '%s/%s' % (self.output_dir, url))
                generated_files.append(url)
            # except:
            #     pass
        return generated_files
    
    
    def generate_template_files(self, urls):
        print 'generating layout files', urls
        generated_files = []
        for url in urls:
            #try:
                url = url.replace('\n','').lstrip('/')
                shutil.copy('%s/index.html' % self.template_dir, '%s/%s' % (self.output_dir, url))
                generated_files.append(url)
            # except:
            #     pass
        
        return generated_files
    

