from pytdx.hq import TdxHq_API

api = TdxHq_API()

with api.connect('119.147.212.81', 7709):
    df = api.to_df(api.get_security_quotes([(0, '000001'), (1, '600300')]))
    print(df.to_json())

    data = api.get_minute_time_data(1, '600300')
    print(data)

    list_df = api.to_df(api.get_security_list(0, 300))
    print(list_df.to_json())