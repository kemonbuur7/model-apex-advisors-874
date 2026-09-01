# -*- coding: utf-8 -*-

# 小龙智脑 (XiaoLong Brain) - 全新原创项目

# 作者 / 版权人: 小龙 (XiaoLong)

# License: MIT。本项目所有代码均为原创，保留署名即可自由使用。



import re



# 中日韩统一表意文字区间

_CJK = re.compile(r"[一-鿿]")





def tokenize(text):

    # 英文/数字按词切分，CJK 按字切分

    if not text:

        return []

    tokens = []

    for piece in re.split(r"\s+", text):

        if not piece:

            continue

        non_cjk = _CJK.sub(" ", piece).strip()

        if non_cjk:

            tokens.extend(re.findall(r"[A-Za-z0-9]+|[^\sA-Za-z0-9]", non_cjk))

        tokens.extend(_CJK.findall(piece))

    return tokens





def count_tokens(text):

    return len(tokenize(text))

