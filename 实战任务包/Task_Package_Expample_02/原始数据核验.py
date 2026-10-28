"""检查原始数据是否准备成功，不执行数据清洗或建模（）。"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parent
DATA = ROOT/'data'
for fn,expected,fields in [('housing.csv',20640,10)]:
    p=DATA/'california_housing'/fn
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
