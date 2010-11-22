from setuptools import setup, find_packages

version = '0.1'

setup(name='cinezune.locaciones',
      version=version,
      description="Locaciones para cinezune",
      long_description="""\
      Descripcion
      ------------
      Una locacion es un contenedor de imagenes que controla la manera 
      en que se accede a las imagenes.
      
      Cada locacion tiene campos privados y publicos.
      
      Para un usuario anonimo se muestra una lista de imagenes con marca de agua 
      y en formato pequenho.
      El administrador puede ver las imagenes en tamanho original.
""",
      # Get strings from http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=['Development Status :: 1 - Planning',
                   'Environment :: Web Environment',
                   'Framework :: Buildout',
                   'Framework :: Zope3',
                   'Framework :: ZODB',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                   'Natural Language :: Spanish',
                   'Topic :: Multimedia :: Graphics :: Presentation'
                   ],
      keywords="grok dolmen movie locations",
      author="Noe Nieto",
      author_email="tzicatl@gmail.com",
      url="http://noenieto.com",
      license="LGPL v2",
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cinezune'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'grok',
                        'grokui.admin',
                        'z3c.testsetup',
                        'grokcore.startup',
                        # Add extra requirements here
                        ],
      )
