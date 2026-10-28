"""仅下载真实的原始数据，不制造样本/缺失/标注。仅用Python标准库。
联网时运行: python 数据准备.py
若网络受限，请手动下载 housing.csv 放入 data/california_housing/ 后重运行。
"""
from pathlib import Path
from urllib.request import Request, urlopen
import shutil

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
HOUSING = DATA / "california_housing"
DATA.mkdir(exist_ok=True)
HOUSING.mkdir(exist_ok=True)

# 主源：ageron/handson-ml2 仓库（《Hands-On Machine Learning》配套数据集）
# 备用：jsDelivr CDN 加速镜像，内容与主源一致
URLS = [
    "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv",
    "https://cdn.jsdelivr.net/gh/ageron/handson-ml2@master/datasets/housing/housing.csv",
]

def download(url: str, path: Path):
    print(f"下载中：{url}")
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=120) as r, path.open("wb") as f:
        shutil.copyfileobj(r, f)
    print(f"已下载：{path}（{path.stat().st_size:,}字节）")

def get_housing():
    dest = HOUSING / "housing.csv"
    if dest.exists():
        print("California Housing数据已存在，略过下载")
        return
    for url in URLS:
        try:
            download(url, dest)
            return
        except Exception as e:
            print('该来源不可用，尝试下一个；原因：', e)
    raise OSError('全部来源均不可用，请按“数据来源与字段说明.md”手动下载')

if __name__=='__main__':
    for name,fn in [('California Housing',get_housing)]:
        try:
            fn()
        except OSError as e:
            print(f'[{name}] 暂未准备成功：{e}')
            print('请阅读“数据来源与字段说明.md”，手动下载并按目录摆放。')
    print('下载操作结束，请运行 原始数据核验.py。')
