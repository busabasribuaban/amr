from setuptools import find_packages, setup

package_name = 'dynamic_tf_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jetsonorinnano',
    maintainer_email='budsaba.sai@mail.kmutt.ac.th',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dynamic_tf_publisher = dynamic_tf_publisher.dynamic_tf_publisher:main',  # เพิ่มบรรทัดนี้
        ],
    },
)

