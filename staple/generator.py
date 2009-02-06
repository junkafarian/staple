from os import listdir, makedirs
from os.path import abspath, isdir, isfile, join, exists
import shutil
import logging

log = logging.getLogger('staple.generator')

class Generator:
    
    def __init__(self, output_dir):
        
        if not isdir(output_dir):
            makedirs(output_dir)
        
        self.output_dir = abspath(output_dir)
        ##TODO: provide support for custom template dir
        self.template_dir = abspath('%s/templates' % __file__.rsplit('/',1)[0])
    
    def __call__(self, config_file):
        cf = open(config_file, 'r')
        urls = cf.readlines()
        cf.close()
        self.generate_layout_files(('/master.layout',))
        self.generate_template_files(urls)
        
    
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
        ##TODO: does not support generating folders
<<<<<<< HEAD:staple/generator.py
        print 'generating template files\n\n* ' + '* '.join(urls)
        log.info('generating template files\n\n* ' + '* '.join(urls))
=======
        log.info('generating template files\n\n* ' + '\n* '.join(urls))
>>>>>>> 682fe0181e58ebcbb6f0953157c6a2654352027c:staple/generator.py
        generated_files = []
        for url in urls:
            #try:
                url = url.replace('\n','').lstrip('/')
                generation_path = '%s/%s' % (self.output_dir, url)
                generation_dir = generation_path.rsplit('/',1)[0]
                if not isdir(generation_dir):
                    makedirs(generation_dir)
                shutil.copy('%s/index.html' % self.template_dir, generation_path)
                generated_files.append(url)
            # except:
            #     pass
        
        return generated_files
    

