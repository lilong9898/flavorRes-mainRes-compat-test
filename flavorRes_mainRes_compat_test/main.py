#! /usr/bin/python3.5
#coding=utf-8

from git import Repo;
from config import *;
import os;

repo = Repo(GIT_REPO_REAL_PATH);

# 暂存区中所有main/res文件夹下的文件
listStrStagedFileRealPathsInMainRes = [];
# 暂存区中所有productFlavor/res文件夹下的文件
listStrStagedFileRealPathsInProductFlavorRes = [];
# 所有productFlavor/res文件夹下的文件
listStrFileRealPathsInProductFlavorRes = [];

# 暂存区中所有main/res文件夹下的文件，同时在文件系统的productFlavor/res文件夹下也出现的，但未在暂存区的productFlavor/res文件夹下出现的
# 这类文件是要进行警告的
listStrStagedFileRealPathsToWarn = [];

# 获取暂存区中所有main/res文件夹下的文件路径和所有productFlavor/res文件夹下的文件路径
for diff in repo.index.diff("HEAD"):
    if(diff.change_type == "M"):
        realResStagedFilePath = os.path.realpath(GIT_REPO_REAL_PATH + os.sep + diff.b_path)
        if(realResStagedFilePath.startswith(DIR_MAIN_RES_REAL_PATH)):
            listStrStagedFileRealPathsInMainRes.append(realResStagedFilePath);
        if(realResStagedFilePath.startswith(DIR_PRODUCT_FLAVOR_REAL_PATH)):
            listStrStagedFileRealPathsInProductFlavorRes.append(realResStagedFilePath);

# 获取所有productFlavor/res文件夹下的文件路径
for (path, d, filelist) in os.walk(DIR_PRODUCT_FLAVOR_REAL_PATH):
    for fileName in filelist:
        strFileRealPathInProductFlavorRes = os.path.join(path, fileName);
        listStrFileRealPathsInProductFlavorRes.append(strFileRealPathInProductFlavorRes);

# 统计需要警告的文件路径，这些路径在main/res和productFlavor/res中都存在，且在前者中有进入暂存区的修改，在后者中没有
for strStagedFileRealPathsInMainRes in listStrStagedFileRealPathsInMainRes:
    if strStagedFileRealPathsInMainRes.replace(DIR_MAIN_RES_REAL_PATH, DIR_PRODUCT_FLAVOR_REAL_PATH) in listStrFileRealPathsInProductFlavorRes and strStagedFileRealPathsInMainRes.replace(DIR_MAIN_RES_REAL_PATH, DIR_PRODUCT_FLAVOR_REAL_PATH) not in listStrStagedFileRealPathsInProductFlavorRes:
        listStrStagedFileRealPathsToWarn.append(strStagedFileRealPathsInMainRes);

# 如果没有危险
if(len(listStrStagedFileRealPathsToWarn) == 0):
    exit(0);

print()
print("=========================警告：%s/res覆盖main/res不完全============================"%(PRODUCT_FLAVOR));
print("这些文件在main的res下有进入暂存区的修改，在" + PRODUCT_FLAVOR + "的res下存在，而且没有进入暂存区的修改:");
print();

for path in listStrStagedFileRealPathsToWarn:
    print(path);

print();
print("这会导致" + PRODUCT_FLAVOR + "/res不能正确反映main/res下的修改!");
print("=================================================================================");
print();
