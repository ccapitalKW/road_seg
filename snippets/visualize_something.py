import open3d.visualization as viz


def visualize_point_cloud(pc) -> None:
    v = viz.Visualizer()
    v.create_window()
    opt = v.get_render_option()
    # blue = z, red = x, green = y
    opt.show_coordinate_frame = True

    # Add the point cloud to the visualizer
    v.add_geometry(pc)
    # Run the visualizer, push "Q" to exit and "h" for help when the window opens
    v.run()

    # Destroy the visualizer window
    v.destroy_window()