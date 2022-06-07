
from lxml import etree
# etree.XML().xpath() #etree里才有xpath

# xml示例:
xml='''
    <store>
        <id>1</id>
        <name>大白便利店</name>
        <price>16.40</price>
        <nick>狗剩</nick>
    <vegetables>
        <food id="001">大白菜</food>
        <food id="002">菠菜</food>
        <food class="cucumber">黄瓜</food>
        <food class="potato">土豆</food>
        <food class="tomato">红薯</food>
        <div>
            <food>甜瓜(可当水果)</food>
            <div>
                <food>甜瓜(可当蔬菜)</food>
            </div>
        </div>
        <span>
            <food>西红柿</food>
        </span>
    </vegetables>
        <meet>
            <food id="beef">牛肉</food>
            <food id="pork">猪肉</food>
        </meet>
    </store>
'''
tree=etree.XML(xml)
result=tree.xpath('/store/vegetables/*/food/text()') #text()获取name标签内的文本
print(result)