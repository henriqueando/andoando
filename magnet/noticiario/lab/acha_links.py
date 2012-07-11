# coding: utf-8

import re

amostra = """Muitos animais comem os cogumelos que brotam na coloração marrom-amarelada e são visíves no outono. O fungo francês - ainda que imenso - é bem menor que o "similar":http://www.factmonster.com/spot/fungus1.html encontrado na "floresta nacional de Malheur":http://www.grantcounty.cc/zones/usfs/malheur/index.htm, no estado norte-americano de Oregon, que se estende por 8.940.800 metros quadrados."""

RE_LINK = re.compile(r'"([^"]+)":(https?://[^ ]+[\w/#])')

for res in RE_LINK.findall(amostra):
    print res

else:
    print 'FIM'

print RE_LINK.sub(r'<a href="\2">\1</a>', amostra)

