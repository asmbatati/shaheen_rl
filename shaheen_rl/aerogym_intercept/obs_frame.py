"""Frame of the interceptor's velocity in the observation (and reward).

MAVROS publishes the odom twist in the BODY frame. The checkpoints trained
before C7 feed it as-is, so ``'body'`` stays the default and they keep loading
and flying the same. ``'world'`` rotates it into the ENU world frame, where it
is consistent with ``target_velocity`` (already world) in the relative-velocity
block and with the line of sight in the reward's alignment term. A model must be
evaluated and flown in the frame it was trained in.

Pure numpy (no ROS), so it is unit-tested directly.
"""
from shaheen_guidance.frames import body_to_world

VELOCITY_FRAMES = ('body', 'world')


def check_velocity_frame(frame):
    """Return `frame` if it is a known velocity frame, else raise ValueError."""
    if frame not in VELOCITY_FRAMES:
        raise ValueError(f'velocity_frame must be one of {VELOCITY_FRAMES}, got {frame!r}')
    return frame


def apply_velocity_frame(state, frame):
    """Set ``state['velocity']`` in `frame`; `state` holds the raw body twist.

    Returns `state`, changed in place.
    """
    if check_velocity_frame(frame) == 'world':
        state['velocity'] = body_to_world(state['quaternion'], state['velocity'])
    return state
