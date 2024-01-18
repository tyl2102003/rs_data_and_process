import numpy as np
import pyrealsense2 as rs

pipeline = rs.pipeline()
config = rs.config()

pipeline_wrapper = rs.pipeline_wrapper(pipeline)
pipeline_profile = config.resolve(pipeline_wrapper)
device = pipeline_profile.get_device()

found_rgb = False
for s in device.sensors:
    if s.get_info(rs.camera_info.name) == 'RGB Camera':
        found_rgb = True
        break
if not found_rgb:
    print("The demo requires Depth camera with Color sensor")
    exit(0)

config.enable_stream(rs.stream.depth, rs.format.z16, 30)
config.enable_stream(rs.stream.color, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)

# Get stream profile and camera intrinsics
profile = pipeline.get_active_profile()
depth_profile = rs.video_stream_profile(profile.get_stream(rs.stream.depth))
depth_intrinsics = depth_profile.get_intrinsics()
w, h = depth_intrinsics.width, depth_intrinsics.height
print("Image width: %d, height: %d" % (w, h))


color_profile = rs.video_stream_profile(profile.get_stream(rs.stream.color))
color_intrinsics = depth_profile.get_intrinsics()
w, h = color_intrinsics.width, color_intrinsics.height
print("Image width: %d, height: %d" % (w, h))
print(depth_intrinsics)
print(color_intrinsics)