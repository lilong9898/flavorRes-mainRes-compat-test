#! /usr/bin/python3.5
#coding=utf-8

import os;

isTest = True;

# git仓库的完整路径
GIT_REPO_REAL_PATH = "/home/lilong/hooktest/" if isTest else "/home/lilong/iReader_oppo/";

# productFlavor
PRODUCT_FLAVOR = "oppo" if isTest else "Oppo";

# main/res目录的完整路径
DIR_MAIN_RES_REAL_PATH = os.path.join(GIT_REPO_REAL_PATH, "main") + os.sep if isTest else os.path.join(GIT_REPO_REAL_PATH, "iReader", "src", "main", "res") + os.sep;

# productFlavor/res目录的完整路径
DIR_PRODUCT_FLAVOR_RES_REAL_PATH = os.path.join(GIT_REPO_REAL_PATH, "oppo") + os.sep if isTest else os.path.join(GIT_REPO_REAL_PATH, "iReader", "src", PRODUCT_FLAVOR, "res") + os.sep;

# res目录下要参与检测的子目录
RES_SUB_DIR_PATHS = ("layout", ) if isTest else ("layout", );
