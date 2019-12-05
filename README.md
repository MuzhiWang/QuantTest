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
pip3 install flask-cors
pip3 install pyinstaller
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


# Local server api:
```
Get stock df: http://127.0.0.1:5000/get_stock_df?stock_id=000001&&start_date=2019-07-07&&end_date=2019-11-11&&date_type=1min
Powershell: Invoke-RestMethod -Uri 'http://127.0.0.1:5000/get_stock_df?stock_id=000001&&start_date=2019-07-07&&end_date=2019-11-11&&date_type=1min'
```

```
Sync stocks with TDX local files: http://127.0.0.1:5000/sync_stocks_with_tdx_local_files
PS: Invoke-RestMethod 'http://127.0.0.1:5000/sync_stocks_with_tdx_local_files' -Method Post -Body (@{
	stock_ids=@('000001','000001.IDX')
	date_type='day'
} | ConvertTo-Json) -ContentType 'application/json'

```

## Local hints:
```
Local python path:  C:\Users\wmz66\AppData\Local\Programs\Python\Python37
Local luanch server: C:\Users\wmz66\AppData\Local\Programs\Python\Python37\python.exe .\App\Server.py
```
