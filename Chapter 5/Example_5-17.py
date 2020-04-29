from clip import clip
from inspect import signature
sig = signature(clip)
sig  # doctest: +ELLIPSIS

str(sig)

for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)
