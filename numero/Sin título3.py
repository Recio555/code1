# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:10:29 2024

@author: usuario
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
#html = urlopen('http://www.pythonscraping.com/pages/page1.html')
#html = urlopen('https://www.temu.com/do/zapatos-casuales-para-hombre-de-talla--con-parte-superior-de-cuero-de-microfibra-zapatos-transpirables-de-suela-suave-con-cordones-elasticos-para-caminar-al-aire-libre-y-conducir-g-601099533003983.html?top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2FFancyalgo%2FVirtualModelMatting%2Fd94dc6613f51971722601b4037434792.jpg&spec_gallery_id=2071035197&share_token=ujV74xjiyQFybGvBZqFciKcq6xFe-4iCSmtzg9X33J70Py33Ixlz0vI_xQGbRP57HMl1eJd58BNbzJV4FdQwty1CmNhOV4X4aGqJyke5TcbyhXDxCUFnXqKliGY66Cri&refer_page_el_sn=209279&_x_vst_scene=adg&_x_ads_sub_channel=feed&_x_ns_prz_type=-1&_x_ns_sku_id=17592336368095&_x_ns_gid=601099544760134&_x_ads_channel=google&_x_ns_lan=es&_x_gmc_account=5352200233&_x_login_type=Google&_x_bg_adid=gd3764933-2&_x_ads_account=8161983713&_x_ads_set=21419898934&_x_ads_id=164401434376&_x_ads_creative_id=703930928869&_x_ns_source=d&_x_ns_gclid=EAIaIQobChMIlIqQ8PryhwMVxY1aBR2e4SpFEAEYASACEgL6NfD_BwE&_x_ns_placement=www.msn.com&_x_ns_match_type=&_x_ns_ad_position=&_x_ns_product_id=&_x_ns_target=&_x_ns_devicemodel=&_x_ns_wbraid=%7Bwbraid%7D&_x_ns_gbraid=%7Bgbraid%7D&_x_ns_targetid=&refer_page_name=kuiper&refer_page_id=13554_1723586553736_2l24h181xt&refer_page_sn=13554&_x_sessn_id=xlxi40p25s')
html = urlopen('https://books.google.com.do/books?id=frVy_zqBG3cC&pg=PA7&lpg=PA7&dq=libro+de+calculo&source=bl&ots=DTO3uIqv7Z&sig=ACfU3U3XVFqdRZE2-C4b3--pekQVO9Je3w&hl=es&sa=X&ved=2ahUKEwjotv7k_fKHAxWtVTABHd00Bcs4RhDoAXoECAsQAw#v=onepage&q=libro%20de%20calculo&f=false')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)