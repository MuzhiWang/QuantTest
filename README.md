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
Get index df: http://127.0.0.1:5000/get_stock_df?stock_id=000001&&start_date=2019-07-07&&end_date=2019-11-11&&date_type=1min&&index=True

Powershell: Invoke-RestMethod -Uri 'http://127.0.0.1:5000/get_stock_df?stock_id=000001&&start_date=2019-07-07&&end_date=2019-11-11&&date_type=1min'
```

```
Sync stocks with TDX local files: http://127.0.0.1:5000/sync_data/stocks_with_tdx_local_files
PS: Invoke-RestMethod 'http://127.0.0.1:5000/sync_data/stocks_with_tdx_local_files' -Method Post -Body (@{
	stock_ids=@('000001','000001.IDX')
	date_type='day'
} | ConvertTo-Json) -ContentType 'application/json'

```

```
Get all index blocks with stocks: http://localhost:5000/get_all_index_with_stocks
PS: Invoke-RestMethod -Method 'GET' -Uri 'http://localhost:5000/get_all_index_with_stocks'

```

```
Get industries name value pair: http://localhost:5000/get_industries?industry_code=sw_l1
PS:  Invoke-RestMethod -Method 'GET' -Uri 'http://localhost:5000/get_industries?industry_code=sw_l1'
# sw_l1 = 0 # 申万一级行业;
# sw_l2 = 1 # 申万二级行业;
# sw_l3 = 2 # 申万三级行业
# jq_l1 = 3 # 聚宽一级行业
# jq_l2 = 4 # 聚宽二级行业
# zjw = 5   # 证监会行业
```

```
Get industry stocks ids: http://localhost:5000/get_industry_stocks?code=801740
PS:  Invoke-RestMethod -Method 'GET' -Uri 'http://localhost:5000/get_industry_stocks?code=801740'

```

```
Get eight diamgrams scores strategy: http://localhost:5000/strategy/eight_diagrams_scores
PS:
*** Get industry scores: ***
 Invoke-RestMethod 'http://localhost:5000/strategy/eight_diagrams_scores' -Method Post -Body (@{
	block='industry'
	start_date='2019-09-25'
	end_date='2019-11-10'
	date_type='5min'
	ma_list=@('5d', '10d', '15d')
	industry_codes=@('852121')
} | ConvertTo-Json) -ContentType 'application/json'

*** Get index scores: ***
 Invoke-RestMethod 'http://localhost:5000/strategy/eight_diagrams_scores' -Method Post -Body (@{
	block='index'
	start_date='2019-09-25'
	end_date='2019-11-10'
	date_type='5min'
	ma_list=@('5d', '10d', '15d')
	index_names=@('zhongzheng100')
} | ConvertTo-Json) -ContentType 'application/json'
```

## Local hints:
```
Local python path:  C:\Users\wmz66\AppData\Local\Programs\Python\Python37
Local luanch server: C:\Users\wmz66\AppData\Local\Programs\Python\Python37\python.exe .\App\Server.py
```
