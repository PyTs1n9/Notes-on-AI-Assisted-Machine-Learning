"""仅下载真实的原始数据，不制造样本/缺失/标注。仅用Python标准库。
联网时运行: python 数据准备.py
若校网限制外网，请手动通过来源文档下载zip到 data/downloads/ 后重运行。
"""
from pathlib import Path
from urllib.request import Request, urlopen
from zipfile import ZipFile, BadZipFile
import shutil

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
DL = DATA / "downloads"
BIKE = DATA / "bike_sharing"
DATA.mkdir(exist_ok=True)
DL.mkdir(exist_ok=True)
BIKE.mkdir(exist_ok=True)

URLS = {
    "bike": "https://archive.ics.uci.edu/static/public/275/bike%2Bsharing%2Bdataset.zip",
}
MIRRORS = {
    "hour.csv": "https://raw.githubusercontent.com/udacity/deep-learning/master/first-neural-network/Bike-Sharing-Dataset/hour.csv",
    "day.csv": "https://raw.githubusercontent.com/udacity/deep-learning/master/first-neural-network/Bike-Sharing-Dataset/day.csv",
}

def download(url: str, path: Path):
    print(f"下载中：{url}")
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=120) as r, path.open("wb") as f:
        shutil.copyfileobj(r, f)
    print(f"已下载：{path}（{path.stat().st_size:,}字节）")

def get_bike():
    if all((BIKE / f).exists() for f in MIRRORS):
        print("UCI数据已存在，略过下载")
        return
    zp = DL / "bike_sharing_uci.zip"
    try:
        if not zp.exists():
            download(URLS["bike"], zp)
        with ZipFile(zp) as z:
            for fname in MIRRORS:
                hits=[p for p in z.namelist() if p.endswith('/'+fname) or p==fname]
                if not hits:
                    raise FileNotFoundError(f"UCI包内不存在 {fname}")
                (BIKE / fname).write_bytes(z.read(hits[0]))
    except Exception as e:
        print('官方ZIP不可用，尝试公开镜像；原因：',e)
        for fname, url in MIRRORS.items():
            if not (BIKE / fname).exists():
                download(url,BIKE/fname)

if __name__=='__main__':
    for name,fn in [('UCI Bike Sharing',get_bike)]:
        try:
            fn()
        except (OSError, BadZipFile, ValueError) as e:
            print(f'[{name}] 暂未准备成功：{e}')
            print('请阅读“数据来源与字段说明.md”，手动下载并按目录摆放。')
    print('下载操作结束，请运行 原始数据核验.py。')
