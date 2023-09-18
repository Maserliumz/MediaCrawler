# Desc: base config
PLATFORM = "xhs"
KEYWORDS = "消费贷,贷款,借款,借贷,分期,利率,借款,信用评分,贷款额度,贷款周期,利息,还款方式,无抵押,信贷,个人贷款,线上申请,额度审批,月供,年利率,逾期,信用卡贷款,贷款顾问,快速审批,资质审核,借贷平台,信用记录,借贷合同,首付,咨询服务,贷款计算器,违约金,征信,资金用途,金融机构,还款期限,贷款利息,抵押贷款,借贷风险,预审批,信用报告,申请条件,线下服务,贷款服务,贷款顾问,银行贷款,担保,信用卡分期,借贷利率,网贷,贷款申请流程,实时审批,灵活还款,贷款政策,提前还款"
LOGIN_TYPE = "qrcode"  # qrcode or phone or cookie
COOKIES = ""  # login by cookie, if login_type is cookie, you must set this value

# enable ip proxy
ENABLE_IP_PROXY = False

# retry_interval
RETRY_INTERVAL = 60 * 30  # 30 minutes

# playwright headless
HEADLESS = True

# save login state
SAVE_LOGIN_STATE = True

# save user data dir
USER_DATA_DIR = "%s_user_data_dir"  # %s will be replaced by platform name

# crawler max notes count
CRAWLER_MAX_NOTES_COUNT = 20

# max concurrency num
MAX_CONCURRENCY_NUM = 10
