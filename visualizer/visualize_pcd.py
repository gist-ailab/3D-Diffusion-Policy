import zarr
import numpy as np
import visualizer

# Path to your Zarr file
zarr_filepath = "/home/bak/Projects/3D-Diffusion-Policy/3D-Diffusion-Policy/data/drill_40demo_1024.zarr"

try:
    # Load the point cloud data from the Zarr file.  Adjust this based on your Zarr's structure.
    # This assumes the point cloud is stored as a NumPy array under a key 'pointcloud' in the Zarr.
    # If it's in a different path or format, modify accordingly.
    zarr_data = zarr.open(zarr_filepath, mode='r')
    entire_pointcloud_data = zarr_data['data']['point_cloud'][:] # Load the entire array. For very large datasets, consider loading in chunks.
    pcd = entire_pointcloud_data[0] # Load the first point cloud in the dataset
   

    # Visualize the point cloud.  You can optionally provide a color tuple.
    visualizer.visualize_pointcloud(pcd)

except FileNotFoundError:
    print(f"Error: Zarr file not found at {zarr_filepath}")
except KeyError:
    print(f"Error: 'pointcloud' key not found in the Zarr file.")
except zarr.errors.ZarrError as e:
    print(f"Error opening or reading Zarr file: {e}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

