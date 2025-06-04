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
        # 👇 ESTA línea es clave para incluir launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',  # pon tu nombre si quieres
    maintainer_email='user@todo.todo',
    description='Paquete de ejemplo con rosbag',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
