from tempfile import mkdtemp
from os.path import join
from os import rmdir

from publisher import publish, publishdir, publishfile

output_dir = mkdtemp()
template_dir = join(__file__, 'templates')

def buildup():
    pass


def teardown():
    rmdir(output_dir)


def test_render_page():
    pass


def test_render_dir():
    pass


def test_render_none_template_file():
    pass


def test_render_file_as_dir():
    pass


def test_render_dir_as_file():
    pass

