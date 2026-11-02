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

"""Launch evaluation of a trained interception policy against the running sim."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument('stage', default_value='high'),
            DeclareLaunchArgument('model', default_value='checkpoints/high/final_model.zip'),
            DeclareLaunchArgument('episodes', default_value='10'),
            Node(
                package='shaheen_rl',
                executable='evaluate',
                name='d2d_evaluate',
                output='screen',
                arguments=[
                    '--stage',
                    LaunchConfiguration('stage'),
                    '--model',
                    LaunchConfiguration('model'),
                    '--episodes',
                    LaunchConfiguration('episodes'),
                ],
            ),
        ]
    )
