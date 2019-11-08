import enum

class IndustryCode(enum.Enum):
    sw_l1 = 0 # 申万一级行业
    sw_l2 = 1 # 申万二级行业
    sw_l3 = 2 # 申万三级行业
    jq_l1 = 3 # 聚宽一级行业
    jq_l2 = 4 # 聚宽二级行业
    zjw = 5  # 证监会行业