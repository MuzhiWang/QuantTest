# Dependencies
```
pip3 install tushare -i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install pandas
pip3 install requests
pip3 install lxml
pip3 install beautifulsoup4
pip3 install matplotlib
pip3 install pymongo
pip3 install pytdx
pip3 install jqdatasdk
pip3 install flask
```

```
python dependency not correct, so that the site-package could not be found:
- find related python
- .\python.exe -m pip install flask

```

# MongoDB initialization
```
mkdir D:\Data\mongodb\db
mkdir D:\Data\mongodb\log
{mongodb_path}\mongod.exe  --dbpath D:\Data\mongodb\db
```
