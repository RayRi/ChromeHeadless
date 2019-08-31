## 说明

该项目的目的是为了测试使用 Headless Driver 的方式使用 Chrome，此外也是为了方便解析一个 [JS 请求页面](http://txzb.miit.gov.cn/DispatchAction.do?efFormEname=POIX14&pagesize=11)——避免人为去解析 JS。最终的结果是只保留了请求到的页面，没有对页面内容进行解析。

## 运行需求

1. 需要安装 Chrome 驱动，[Chromedriver 75](https://chromedriver.storage.googleapis.com/index.html?path=75.0.3770.8/)
2. Python3.6+

运行文件需要进入 `main.py` 文件所在文件夹，直接运行 `python main.py`

## 文件结构

```
├── README.md
├── config # 配置文件夹
├── ├── settings.py	# 常用设置
├── data	# 数据存储文件夹
├── log		# 日志文件夹
├── main.py	# main 文件
└── utils		# 工具文件夹
    └── chromedriver	# Chrome 驱动
```

