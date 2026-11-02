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

"""Gymnasium env registration for the interception environments."""

from gymnasium.envs.registration import register

from .base_intercept_env import BaseInterceptEnv
from .high_level_env import HighLevelInterceptEnv
from .low_level_env import LowLevelInterceptEnv

register(
    id='D2DIntercept-HighLevel-v0',
    entry_point='shaheen_rl.envs.high_level_env:HighLevelInterceptEnv',
    max_episode_steps=400,
)

register(
    id='D2DIntercept-LowLevel-v0',
    entry_point='shaheen_rl.envs.low_level_env:LowLevelInterceptEnv',
    max_episode_steps=400,
)

__all__ = ['BaseInterceptEnv', 'HighLevelInterceptEnv', 'LowLevelInterceptEnv']
