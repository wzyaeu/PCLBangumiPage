import os
import time
import shutil
import re
import secrets
import math
from typing import Any

with open('.version','r',encoding='utf-8') as f:
    VERSION = f.read()
BUILD_VERSION = secrets.token_hex(4)

HEADER = {
    'user-agent': 'wzyaeu/PclBangumiPage'
}

logs: dict[str,list[tuple[str,Any]]] = {}

def logs_add(region: str, name: str, result: Any):
    if region in logs:
        logs[region].append((name,result))
    else:
        logs[region] = [(name,result)]

def logs_result():
    return logs

ht = {}

def gett(tn: str, x:str = 'xaml') -> str:
    global ht
    if tn in ht.keys() :
        return ht[tn]
    else:
        with open(os.path.join(os.path.dirname(__file__),'template',tn+f'.{x}'), 'r', encoding='utf-8') as f:
            ht[tn] = f.read()
            return ht[tn]

def gettb(tn: str) -> bytes:
    with open(os.path.join(os.path.dirname(__file__),'template',tn), 'rb') as f:
        return f.read()

def savef(n, d: str):
    os.makedirs(os.path.dirname(os.path.join(os.path.dirname(__file__),'output',n)), exist_ok=True)
    with open(os.path.join(os.path.dirname(__file__),'output',n), 'w', encoding='utf-8') as f:
        f.write(d)

def savefb(n, d: bytes):
    os.makedirs(os.path.dirname(os.path.join(os.path.dirname(__file__),'output',n)), exist_ok=True)
    with open(os.path.join(os.path.dirname(__file__),'output',n), 'wb') as f:
        f.write(d)

def copy_overwrite(src_dir: str, dst_dir: str):
    os.makedirs(dst_dir, exist_ok=True)

    for root, _, files in os.walk(src_dir):
        rel_path = os.path.relpath(root, src_dir)
        target_dir = os.path.join(dst_dir, rel_path)
        os.makedirs(target_dir, exist_ok=True)

        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(target_dir, file)
            shutil.copy2(src_file, dst_file)

def y(s):
    return re.sub('> +<','><',re.sub('\n',' ',re.sub('\n +',' ',s)))