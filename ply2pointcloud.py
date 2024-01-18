import open3d as o3d
# 读取ply文件并将其保存为pcd文件
def ply2pointcloud(ply_path):
    o3d_pcd = o3d.io.read_point_cloud(ply_path)
    print(o3d_pcd.has_colors())
    o3d_pcd.colors.clear() # 清除颜色信息
    print(o3d_pcd.has_colors()) # 检查颜色信息是否存在
    
    o3d.io.write_point_cloud("test1" + '.ply', o3d_pcd, write_ascii=True)
    

ply_path = './PLY_file/1705200551.ply'
ply2pointcloud(ply_path)
print('Finish!')