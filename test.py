import backports.textwrap.textwrap as wrp
from cwcwidth import wcswidth as wcw

print(wcw('a'))
y = "12⁦⁩⁦⁩⁩⁩⁩345678900"
print(wcw(y))
wrpr = wrp.TextWrapper(width=6, text_len=wcw)
print(wrpr.wrap(y))

def text_len(text):
    return sum(
        0 if c == 'Q' else 1
        for c in text
    )


wrappd = wrp.TextWrapper(width=6, text_len=text_len)
print(wrappd.wrap("012345678"))
print(wrappd.wrap("01QQQQ2Q345678"))
print(wrappd.wrap("QQQQQ01234"))