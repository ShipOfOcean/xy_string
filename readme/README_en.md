# xy_string

- zh_CN [简体中文](README_zh_CN.md)
- zh_TW [繁体中文](README_zh_TW.md)
- en [English](README_en.md)

# Description
String tool.

## Install

```bash
pip install xy_string
```

## Start

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

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?
![WeChat](WeChat.png)
![Alipay](Alipay.png)


## Contact

```
Wechat: yuyangitt
Mail: 845262968@qq.com
```