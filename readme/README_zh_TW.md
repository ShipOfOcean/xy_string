# xy_string

- zh_CN [简体中文](README_zh_CN.md)
- zh_TW [繁体中文](README_zh_TW.md)
- en [English](README_en.md)

# 说明
字串工具.

<a href="https://github.com/ShipOfOcean/xy_string.git" target="_blank">Github位址</a>

## 安装

```bash
pip install xy_string
```

## 开始

```python
from xy_string.utils import is_empty_string, empty_string, contains_zh

is_empty_string("")
# true

is_empty_string("empty")
# false

empty_string("empty")
# empty

empty_string(None, default="empty")
# empty

empty_string(None)
# None

contains_zh("中文")
# True

contains_zh("Chinese")
# False

```

## 捐贈

如果小夥伴們覺得這些工具還不錯的話，能否請咱喝一杯咖啡呢
<br />
![微信](WeChat.png)
![支付寶](Alipay.png)

## 聯繫方式

```
微信: yuyangitt
郵箱: 845262968@qq.com
```