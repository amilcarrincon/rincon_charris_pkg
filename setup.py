import os
from glob import glob
from setuptools import setup

package_name = 'rincon_charris_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Amílcar Rincón',
    maintainer_email='amilcar@ejemplo.com',
    description='Paquete de ejemplo con rosbag y nodos personalizados',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'procesador_vision = rincon_charris_pkg.procesador_vision:main',
            'controlador_brazo = rincon_charris_pkg.controlador_brazo:main',
        ],
    },
)
