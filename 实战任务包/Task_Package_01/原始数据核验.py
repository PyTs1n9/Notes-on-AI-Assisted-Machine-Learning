"""检查原始数据是否准备成功，不执行数据清洗或建模（）。"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parent
DATA = ROOT/'data'
for fn,expected,fields in [('hour.csv',17379,17),('day.csv',731,16)]:
    p=DATA/'bike_sharing'/fn
    if not p.exists():
        print('[缺失]',p)
        continue
    with p.open('r',encoding='utf-8-sig',newline='') as f:
        rdr=csv.reader(f)
        head=next(rdr)
        cnt=sum(1 for _ in rdr)
    ok=(cnt==expected and len(head)==fields)
    status = '通过' if ok else '异常'
    print(f'[{status}] {fn}：{cnt}条，{len(head)}字段；期望 {expected}条、{fields}字段')
images=DATA/'coco128'/'images'/'train2017'
labels=DATA/'coco128'/'labels'/'train2017'
if images.exists() and labels.exists():
    pics=[p for p in images.iterdir() if p.suffix.lower() in ('.jpg','.jpeg','.png')]
    txt=list(labels.glob('*.txt'))
    status = '通过' if len(pics) == 128 else '异常'
    print(f'[{status}] COCO128图片：{len(pics)} 张；标签TXT：{len(txt)} 个（请学生检查空/缺标签）')
else:
    print('[缺失] COCO128图片或标签目录；请检查数据下载及解压路径')
