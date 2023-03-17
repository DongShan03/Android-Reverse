import requests
from lxml import etree 

lua_source = """
function main(splash, args)
  assert(splash:go("https://news.163.com/"))
  assert(splash:wait(0.5))
  
  get_btn_display = splash:jsfunc([[
    function(){
      return document.getElementsByClassName("load_more_btn")[0].style.display
    }
    ]])
  while(true)
  do
    splash:runjs("document.getElementsByClassName('load_more_btn')[0].scrollIntoView[true]")
    splash:select(".load_more_btn").click()
    splash:wait(1)
    display = get_btn_display()
    if (display == "none")
      then
      	break
      end
  end
  return splash:html()
end
"""

resp = requests.get(url="http://192.168.1.5:8050/execute", params={
    "lua_source": lua_source,
})

tree = etree.HTML(resp.text)

divs = tree.xpath("//div[@class='ndi_main']/div")
print(divs)
for div in divs:
    a = div.xpath("./div/div/h3/a")
    if not a:
        continue
    a = a[0]
    href = a.xpath("./@href")[0]
    text = a.xpath("./text()")[0]
    print(text)
