from build import build
import shutil
import os
import time
from tool import START_TIME, copy_overwrite

OUTPUT_DIR = os.path.join(os.path.dirname(__file__),'output')

def main():
    print(START_TIME)
    print('## 主程序运行')
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.mkdir(OUTPUT_DIR)
    build()

main()