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

"""Unit tests for the velocity-frame option (C7)."""

import math

import numpy as np
import pytest
from shaheen_rl.aerogym_intercept.obs_frame import apply_velocity_frame


def _state(yaw):
    q = [0.0, 0.0, math.sin(yaw / 2), math.cos(yaw / 2)]  # x, y, z, w
    return {'quaternion': np.array(q), 'velocity': np.array([1.0, 0.0, 0.5])}


def test_body_is_unchanged():
    s = apply_velocity_frame(_state(math.pi / 2), 'body')
    assert np.allclose(s['velocity'], [1.0, 0.0, 0.5])


def test_world_rotates_by_yaw():
    # facing +y and flying forward at 1 m/s is +y in the world
    s = apply_velocity_frame(_state(math.pi / 2), 'world')
    assert np.allclose(s['velocity'], [0.0, 1.0, 0.5], atol=1e-9)


def test_world_at_zero_yaw_matches_body():
    s = apply_velocity_frame(_state(0.0), 'world')
    assert np.allclose(s['velocity'], [1.0, 0.0, 0.5])


def test_unknown_frame_raises():
    with pytest.raises(ValueError):
        apply_velocity_frame(_state(0.0), 'ned')
