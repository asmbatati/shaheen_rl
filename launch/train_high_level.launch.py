#!/usr/bin/env python3
# Copyright 2026 Abdulrahman S. Al-Batati
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

"""
Launch stage-1 (high-level PPO) interception training.

The simulation (drone_interception_sim interception.launch.py) must already be
running. This only starts the training process against it.
"""

import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    cfg = os.path.join(
        get_package_share_directory('shaheen_rl'), 'config', 'train_ppo_high_level.yaml'
    )
    return LaunchDescription(
        [
            DeclareLaunchArgument('config', default_value=cfg),
            DeclareLaunchArgument('timesteps', default_value='200000'),
            Node(
                package='shaheen_rl',
                executable='train',
                name='d2d_train',
                output='screen',
                arguments=[
                    '--stage',
                    'high',
                    '--config',
                    LaunchConfiguration('config'),
                    '--timesteps',
                    LaunchConfiguration('timesteps'),
                ],
            ),
        ]
    )
