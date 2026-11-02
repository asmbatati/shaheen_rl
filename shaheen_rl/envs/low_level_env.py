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
Low-level interception env (curriculum stage 2).

The agent outputs body angular rates + collective thrust (the expressive but
hard-to-train interface). Observation is extended with the interceptor's
orientation (quaternion) and body angular velocity, which attitude/rate control
needs. Train with an off-policy algorithm (SAC) for sample efficiency.
"""

from gymnasium import spaces
import numpy as np

from .base_intercept_env import BaseInterceptEnv


class LowLevelInterceptEnv(BaseInterceptEnv):
    """Action = [roll_rate, pitch_rate, yaw_rate, thrust] (rates scaled to r_max)."""

    def __init__(self, config=None, ros=None):
        self.r_max = (config or {}).get('r_max', 3.0)
        super().__init__(config=config, ros=ros)

    def _extra_obs_dim(self):
        return 7  # quaternion (4) + body angular velocity (3)

    def _extra_obs(self, interceptor_odom):
        if interceptor_odom is None:
            return np.zeros((7,), dtype=np.float32)
        q = interceptor_odom.pose.pose.orientation
        w = interceptor_odom.twist.twist.angular
        return np.array([q.x, q.y, q.z, q.w, w.x, w.y, w.z], dtype=np.float32)

    def _build_action_space(self):
        return spaces.Box(
            low=np.array([-1, -1, -1, 0], dtype=np.float32),
            high=np.array([1, 1, 1, 1], dtype=np.float32),
            dtype=np.float32,
        )

    def _apply_action(self, action):
        rr = float(np.clip(action[0], -1, 1)) * self.r_max
        pr = float(np.clip(action[1], -1, 1)) * self.r_max
        yr = float(np.clip(action[2], -1, 1)) * self.r_max
        thrust = float(np.clip(action[3], 0.0, 1.0))
        self.ros.publish_attitude_rate(rr, pr, yr, thrust)
