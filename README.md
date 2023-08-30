# Peggle-Nights-CHN
[宝开游戏](https://zh.wikipedia.org/wiki/%E5%AF%B6%E9%96%8B%E9%81%8A%E6%88%B2)《[幻幻球之夜](https://en.wikipedia.org/wiki/Peggle_Nights)》（下称“幻夜”）的简体中文汉化素材，包含贴图以及3个宝开官方发布的额外关卡包。欢迎各位参与改进。

## 私人使用区里的字符
很多全角标点的右半边是空白的，这会导致一行以这些全角标点符号结尾的文本在居中后看起来偏左；同理有些左半边空白的全角标点会导致一行以这些标点开头的文本在居中后看起来偏右。为解决这个问题，我们在Unicode的[私人使用区](https://zh.wikipedia.org/wiki/%E7%A7%81%E4%BA%BA%E4%BD%BF%E7%94%A8%E5%8C%BA)分配了几个码点。当一行需要居中的文本以全角标点符号结尾，我们会改用这些魔改码点。

|标点|字符|原码点|魔改码点|
|-|-|-|-|
|左双引号|“|U+201C|U+E01C|
|右双引号|”|U+201D|U+E01D|
|顿号|、|U+3001|U+E001|
|句号|。|U+3002|~~U+FF61~~ U+E002|
|感叹号|！|U+FF01|U+EF01|
|左圆括号|（|U+FF08|U+EF08|
|右圆括号|）|U+FF09|U+EF09|
|逗号|，|U+FF0C|U+EF0C|
|冒号|：|U+FF1A|U+EF1A|
|分号|；|U+FF1B|U+EF1B|
|问号|？|U+FF1F|U+EF1F|

这些魔改码点与原码点采用完全相同的字形，唯一区别是字形的左半边或右半边空白被极大缩减。

## 译名对比
本仓库的汉化语料参考了网元网为官方制作的《幻幻球》简体中文版（下称“幻一”），采取的译名有相同之处和不同之处。

### 导师和技能
|导师英文名|幻一译名|本仓库译名|技能英文名|幻一译名|本仓库译名|
|-|-|-|-|-|-|
|Bjorn|伯恩|**比约恩**|Super Guide|超级指引|超级指引|
|Lightning Jimmy|闪电吉米|闪电吉米|Multiball|五彩珠|**分身球**|
|Renfield|兰菲尔德|**任菲尔德**|Spooky Ball|幽灵球|幽灵球|
|Kat Tut|法老卡盟|**图坦卡猫**|Pyramid|金字塔|金字塔|
|Splork|斯普洛克|斯普洛克|Space Blast|空间爆炸|空间爆炸|
|Claude|克劳德|克劳德|Flippers|弹力臂|**弹力钳**|
|Tula|图拉|图拉|Flower Power|花开之魅|花开之魅|
|Lord Cinderbottom|地火领主|地火领主|Fireball|火球|**火球术**|
|Warren|沃伦|沃伦|Lucky Spin|幸运转盘|幸运转盘|
|Master Hu|胡神仙|**胡师傅**|Zen Shot|神来之笔|**禅宗球**|
|Marina||玛琳娜|Electrobolt||高压电弧|

### 特技
|特技英文名|幻一译名|本仓库译名|
|-|-|-|
|Long Shot|长击|**远射**|
|Super Long Shot|超级长击|**超长远射**|
|Double Long Shot||双重远射|
|Off the Wall||飞檐走壁|
|Free Ball Skills|巧取赠球|巧取赠球|
|Mad Skillz|神乎其技|神乎其技|
|Crazy Mad Skillz|惊世绝技|惊世绝技|
|Lucky Bounce|幸运反弹|**幸运弹跳**|
|Orange Attack|橙色风暴|**橙色冲击**|
|Extreme Slide|极限滑行|极限滑行|
|Kick the Bucket|木桶弹射|**临桶一脚**|
|Cool Clear|风卷残云|风卷残云|
|Bucket Bonus|接球奖励|**入桶奖励**|
|Mega Shot Bonus|单次高分奖励|**高分奖励**|
|Double Guide|双倍指引|双倍指引|
|Triple Play|三球出击|三球出击|
|Spooktacular|神出鬼没|神出鬼没|
|Pyramid Pileup|连环金字塔|连环金字塔|
|Big Bang|宇宙大爆炸|宇宙大爆炸|
|Flip Out|超长弹力|**弹力四射**|
|Petal to the Metal|天女散花|天女散花|
|Great Balls of Fire|熊熊火球|熊熊火球|
|Spin Again|旋转再现|**再转一次**|
|Zen Maniac|神乎其神|**禅心爆发**|
|Power Surge||电潮汹涌|
|Multiball Madness|疯狂五彩珠|**分身球狂欢**|
|Free Ball Frenzy|赠球大酬宾|赠球大酬宾|
|Pyramid Pickup|塔上乾坤|塔上乾坤|
|Eye of Pyramid||金字塔之眼|
|Flipper Maniac|弹无止境|弹无止境|
|Hot Stuff|请球入瓮|请球入瓮|
|Hat Trick|帽子戏法|帽子戏法|
|Shock It to Me||强力通电|
