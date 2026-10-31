import argparse,json
from pathlib import Path
SIGNATURES=[("89504e470d0a1a0a","PNG"),("ffd8ff","JPEG"),("474946383761","GIF"),("474946383961","GIF"),("255044462d","PDF"),("504b0304","ZIP or Office archive"),("53514c69746520666f726d61742033","SQLite")]
def detect(path):
 head=Path(path).read_bytes()[:32].hex()
 for sig,name in SIGNATURES:
  if head.startswith(sig):return name
 return "unknown"
def main():
 a=argparse.ArgumentParser();a.add_argument("files",nargs="+");x=a.parse_args()
 print(json.dumps({p:detect(p) for p in x.files if Path(p).is_file()},indent=2))
if __name__=="__main__":main()
