#!/usr/bin/env python

import setuptools

setup_kwargs = { 'author': 'Peter Boin',
  'author_email': 'peter.boin+cqparts@gmail.com',
  'classifiers': [ 'Intended Audience :: Developers',
                   'Intended Audience :: Manufacturing',
                   'Intended Audience :: End Users/Desktop',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: Apache Software License',
                   'Natural Language :: English',
                   'Operating System :: MacOS',
                   'Operating System :: POSIX',
                   'Operating System :: Unix',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Multimedia :: Graphics :: 3D Modeling',
                   'Topic :: Multimedia :: Graphics :: 3D Rendering',
                   'Development Status :: 3 - Alpha'],
  'description': 'Hierarchical and deeply parametric models using cadquery',
  'install_requires': [ 'cadquery',
                        'six',
                        'numpy',
                        'Jinja2',
                        'tinydb',
                        'requests'],
  'keywords': ['cadquery', 'cad', '3d', 'modeling'],
  'license': 'Apache Public License 2.0',
  'long_description': '\n'
                      '.. image:: '
                      'https://cqparts.github.io/cqparts/media/logo/dark.svg\n'
                      '    :align: center\n'
                      '\n'
                      '=====================\n'
                      'What is `cqparts`?\n'
                      '=====================\n'
                      '\n'
                      '``cqparts`` is CAD for Python programmers, short for '
                      '"``cadquery`` parts".\n'
                      '\n'
                      'Using ``cqparts`` you can wrap geometry made with '
                      '``cadquery`` to build complex\n'
                      'and deeply parametric models.\n'
                      '\n'
                      'Full documentation at: '
                      'https://cqparts.github.io/cqparts\n'
                      '\n'
                      '\n'
                      'Installing\n'
                      '------------------\n'
                      '\n'
                      'Pre-requisites\n'
                      '^^^^^^^^^^^^^^^^^^\n'
                      '\n'
                      "You'll need to fulfill the requirements of "
                      '``cadquery``, the simplest way to do\n'
                      'that is to install ``cadquery`` first by following the '
                      'instructions here:\n'
                      '\n'
                      'http://dcowden.github.io/cadquery/installation.html\n'
                      '\n'
                      'PyPI\n'
                      '^^^^^^^^^\n'
                      '\n'
                      'Once ``cadquery`` is installed, install ``cqparts`` '
                      'with::\n'
                      '\n'
                      '    pip install cqparts\n'
                      '\n'
                      '\n'
                      '``cqparts_*`` Content Libraries\n'
                      '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n'
                      '\n'
                      'You can also install content libraries with a similar '
                      '``pip install`` command.\n'
                      '\n'
                      'List available libraries with::\n'
                      '\n'
                      '    pip search cqparts-\n'
                      '\n'
                      'For example, to install the ``cqparts_bearings`` '
                      'content library, run::\n'
                      '\n'
                      '    pip install cqparts-bearings\n'
                      '\n'
                      '\n'
                      '_Note_: ``pip`` packages use ``-`` to separate words, '
                      'but when importing them the\n'
                      'standard ``_`` is used.\n'
                      '\n'
                      '\n'
                      'Example Usage\n'
                      '-------------------\n'
                      '\n'
                      'Here is just one of the simplest examples to give you '
                      'an idea of what this\n'
                      'library does.\n'
                      '\n'
                      'More detailed examples found in\n'
                      '`the official documentation for cqparts '
                      '<https://cqparts.github.io/cqparts/doc>`_.\n'
                      '\n'
                      'Wrapping a Cube\n'
                      '^^^^^^^^^^^^^^^^^^\n'
                      '\n'
                      '.. image:: '
                      'https://cqparts.github.io/cqparts/media/img/unit-cube.png\n'
                      '\n'
                      'A simple cube defined with ``cadquery`` alone::\n'
                      '\n'
                      '    # create unit cube solid\n'
                      '    import cadquery\n'
                      '    size = 10\n'
                      "    cube = cadquery.Workplane('XY').box(size, size, "
                      'size)\n'
                      '\n'
                      '    # display cube (optional)\n'
                      '    from Helpers import show\n'
                      '    show(cube)\n'
                      '\n'
                      'Wrapping this in a ``cqparts.Part`` object can be done '
                      'like this::\n'
                      '\n'
                      '    # create unit cube as cqparts.Part\n'
                      '    import cadquery\n'
                      '    import cqparts\n'
                      '    from cqparts.params import PositiveFloat\n'
                      '\n'
                      '    class MyCube(cqparts.Part):\n'
                      '        size = PositiveFloat(1, doc="cube size")\n'
                      '        def make(self):\n'
                      '            return '
                      "cadquery.Workplane('XY').box(self.size, self.size, "
                      'self.size)\n'
                      '\n'
                      '    # create cube instance\n'
                      '    cube = MyCube(size=10)\n'
                      '\n'
                      '    # display cube (optional)\n'
                      '    from cqparts.display import display\n'
                      '    display(cube)\n'
                      '\n'
                      'You can see that under the bonnet (in the ``make`` '
                      'function) the geometry is\n'
                      'created with ``cadquery``, but the resulting ``MyCube`` '
                      'class is instantiated\n'
                      'more intuitively, and more object orientated.\n'
                      '\n'
                      '\n'
                      'Creating a Hierarchy\n'
                      '^^^^^^^^^^^^^^^^^^^^^^\n'
                      '\n'
                      '``cqparts`` can also be used to create a deep hierarchy '
                      'of *parts* and\n'
                      '*assemblies* to build something deeply complicated and '
                      'entirely parametric.\n'
                      '\n'
                      'A simple example of this is the\n'
                      '`toy car tutorial '
                      '<https://cqparts.github.io/cqparts/doc/tutorials/assembly.html>`_.\n'
                      '\n'
                      '.. image:: '
                      'https://cqparts.github.io/cqparts/media/img/toy-car.png\n'
                      '\n'
                      '\n'
                      '``cqparts`` Capabilities\n'
                      '^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n'
                      '\n'
                      'The work done in ``cqparts_fasteners`` is a good '
                      'example of how useful\n'
                      '``cqparts`` wrapping can be; read about the '
                      '``Fastener`` class, how it works,\n'
                      'and what can be done with it in the\n'
                      '`cqparts_fasteners docs '
                      '<https://cqparts.github.io/cqparts/doc/cqparts_fasteners/index.html>`_\n'
                      '\n'
                      '.. image:: '
                      'https://cqparts.github.io/cqparts/media/img/nut-bolt-fastener.png\n'
                      '\n'
                      '\n'
                      'Contributing\n'
                      '-----------------\n'
                      '\n'
                      'Issues, and Pull Requests are encouraged, and happily '
                      'received, please read\n'
                      '`CONTRIBUTING.md '
                      '<https://github.com/fragmuffin/cqparts/blob/master/CONTRIBUTING.md>`_\n'
                      'for guidance on how to contribute.\n',
  'maintainer': 'Peter Boin',
  'maintainer_email': 'peter.boin+cqparts@gmail.com',
  'name': 'cqparts',
  'package_data': { '': [ 'LICENSE',
                          'display/web-template/*',
                          'display/web-template/model/*',
                          'display/web-template/static/*',
                          'display/web-template/static/js/*',
                          'display/web-template/static/css/*']},
  'packages': [ 'cqparts',
                'cqparts.display',
                'cqparts.utils',
                'cqparts.codec',
                'cqparts.catalogue',
                'cqparts.constraint',
                'cqparts.params'],
  'scripts': [],
  'url': 'https://github.com/fragmuffin/cqparts',
  'version': '0.2.2.dev1',
  'zip_safe': False}

setuptools.setup(**setup_kwargs)