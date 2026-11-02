# Copyright 2024 Abdulrahman S. Al-Batati
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from glob import glob
import os

from setuptools import find_packages, setup

package_name = 'shaheen_rl'

setup(
    name=package_name,
    version='0.2.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config', 'mavros'), glob('config/mavros/*.yaml')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Abdulrahman S. Al-Batati',
    maintainer_email='asmalbatati@hotmail.com',
    description='Reinforcement learning for drone-to-drone interception (Gymnasium + SB3).',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'train = shaheen_rl.train:main',
            'evaluate = shaheen_rl.evaluate:main',
            'curriculum = shaheen_rl.curriculum:main',
            'train_intercept = shaheen_rl.aerogym_intercept.train_intercept:main',
            'evaluate_intercept = shaheen_rl.aerogym_intercept.evaluate_intercept:main',
            'policy_head = shaheen_rl.aerogym_intercept.policy_head:main',
        ],
    },
)
