import os
import shutil

# 当前脚本的目录
script_dir = os.path.dirname(os.path.realpath(__file__))

# 源文件的路径
source_path = os.path.join(script_dir, '3DPrintedMetricV3.xml')

# 目标目录的主路径
main_target_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'Autodesk', 'webdeploy', 'Production')

# 遍历主路径下的所有目录
for dir_name in os.listdir(main_target_dir):
    # 构造完整的目标路径
    full_target_dir = os.path.join(main_target_dir, dir_name, 'Fusion', 'Server', 'Fusion', 'Configuration', 'ThreadData')
    # 检查这个路径是否存在
    if os.path.exists(full_target_dir):
        # 目标文件的路径
        target_path = os.path.join(full_target_dir, 'a.xml')
        # 执行拷贝
        shutil.copyfile(source_path, target_path)
        print(f'Copied to {target_path}')