from unittest import TestCase
from nose.tools import assert_true

from tempfile import mkdtemp, NamedTemporaryFile
from os.path import join, dirname, isdir
from os import rmdir, listdir
import shutil



class TestGenerator(TestCase):
    
    def setUp(self):
        self.output_dir = mkdtemp()
        from staple.generator import Generator
        self.generator = Generator(self.output_dir)
    
    def tearDown(self):
        shutil.rmtree(self.output_dir)
        del self.generator
    
    def test_generate_file(self):
        assert_true(
            'index.html' not in listdir(self.output_dir),
            'existing `index.html` in the output directory'
        )
        config = NamedTemporaryFile()
        config.write('/index.html')
        config.flush()
        self.generator(config.name)
        config.close()
        assert_true(
            'index.html' in listdir(self.output_dir),
            'did not create `index.html`'
        )
    
    def test_generate_dir(self):
        assert_true(
            'testdirectory' not in listdir(self.output_dir),
            'existing `testdirectory` in the output directory'
        )
        config = NamedTemporaryFile()
        config.write('/testdirectory/index.html')
        config.flush()
        self.generator(config.name)
        config.close()
        assert_true(
            'testdirectory' in listdir(self.output_dir),
            'did not create `testdirectory`'
        )
        assert_true(
            isdir(join(self.output_dir, 'testdirectory')),
            '`testdirectory` is not valid directory'
        )
    
    # def test_render_none_template_file():
    #     pass
    # 
    # def test_render_file_as_dir():
    #     pass
    # 
    # def test_render_dir_as_file():
    #     pass
    # 


class TestPublisher(TestCase):

    def setUp(self):
        self.output_dir = mkdtemp()
        self.template_dir = join(dirname(__file__), 'templates')
        from staple.publisher import Publisher
        self.publisher = Publisher(self.template_dir)
    
    def tearDown(self):
        shutil.rmtree(self.output_dir)
        del self.publisher
    
    def test_publish_file(self):
        assert_true(
            'index.html' not in listdir(self.output_dir),
            'existing `index.html` in the output directory'
        )
        self.publisher(self.output_dir)
        assert_true(
            'index.html' in listdir(self.output_dir),
            'did not create `index.html`'
        )

    def test_publish_dir(self):
        assert_true(
            'one' not in listdir(self.output_dir),
            'existing `one` in the output directory'
        )
        self.publisher(self.output_dir)
        assert_true(
            'one' in listdir(self.output_dir),
            'did not create `one`'
        )
        assert_true(
            isdir(join(self.output_dir, 'one')),
            '`one` is not valid directory'
        )

