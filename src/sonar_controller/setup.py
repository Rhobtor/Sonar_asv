from setuptools import setup

package_name = 'sonar_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aceti',
    maintainer_email='aceti@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sonar_service=sonar_controller.service_sonar:main',
            'sonar_client=sonar_controller.client_sonar:main'
        ],
    },
)
