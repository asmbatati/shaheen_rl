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
High-level interception env (curriculum stage 1).

The agent outputs an ENU velocity command; PX4 handles stabilization. This is
the easiest-to-learn, most stable interface and the primary working env.
"""

import math

from gymnasium import spaces
import numpy as np

from .base_intercept_env import BaseInterceptEnv


class HighLevelInterceptEnv(BaseInterceptEnv):
    """Action = normalized ENU velocity setpoint in [-1, 1]^3 (scaled to v_max)."""

    def __init__(self, config=None, ros=None):
        self.v_max = (config or {}).get('v_max', 8.0)
        super().__init__(config=config, ros=ros)

    def _build_action_space(self):
        return spaces.Box(low=-1.0, high=1.0, shape=(3,), dtype=np.float32)

    def _apply_action(self, action):
        vx, vy, vz = (float(np.clip(a, -1.0, 1.0)) * self.v_max for a in action[:3])
        yaw = math.atan2(vy, vx)
        self.ros.publish_velocity_target(vx, vy, vz, yaw=yaw)
