from build import build
import shutil
import os
import time
from tool import copy_overwrite, BUILD_VERSION

OUTPUT_DIR = os.path.join(os.path.dirname(__file__),'output')

def main():
    print(BUILD_VERSION)
    print('## 主程序运行')
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.mkdir(OUTPUT_DIR)
    build()

main()