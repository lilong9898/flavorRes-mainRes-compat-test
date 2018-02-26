#! /usr/bin/python3.5
#coding=utf-8

import os;

# git仓库的完整路径
GIT_REPO_REAL_PATH = "/home/lilong/iReader_oppo/";

# productFlavor
PRODUCT_FLAVOR = "Oppo";

# main/res目录的完整路径
DIR_MAIN_RES_REAL_PATH = os.path.join(GIT_REPO_REAL_PATH, "iReader", "src", "main", "res") + os.sep;

# productFlavor/res目录的完整路径
DIR_PRODUCT_FLAVOR_REAL_PATH = os.path.join(GIT_REPO_REAL_PATH, "iReader", "src", PRODUCT_FLAVOR, "res") + os.sep;
