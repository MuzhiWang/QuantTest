# TODO

- `Improve query df for range dates [2019-01-01, 2019-01-10]`
- Improve store dates in StockProvider
- Store valid stock dates and query it, from JQData get_trade_days store it on local
- For online provider, if the daily query data counts is not enough, should not store the data 
- update_one -> update_many for upserting batch dates' data
- Refactor tests
- `Add log system`
- Close open socket
- `Add annotation for func running time`
- Create Context to contains basic components such as logger, Utils etc.
- Support CUDA on calculating DF. install cuDF
- `Support multiple processes`
- Get history 1min data. From tdx get_history_minute_time_data()
- Improve daily df store in mongodb. Make each record with ONE year's df.





# Chuquan:
``` sh 600381
    year  month  day  category    name  fenhong  peigujia  songzhuangu  peigu     suogu  panqianliutong  panhouliutong  qianzongguben   houzongguben fenshu xingquanjia
0   2002      7    5         1    除权除息     0.65       0.0         0.00    0.0       NaN             NaN            NaN            NaN            NaN   None        None
1   2003      5   21         1    除权除息     0.68       0.0         0.00    0.0       NaN             NaN            NaN            NaN            NaN   None        None
2   2004      7   19         1    除权除息     0.00       0.0        10.00    0.0       NaN             NaN            NaN            NaN            NaN   None        None
3   2004      7   20         2   送配股上市      NaN       NaN          NaN    NaN       NaN     3500.000000    7000.000000   11000.000000   22000.000000   None        None
4   2005      5   12         1    除权除息     0.00       0.0         3.00    0.0       NaN             NaN            NaN            NaN            NaN   None        None
5   2005      5   13         2   送配股上市      NaN       NaN          NaN    NaN       NaN     7000.000000    9100.000000   22000.000000   28600.000000   None        None
6   2006     11   27         1    除权除息     0.00       0.0         2.24    0.0       NaN             NaN            NaN            NaN            NaN   None        None
7   2006     11   27         5    股本变化      NaN       NaN          NaN    NaN       NaN     9100.000000   11138.400391   28600.000000   30638.400391   None        None
8   2007     11   29         5    股本变化      NaN       NaN          NaN    NaN       NaN    11138.400391   12662.000000   30638.400391   30638.400391   None        None
9   2007     12   19         5    股本变化      NaN       NaN          NaN    NaN       NaN    12662.000000   14599.519531   30638.400391   30638.400391   None        None
10  2009      2    5         3  非流通股上市      NaN       NaN          NaN    NaN       NaN    14599.519531   16131.440430   30638.400391   30638.400391   None        None
11  2009     12    2         3  非流通股上市      NaN       NaN          NaN    NaN       NaN    16131.440430   30638.400391   30638.400391   30638.400391   None        None
12  2011      1   17         5    股本变化      NaN       NaN          NaN    NaN       NaN    30638.400391   30638.400391   30638.400391   45332.980469   None        None
13  2011      8   25         1    除权除息     0.00       0.0         5.00    0.0       NaN             NaN            NaN            NaN            NaN   None        None
14  2011      8   26         9   转配股上市      NaN       NaN          NaN    NaN       NaN    30638.400391   45957.601562   45332.980469   67999.468750   None        None
15  2011     12   23         5    股本变化      NaN       NaN          NaN    NaN       NaN    45957.601562   45957.601562   67999.468750   94226.203125   None        None
16  2012      5   15         1    除权除息     0.00       0.0         7.00    0.0       NaN             NaN            NaN            NaN            NaN   None        None
17  2012      5   16         9   转配股上市      NaN       NaN          NaN    NaN       NaN    45957.601562   78127.921875   94226.203125  160184.531250   None        None
18  2012     12   27         5    股本变化      NaN       NaN          NaN    NaN       NaN    78127.921875  118398.757812  160184.531250  160184.531250   None        None
19  2014      6   27        11     扩缩股      NaN       NaN          NaN    NaN  0.124185             NaN            NaN            NaN            NaN   None        None
20  2014      6   27         5    股本变化      NaN       NaN          NaN    NaN       NaN   118398.757812   18711.691406  160184.531250   19892.576172   None        None
21  2015      3   25         5    股本变化      NaN       NaN          NaN    NaN       NaN    18711.691406   18711.691406   19892.576172   68831.398438   None        None
22  2015      7    6         5    股本变化      NaN       NaN          NaN    NaN       NaN    18711.691406   19892.576172   68831.398438   68831.398438   None        None
23  2016      9   14         5    股本变化      NaN       NaN          NaN    NaN       NaN    19892.576172   19892.576172   68831.398438   68561.148438   None        None
24  2016      9   27         5    股本变化      NaN       NaN          NaN    NaN       NaN    19892.576172   20581.015625   68561.148438   68561.148438   None        None
25  2017      8    3         5    股本变化      NaN       NaN          NaN    NaN       NaN    20581.015625   20581.015625   68561.148438   63075.398438   None        None
26  2017      8   16         5    股本变化      NaN       NaN          NaN    NaN       NaN    20581.015625   21191.068359   63075.398438   63075.398438   None        None
27  2018      8    2         5    股本变化      NaN       NaN          NaN    NaN       NaN    21191.068359   21191.068359   63075.398438   58807.527344   None        None
28  2018      8   14         5    股本变化      NaN       NaN          NaN    NaN       NaN    21191.068359   58317.175781   58807.527344   58807.527344   None        None
29  2019      1    7         5    股本变化      NaN       NaN          NaN    NaN       NaN    58317.175781   58317.175781   58807.527344   58706.074219   None        None
30  2019      1   22         5    股本变化      NaN       NaN          NaN    NaN       NaN    58317.175781   58706.074219   58706.074219   58706.074219   None        None
2019-11-22 23:57:07,772 - Database.MongoDB.Client - DEBUG - test_tdx_client_get_xdxr_info (TestClients.TestClients) spend time: 3716.064929962158 ms

```

``` sz 000001
    year  month  day  category    name  fenhong  peigujia  songzhuangu  peigu suogu  panqianliutong  panhouliutong  qianzongguben  houzongguben fenshu xingquanjia
0   1990      3    1         1    除权除息    0.000      3.56          0.0    1.0  None             NaN            NaN            NaN           NaN   None        None
1   1991      4    3         5    股本变化      NaN       NaN          NaN    NaN  None    0.000000e+00   2.650000e+03   0.000000e+00  4.850017e+03   None        None
2   1991      5    2         1    除权除息    3.000      0.00          4.0    0.0  None             NaN            NaN            NaN           NaN   None        None
3   1991      5    2         2   送配股上市      NaN       NaN          NaN    NaN  None    2.650000e+03   3.949072e+03   4.850017e+03  8.975164e+03   None        None
4   1991      8   17         1    除权除息    0.000      0.00         10.0    0.0  None             NaN            NaN            NaN           NaN   None        None
5   1992      3   23         1    除权除息    2.000      0.00          5.0    0.0  None             NaN            NaN            NaN           NaN   None        None
6   1993      5   24         1    除权除息    3.000     16.00          8.5    1.0  None             NaN            NaN            NaN           NaN   None        None
7   1993      5   24         2   送配股上市      NaN       NaN          NaN    NaN  None    3.949072e+03   1.881298e+04   8.975164e+03  2.694179e+04   None        None
8   1993      6   30         2   送配股上市      NaN       NaN          NaN    NaN  None    1.881298e+04   1.800433e+04   2.694179e+04  2.612537e+04   None        None
9   1994      7    9         2   送配股上市      NaN       NaN          NaN    NaN  None    1.800433e+04   1.980477e+04   2.612537e+04  2.873791e+04   None        None
10  1994      7   11         1    除权除息    5.000      5.00          5.0    1.0  None             NaN            NaN            NaN           NaN   None        None
11  1994      7   14         2   送配股上市      NaN       NaN          NaN    NaN  None    1.980477e+04   2.970715e+04   2.873791e+04  4.310686e+04   None        None
12  1995      9   25         1    除权除息    3.000      0.00          2.0    0.0  None             NaN            NaN            NaN           NaN   None        None
13  1995      9   27         2   送配股上市      NaN       NaN          NaN    NaN  None    2.970715e+04   3.564858e+04   4.310686e+04  5.172824e+04   None        None
14  1996      5   27         1    除权除息    0.000      0.00         10.0    0.0  None             NaN            NaN            NaN           NaN   None        None
15  1996      5   29         2   送配股上市      NaN       NaN          NaN    NaN  None    3.564858e+04   7.144230e+04   5.172824e+04  1.034565e+05   None        None
16  1997      8   25         1    除权除息    2.000      0.00          5.0    0.0  None             NaN            NaN            NaN           NaN   None        None
17  1997      8   27         2   送配股上市      NaN       NaN          NaN    NaN  None    7.144230e+04   1.071634e+05   1.034565e+05  1.551847e+05   None        None
18  1999     10   18         1    除权除息    6.000      0.00          0.0    0.0  None             NaN            NaN            NaN           NaN   None        None
19  2000     11    6         1    除权除息    0.000      8.00          0.0    3.0  None             NaN            NaN            NaN           NaN   None        None
20  2000     12    8         2   送配股上市      NaN       NaN          NaN    NaN  None    1.071634e+05   1.393125e+05   1.551847e+05  1.945822e+05   None        None
21  2001     10   15         5    股本变化      NaN       NaN          NaN    NaN  None    1.393125e+05   1.409362e+05   1.945822e+05  1.945822e+05   None        None
22  2002      7   23         1    除权除息    1.500      0.00          0.0    0.0  None             NaN            NaN            NaN           NaN   None        None
23  2003      9   29         1    除权除息    1.500      0.00          0.0    0.0  None             NaN            NaN            NaN           NaN   None        None
24  2007      6   18         1    除权除息    0.000      0.00          1.0    0.0  None             NaN            NaN            NaN           NaN   None        None
25  2007      6   20         5    股本变化      NaN       NaN          NaN    NaN  None    1.409362e+05   1.550188e+05   1.945822e+05  2.086758e+05   None        None
26  2007     12   28         5    股本变化      NaN       NaN          NaN    NaN  None    1.550188e+05   1.703272e+05   2.086758e+05  2.293407e+05   None        None
27  2007     12   31         5    股本变化      NaN       NaN          NaN    NaN  None    1.703272e+05   1.703256e+05   2.293407e+05  2.293407e+05   None        None
28  2008      1   21         5    股本变化      NaN       NaN          NaN    NaN  None    1.703256e+05   1.756821e+05   2.293407e+05  2.293407e+05   None        None
29  2008      6   26         5    股本变化      NaN       NaN          NaN    NaN  None    1.756821e+05   2.046520e+05   2.293407e+05  2.293407e+05   None        None
30  2008      6   27         5    股本变化      NaN       NaN          NaN    NaN  None    2.046520e+05   2.142004e+05   2.293407e+05  2.388795e+05   None        None
31  2008     10   31         1    除权除息    0.335      0.00          3.0    0.0  None             NaN            NaN            NaN           NaN   None        None
32  2008     10   31         5    股本变化      NaN       NaN          NaN    NaN  None    2.142004e+05   2.784606e+05   2.388795e+05  3.105434e+05   None        None
33  2009      6   22         3  非流通股上市      NaN       NaN          NaN    NaN  None    2.784606e+05   2.923675e+05   3.105434e+05  3.105434e+05   None        None
34  2009      6   30         5    股本变化      NaN       NaN          NaN    NaN  None    2.923675e+05   2.923757e+05   3.105434e+05  3.105434e+05   None        None
35  2009     10   15         3  非流通股上市      NaN       NaN          NaN    NaN  None    2.923757e+05   2.924114e+05   3.105434e+05  3.105434e+05   None        None
36  2010      6   28         3  非流通股上市      NaN       NaN          NaN    NaN  None    2.924114e+05   3.105370e+05   3.105434e+05  3.105434e+05   None        None
37  2010      6   29         5    股本变化      NaN       NaN          NaN    NaN  None    3.105370e+05   3.105370e+05   3.105434e+05  3.485014e+05   None        None
38  2010      6   30         5    股本变化      NaN       NaN          NaN    NaN  None    3.105370e+05   3.105368e+05   3.485014e+05  3.485014e+05   None        None
39  2010     12   31         5    股本变化      NaN       NaN          NaN    NaN  None    3.105368e+05   3.105358e+05   3.485014e+05  3.485014e+05   None        None
40  2011      6   30         5    股本变化      NaN       NaN          NaN    NaN  None    3.105358e+05   3.105359e+05   3.485014e+05  3.485014e+05   None        None
41  2011      8    5         5    股本变化      NaN       NaN          NaN    NaN  None    3.105359e+05   3.105359e+05   3.485014e+05  5.123350e+05   None        None
42  2012     10   19         1    除权除息    1.000      0.00          0.0    0.0  None             NaN            NaN            NaN           NaN   None        None
43  2013      6   20         1    除权除息    1.700      0.00          6.0    0.0  None             NaN            NaN            NaN           NaN   None        None
44  2013      6   20         2   送配股上市      NaN       NaN          NaN    NaN  None    3.105359e+05   4.968574e+05   5.123350e+05  8.197361e+05   None        None
45  2013     11   12         5    股本变化      NaN       NaN          NaN    NaN  None    4.968574e+05   5.575902e+05   8.197361e+05  8.197361e+05   None        None
46  2014      1    9         5    股本变化      NaN       NaN          NaN    NaN  None    5.575902e+05   5.575902e+05   8.197361e+05  9.520746e+05   None        None
47  2014      6   12         1    除权除息    1.600      0.00          2.0    0.0  None             NaN            NaN            NaN           NaN   None        None
48  2014      6   12         9   转配股上市      NaN       NaN          NaN    NaN  None    5.575902e+05   6.691059e+05   9.520746e+05  1.142490e+06   None        None
49  2014      9    1         5    股本变化      NaN       NaN          NaN    NaN  None    6.691059e+05   9.836712e+05   1.142490e+06  1.142490e+06   None        None
50  2015      4   13         1    除权除息    1.740      0.00          2.0    0.0  None             NaN            NaN            NaN           NaN   None        None
51  2015      4   13         9   转配股上市      NaN       NaN          NaN    NaN  None    9.836712e+05   1.180406e+06   1.142490e+06  1.370987e+06   None        None
52  2015      5   21         5    股本变化      NaN       NaN          NaN    NaN  None    1.180406e+06   1.180406e+06   1.370987e+06  1.430868e+06   None        None
53  2016      5   23         5    股本变化      NaN       NaN          NaN    NaN  None    1.180406e+06   1.219265e+06   1.430868e+06  1.430868e+06   None        None
54  2016      6   16         1    除权除息    1.530      0.00          2.0    0.0  None             NaN            NaN            NaN           NaN   None        None
55  2016      6   16         9   转配股上市      NaN       NaN          NaN    NaN  None    1.219265e+06   1.463118e+06   1.430868e+06  1.717041e+06   None        None
56  2017      1    9         5    股本变化      NaN       NaN          NaN    NaN  None    1.463118e+06   1.691799e+06   1.717041e+06  1.717041e+06   None        None
57  2017      7   21         1    除权除息    1.580      0.00          0.0    0.0  None             NaN            NaN            NaN           NaN   None        None
58  2017     12   31         5    股本变化      NaN       NaN          NaN    NaN  None    1.691799e+06   1.691798e+06   1.717041e+06  1.717041e+06   None        None
59  2018      5   21         5    股本变化      NaN       NaN          NaN    NaN  None    1.691798e+06   1.717025e+06   1.717041e+06  1.717041e+06   None        None
60  2018      7   12         1    除权除息    1.360      0.00          0.0    0.0  None             NaN            NaN            NaN           NaN   None        None
61  2019      6   26         1    除权除息    1.450      0.00          0.0    0.0  None             NaN            NaN            NaN           NaN   None        None
62  2019      6   30         5    股本变化      NaN       NaN          NaN    NaN  None    1.717025e+06   1.717025e+06   1.717041e+06  1.717041e+06   None        None
63  2019      9   18         5    股本变化      NaN       NaN          NaN    NaN  None    1.717025e+06   1.940575e+06   1.717041e+06  1.940592e+06   None        None
2019-11-23 00:06:11,293 - Database.MongoDB.Client - DEBUG - test_tdx_client_get_xdxr_info (TestClients.TestClients) spend time: 1372.3251819610596 ms

```