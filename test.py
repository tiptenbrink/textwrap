import backports.textwrap.textwrap as wrp
from cwcwidth import wcswidth as wcw

print(wcw('a'))
y = "12⁦⁩⁦⁩⁩⁩⁩345678900"
print(wcw(y))
wrpr = wrp.TextWrapper(width=10, text_len=wcw)
print(wrpr.wrap(y))