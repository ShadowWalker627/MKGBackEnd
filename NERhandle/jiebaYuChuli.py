import jieba
import jieba.posseg as pseg

jieba.load_userdict("userdict.txt")

yuliao = open('chapter11.txt')
# print(yuliao.read())

# seg_list = jieba.cut(yuliao.read())

# seg_list = jieba.cut("在圆柱或圆锥母体表面上制出的螺旋线形的、具有特定截面的连续凸起部分。螺纹按其母体形状分为圆柱螺纹和圆锥螺纹；"
#                      "按其在母体所处位置分为外螺纹、内螺纹，按其截面形状（牙型）分为三角形螺纹、矩形螺纹、梯形螺纹、"
#                      "锯齿形螺纹及其他特殊形状螺纹。在圆柱或圆锥表面上，沿着螺旋线所形成的具有规定牙型的连续凸起。"
#                      "凸起是指螺纹两侧面的实体部分。又称牙。在机械加工中，螺纹是在一根圆柱形的轴上（或内孔表面）用刀具或砂轮切成的，"
#                      "此时工件转一转，刀具沿着工件轴向移动一定的距离，刀具在工件上切出的痕迹就是螺纹。在外圆表面形成的螺纹称外螺纹。"
#                      "在内孔表面形成的螺纹称内螺纹。螺纹的基础是圆轴表面的螺旋线。通常若螺纹的断面为三角形，则叫三角螺纹；"
#                      "断面为梯形叫做梯形螺纹；断面为锯齿形叫做锯齿形螺纹；断面为方形叫做方牙螺纹；断面为圆弧形叫做圆弧形螺纹等等螺纹的基本要素:牙型、螺纹的直径、线数、导程和螺距、旋向1）牙型"
#                      "在通过螺纹轴线的剖面上，螺纹的轮廓形状称螺纹牙型。常见的牙型有三角形、梯形、锯齿形等。本图所示的是三角形牙型。"
#                      "2）螺纹的直径大径d（D）：与外螺纹牙顶或内螺纹牙底相重合的假想圆柱体直径，是螺纹的最大直径。小径d1（D1）："
#                      "与外螺纹牙底或内螺纹牙顶相重合的假想圆柱体直径，是螺纹的最小直径。中径：一个假想圆柱的直径，"
#                      "其圆柱母线通过牙型上沟槽和凸起宽度相等的地方。公称直径：代表螺纹规格的直径，一般指螺纹大径尺寸。"
#                      "但管螺纹的公称直径不是指螺纹大径，而是指管子的公称直径。3）线数（n）螺纹有单线和多线之分，"
#                      "沿一条螺旋线形成的螺纹称单线螺纹，沿两条或两条以上在轴向等距分布的螺旋线形成的螺纹，称多线螺纹。4"
#                      "）导程和螺距导程（P）：沿同一条螺旋线形成的螺纹上相邻两牙在中径线上对应两点间的轴向距离。螺距（L）："
#                      "螺纹上相邻两牙在中径线上对应两点间的轴向距离。可见导程=螺距x线数 双线螺纹的导程L＝Px2=2P普通螺纹的螺距查表可得。"
#                      "5）旋向螺纹有右旋和左旋之分。当螺纹旋进时为顺时针方向旋转的，称为右旋螺纹；逆时针方向旋转的，称为左旋螺纹。右"
#                      "旋螺纹由于应用较多，故图纸上不必注明；而左旋螺纹则必须在图纸上注明左旋。上述五项是螺纹的基本要素，"
#                      "改变其中任何一顶，就会使螺纹规格不同。为了便于设计、制造与选用，国家标准对螺纹的牙型、大径、螺距都作了规定"
#                      "，凡这三项符合标准的，称为标准螺纹；牙型符合标准规定，大径或螺距不符合标准的称特殊螺纹；牙型不符合标准的称非标准螺纹"
#                      "。要使内外螺纹旋合，五要素应分别相同。")
seg_list = jieba.cut("在圆柱或圆锥母体表面上制出的螺旋线形的、具有特定截面的连续凸起部分。螺纹按其母体形状分为圆柱螺纹和圆锥螺纹。按其在母体所处位置分为外螺纹、内螺纹，按其截面形状（牙型）分为三角形螺纹、矩形螺纹、梯形螺纹、锯齿形螺纹及其他特殊形状螺纹。在圆柱或圆锥表面上，沿着螺旋线所形成的具有规定牙型的连续凸起。凸起是指螺纹两侧面的实体部分。又称牙。在机械加工中，螺纹是在一根圆柱形的轴上（或内孔表面）用刀具或砂轮切成的，此时工件转一转，刀具沿着工件轴向移动一定的距离，刀具在工件上切出的痕迹就是螺纹。")
se = ''
for i in seg_list:
    # print(i)
    se += i + ' / '
    # se += i + ' '
print(se)

topicTitle = 'yuliaoyuchuli'
fileurl = '/Users/baymax/Dev/owl/{topicTitle}.txt'


nerDit = {
    "PM": ('螺纹', '三角形螺纹', '矩形螺纹', '梯形螺纹', '锯齿形螺纹', '管螺纹', '粗牙普通螺纹', '细牙普通螺纹', '管联接用细牙普通螺纹',
           '非螺纹密封的55°圆柱管螺纹', '用螺纹密封的55°圆柱管螺纹', '60°圆锥管螺纹', '米制锥螺纹', '圆弧螺纹', '普通平键', '导向平键',
           '薄型平键', '滑键联接', '半圆键', '普通楔键', '钩头楔键', '切向键', '圆头普通平键(A型)', '平头普通平键(B型)', '单圆头普通平键(C型)',
           '普通切向键', '强力切向键', '花键', '花键联接', '矩形花键', '渐开线花键', '钢铆钉', '铜铆钉', '铝铆钉', '半圆头铆钉', '沉头铆钉',
           '半圆头钢铆钉', '沉头钢铆钉', '半沉头铆钉', '开口型扁圆头铆钉', '标牌铆钉', '熔化焊', '气焊', '电弧焊', '手工电弧焊', '埋弧焊',
           '氩弧焊', '二氧化碳气体保护焊', '真空电子束焊', '电渣焊', '对焊', '点焊', '缝焊', '钎焊', '碳钢焊条', '低合金钢焊条', '不锈钢焊条',
           '堆焊焊条', '铸铁焊条', 'E4300', 'E4301', 'E5001', 'E4303', 'E5003', 'E4311', 'E5011', 'E4313', 'E4353', 'E5015', 'E4316',
           'E4315', 'E5016', 'E4320', 'E4323', 'E4324', 'E5024', 'E4327', 'E5027', 'E5028', 'E5015-A1', 'E5500-B1', 'E5503-B1',
           'E5515-B1', 'E5515-B2', 'E5500-B2-V', 'E5515-B2-V', 'E5515-B2-VNb', 'E5515-B2-VW', '有机胶粘剂', '天然胶粘剂', '动物胶',
           '植物胶', '合成胶粘剂', '热塑性树脂型胶粘剂', '热固性树脂型胶粘剂', '橡胶型树脂型胶粘剂', '混合型胶粘剂', '无机胶粘剂', '磷酸盐型',
           '磷酸盐型胶粘剂', '硅酸盐型', '硅酸盐型胶粘剂', '硼酸盐型', '硼酸盐型胶粘剂', '结构型胶粘剂', '溶剂型胶粘剂', '反应型胶粘剂',
           '热塑性胶粘剂', '溶液型胶粘剂', '乳液型胶粘剂', '膏糊型胶粘剂', '粉末型胶粘剂', '环氧树脂胶粘剂', '酚醛树脂胶粘剂', '丙烯酸酯胶粘剂',
           '聚氨酯胶粘剂', '杂环高分子胶粘剂', '不饱和聚酯树脂胶粘剂', '螺栓联接', '双头螺柱联接', '螺钉联接', '紧定螺钉联接', '对顶螺母',
           '弹簧垫圈', '自锁螺母', '开口销与六角开槽螺母', '止动垫圈', '串联铁丝', '圆柱管螺纹', '左旋螺纹', '右旋螺纹', '单线螺纹', '粗牙螺纹',
           '细牙螺纹', '普通螺纹', '公制螺纹', '英制螺纹', '圆锥管螺纹', '英制细牙螺纹', '传动螺纹', '标准螺纹', '内螺纹', '外螺纹',
           '螺栓', '橡胶垫', '螺母', '垫圈', '垫片', '弹簧', '螺杆', ' 双头螺柱', ' 对顶螺母', '联接螺纹', '传动螺纹', '英制螺纹', '公制螺纹',
           '粗牙螺纹', '细牙螺纹', '圆柱管螺纹', '圆锥管螺纹', '英制细牙螺纹', '螺旋副', '单线螺纹', '多线螺纹', ' 旋转螺母', ' 矩形螺旋副',
           '螺纹升角', '松联接', '紧联接', '弹簧垫圈', '六角开槽螺母', '自锁螺母', '止动垫圈', '串联铁丝', '螺钉组', ' 串联钢丝', '螺栓组联接',
           '单个螺栓联接', '钢制螺栓', '石棉垫片', '胶垫片', '金属垫片', '皮革垫片', '铜皮', '铰制孔螺栓联接', '普通螺栓联接', '螺栓组联接',
           '环槽螺母', ' 传力螺旋', '传导螺旋', '调整螺旋', '铸铁螺母', '青铜螺母', '型面联接', '键联接', '平键联接', '半圆键联接', '楔键联接',
           '切向键联接', '普通平键', '导向平键', '薄型平键', '滑键', '静联接', '动联接', '轴端联接', '空心轴', '起键螺孔', '半圆键',
           '钩头楔键', '普通楔键', '矩形花键', '花键联接', '渐开线花键', '圆柱销', '圆锥销', '槽销', '开口销', '搭接缝', '不可拆联接', '铆钉联接',
           '铆接', '铆钉', '强固铆缝', '强密铆缝', '紧密铆缝', '正交接头', '搭接接头', '对接接头', '角焊缝', '搭接焊缝', '无机黏结剂', '有机黏结剂',
           '黏结剂', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    ),
    "MA": ('金属', '塑料', '橡胶', '玻璃', '铸铁', '碳素钢', '合金钢', '钢', '青铜', '铜', '紫铜', '白铜', '黄铜', '电解铜', '无氧铜',
           '镍黄铜', '锰黄铜', '低锌黄铜', '铝青铜', '硅青铜', '高强度镀青铜', '灰口铸铁', '球墨铸铁', '钛','钛及其合金', '工业纯钛',
           '铝', '铝及其合金', '硬合金铝', '工业纯铝', '二十一号防锈铝', '防锈铝', '不锈钢', '中碳钢', '低碳钢', '低合金钢', '优质碳素钢',
           '磷酸盐', '硅酸盐', '无机氧化铜-磷酸胶', '高分子材料', '树脂', '酚醛树脂', '环氧树脂', '有机胶', '酚醛-缩醛-有机硅胶', '环氧-酚醛胶',
           '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''
    ),
    "STR": ('挤压强度', '剪切强度', '轴向载荷', ' 静载荷', '动载荷', ' ', ''),
    "TO": ('测力矩扳手', '定力矩扳手', '', '', '', '', ''),
    "PRC": ('刀具', '工件', '砂轮', '回火', '正火', '退火', '淬火', '冷作硬化', '端铣刀', '盘铣刀', '插刀', '拉刀', '', '', '', '', '', '', '', '', '', '', '', '', '',),
    "PARAM": ('公称直径', '最大直径', '最小直径', '导程', ' 牙型角', ' 大径', '小径', '螺距', '线数', '接触高度', '螺纹轴线', '传动效率',
              '径向高度', '牙侧角', '摩擦因数', '法向反力', '水平推力', '摩擦力', '摩擦角', '阻力', '驱动力', '总反力', '切向力', '力矩',
              '法向力', ' 联接精度', '屈服极限', '结构型式', '最大许用值', '摩擦力矩', '拧紧力矩', '工作载荷', ' 拉应力', '扭转应力',
              '螺栓危险截面', ' 计算应力', '第四强度理论', '强度条件', '受力形式', '弹性变形', '总拉力', ' 轴向工作载荷', '工作拉力', '预紧力',
              '残余预紧力', '总拉伸载荷', '工作载荷', '伸长量', '总的伸长量', ' 压缩量', '总压缩量', '总伸长量', '总的压缩量', '相对刚度',
              '拉伸强度条件', '可靠系数', '摩擦因数', '横向工作载荷', '横向载荷', ' 拉伸刚度', '剪切刚度', '横向总载荷', '挤压力', '横向工作剪切力',
              '最大摩擦力', '防滑系数', '翻转力矩', '弯曲应力', '疲劳强度', '应力集中', '残余应力', '失效形式', ' 螺纹中径', '螺纹圈数',
              '许用压强', '引用系数', '螺纹高度', '工作高度', '阻力矩', '临界载荷', '螺杆长细比', '长度系数', '螺杆危险截面', '惯性半径',
              '惯性矩', '弹性模量', '双向转矩', '单方向轴向力', '抗拉强度', '工作长度', '许用挤压应力', '许用压强', '齿侧面', '齿形',
              '铆钉直径', '钉孔直径', '板宽', '铆钉数目', '许用拉应力', '许用切应力', '静载许用应力', '载荷应力', '压应力', '焊缝的长度',
              '降低因数', '许用应力', '许用压应力', '最低抗拉强度', '胶接强度', '耐热性', '耐介质性', '耐老化性', '温度', '压力', '保持时间',
              '涂布性', '流动性', '有效储存期', '防锈', '到点', '黏结强度', '力学性能', '胶层厚度', '固化情况', '工艺水平', '环境温度', '载荷性质',
              '工作时间', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
    )
}

count = 0
res = ''
words = pseg.cut(se)

nerPM = []
nerMA = []
nerSTR = []
nerTO = []
nerPRC = []

try:
    f = open(fileurl.format(topicTitle=topicTitle), 'w')
    for word, flag in words:
        # 删除字符串x, 副词 d, 助词 u,方位词 f, 代词 r
        # if(flag == 'x' or flag == 'd' or flag == 'uj' or flag == 'ud' or flag == 's' or flag == 'a' or flag == 'f'
        #      or flag == 'r' or flag=='m' or flag == 'p' or flag == 'c'):
        #     count += 1
        # else:
        # print('%s %s' % (word, flag))
        if (flag == 'n'):
            print('%s %s' % (word, flag))
            # res += word + ' / '
            res += word + ' '
            f.write('%s %s \n' % (word, flag))
            if(word in nerDit['PM'] and (not word + '-PM' in nerPM)):
                nerPM.append(word + '-PM')
                # print(word + '-PM')
            elif(word in nerDit['MA'] and (not word + '-MA' in nerMA)):
                nerMA.append(word + '-MA')
            elif (word in nerDit['STR'] and (not word + '-STR' in nerSTR)):
                nerSTR.append(word + '-STR')
            elif (word in nerDit['TO'] and (not word + '-TO' in nerTO)):
                nerTO.append(word + '-TO')
            elif (word in nerDit['PRC'] and (not word + '-PRC' in nerPRC)):
                nerPRC.append(word + '-PRC')
    print(res)
    print(nerPM)
    print(nerMA)
    print(nerSTR)
    print(nerTO)
    print(nerPRC)
    f.close()
except IOError as e:
    print(e)
