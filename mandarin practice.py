import random

book_words = [
[["ni", "you", "你"], ["hao", "good", "好"], ["ni hao", "hello", "你好"], ["nin", "you (respectfully)", "您"],
               ["nin hao", "hello", "您好"], ["zao", "early", "早"], ["ni zao", "good morning", "你早"],
               ["nin zao", "good morning", "您早"], ["zai", "again", "再"], ["jian", "see", "见"],
               ["zai jian", "good bye", "再见"]],
              
[["ma", "particle", "吗"], ["ni hao ma", "how are you", "你好吗"], ["bu", "no; not", "不"],
               ["cuo", "mistake; bad", "错"], ["bu cuo", "not bad", "不错"], ["hai", "also; fairly", "还"],
               ["ke", "can; may", "可"], ["yi", "use; take", "以"], ["ke yi", "can; pretty good", "可以"],
               ["hai ke yi", "ok; pretty good", "还可以"], ["wo", "I; me", "我"], ["hen", "very; quite", "很"],
               ["hen hao", "very good; very well", "很好"], ["xie", "thank", "谢"], ["xie xie", "thanks", "谢谢"],
               ["ne", "particle", "呢"], ["ni ne", "how about you", "你呢"], ["ye", "also;as well", "也"]],
              
[["shi", "is", "是"], ["de", "of; 's", "的"], ["wo de", "my; mine", "我的"], ["peng", "friend", "朋"],
               ["you", "friend", "友"], ["yi", "one", "一"], ["er", "two", "二"], ["san", "three", "三"],
               ["si", "four", "四"], ["wu", "five", "五"], ["liu", "six", "六"], ["qi", "seven", "七"],
               ["ba", "eight", "八"], ["jiu", "nine", "九"], ["shi", "", "十"]],
              、
[["jin", "today; now", "今"], ["tian", "sky; day", "天"], ["jin tian", "today", "今天"],
               ["ji", "how many", "几"], ["yue", "moon; month", "月"], ["ji yue", "which month", "几月"],
               ["hao", "number; date", "号"], ["ji hao", "what date", "几号"], ["xing", "star", "星"],
               ["qi", "period of time", "期"], ["xing qi", "week", "星期"], ["xing qi ji", "what day of the week", "星期几"],
               ["zuo", "yesterday", "昨"], ["zuo tian", "yesterday", "昨天"], ["ri", "sun", "日"],
               ["ming", "bright; clear", "明"], ["ming tian", "tomorrow", "明天"]],
              
[["jiao", "call", "叫"], ["shen me", "what", "什么"], ["ming", "name", "名"], ["zi", "character; word", "字"],
               ["ming zi", "name", "名字"], ["ta", "she; her", "她"], ["xing", "surname", "姓"],
               ["ma", "horse; surname", "马"], ["ta", "he; him", "他"], ["li", "surname", "李"], ["wang", "surname", "王"],
               ["shan", "surname", "山"]],
              
[["zhu", "live; reside", "住"], ["zai", "in; on", "在"], ["na", "which; what", "哪"],
               ["er", "child; son", "儿"], ["nar", "where", "哪儿"], ["zhong", "middle; center", "中"],
               ["guo", "country; kingdom", "国"], ["ren", "person; people", "人"], ["zhong guo ren", "Chinese", "中国人"],
               ["bei", "north", "北"], ["jing", "capital", "京"], ["bei jing", "Beijing", "北京"],
               ["shang", "up; previous; attend", "上"], ["hai", "sea", "海"], ["shang hai", "Shanghai", "上海"],
               ["xi", "west", "西"], ["an", "safe", "安"], ["xi an", "Xi'an", "西安"], ["ben", "root; origin", "本"],
               ["ri ben", "Japan", "日本"], ["ri ben ren", "Japanese", "日本人"], ["xiang", "fragrant", "香"],
               ["gang", "harbour", "港"], ["xiang gang", "Hong Kong", "香港"], ["na guo ren", "what nationality", "哪国人"]],
              
[["zhe", "this", "这"], ["jia", "family; home", "家"], ["yi jia ren", "one family", "一家人"],
               ["men", "plural suffix", "们"], ["ta men", "they; them", "他们"], ["wo men", "we; us", "我们"],
               ["ma ma", "mother", "妈妈"], ["mei mei", "younger sister", "妹妹"], ["di di", "younger brother", "弟弟"],
               ["ba ba", "father", "爸爸"], ["shui", "who", "谁"], ["jie jie", "older sister", "姐姐"],
               ["ge ge", "older brother", "哥哥"]],
              
[["you", "have; there is", "有"], ["kou", "mouth", "口"], ["da", "big", "大"], ["xiao", "small", "小"],
               ["na", "that", "那"], ["ge", "measure word", "个"], ["liang", "two of", "两"], ["he", "and", "和"],
               ["ying", "hero", "英"], ["ying guo", "Britain", "英国"], ["ying guo ren", "British", "英国人"],
               ["ji kou ren", "how many family members", "几口人"], ["xiong", "elder brother", "兄"],
               ["xiong di jie mei", "brothers and sisters", "兄弟姐妹"], ["mei", "no", "没"],
               ["mei you", "not have; there is not", "没有"]],
              
[["gong", "work", "工"], ["zuo", "do; work", "作"], ["gong zuo", "work", "工作"], ["sui", "age", ""],
               ["sheng", "grow; bear", ""], ["xue sheng", "student", ""],
               ["zhong xue sheng", "secondary school student", "中学生"], ["xiao xue sheng", "primary school student", "小学生"],
               ["le", "particle", ""], ["ji sui", "how old (under ten)", ""], ["duo da", "how old (over ten)", ""]],
              
[["nian", "year", "年"], ["jin nian", "this year", "今年"], ["ji", "grade", "级"],
               ["nian ji", "grade; year", "年级"], ["da ge", "eldest brother", "大哥"],
               ["da xue sheng", "university student", "大学生"], ["dou", "all; both", "都"]],
              
[["ya", "second; asia", "亚"], ["zhou", "continect", "洲"], ["ya zhou", "Asia", "亚洲"], ["jia", "add", "加"],
               ["na", "take", "拿"], ["jia na da", "Canada", "加拿大"], ["mei", "beautiful", "美"],
               ["mei guo", "America", "美国"], ["ba", "hope; earnestly", "巴"], ["ba xi", "Brazil", "巴西"],
               ["nan", "south", "南"], ["nan mei zhou", "South America", "南美洲"],
               ["bei mei zhou", "North America", "北美洲"], ["fa", "law; method", "法"], ["fa gou", "France", "法国"],
               ["de", "morals; virtue", "德"], ["de guo", "Germany", "德国"], ["fei", "wrong; no; not", "非"],
               ["fei zhou", "Africa", "非洲"], ["ou", "Europe", "欧"], ["ou zhou", "Europe", "欧洲"],
               ["nan fei", "South Africa", "南非"], ["lai", "come", "来"], ["ma lai xi ya", "Malaysia", "马来西亚"],
               ["yang", "ocean", "洋"], ["da yang zhou", "Australia; Oceania", "大洋洲"], ["ao", "inlet of sea; bay", ""],
               ["li", "sharp; advantage; benifit", "利"], ["ao da li ya", "Australia", "澳大利亚"], ["qu", "go", "去"],
               ["guo", "pass; cross over; particle", "过"], ["hen duo", "many", "很多"], ["guo jia", "county", "国家"],
               ["ke shi", "but", "可是"]],
              
[["nu", "female", "女"], ["li", "power; strength", "力"], ["nan", "male", "男"], ["men", "door", "门"],
               ["wen", "ask", "问"], ["jian", "tip; pointed; sharp", "尖"], ["bi", "pen", "笔"],
               ["di", "earth; fields; ground", "地"], ["deng", "rank; wait", "等"], ["dan", "but", "但"],
               ["chu", "out; exit", "出"], ["xian", "present; now", "现"], ["chu sheng ri qi", "date of birth", "出生日期"],
               ["chu sheng di", "place of birth", "出生地"]],
              
[["shou", "speak; talk; say", "说"], ["han", "the Han nationality", "汉"], ["yu", "language", "语"],
               ["han you", "Chinese", "汉语"], ["ying yu", "English", "英语"], ["ri yu", "Japanese", "日语"],
               ["fa yu", "French", "法语"], ["de yu", "German", "德语"], ["guang", "broad", "广"], ["dong", "east", "东"],
               ["guang dong", "Guangdong, province in China", "广东"], ["hua", "word; talk", "话"],
               ["guang dong hua", "Cantonese", "广东话"], ["pu", "general; universal", "普"],
               ["tong", "open; through", "通"], ["pu tong hua", "Putonghua, Mandarin", "普通话"]],
              
[["hui", "can; meeting; party", "会"], ["ji", "a few; several", "几"], ["zhong", "type; race; seed", "种"],
               ["hao ji zhong", "several kinds of", "好几种"], ["yu yan", "languange", "语言"], ["ye", "grandfather", "爷"],
               ["ye ye", "grandfather", "爷爷"], ["nai", "grandmother", "奶"], ["nai nai", "grandmother", "奶奶"],
               ["shi", "lifetime; world", "世"], ["jie", "boundry; scope", "界"], ["shi jie", "world", "世界"],
               ["shi jie shang", "in the world", "世界上"], ["xiang", "think; want to; would like to", "想"]],
              
[["yi", "medicine", "医"], ["yi sheng", "doctor", "医生"], ["shi", "teacher; master", "师"],
               ["lao shi", "teacher", "老师"], ["dong jing", "Tokyo", "东京"], ["ting", "front; courtyard", "庭"],
               ["jia ting", "family", "家庭"], ["zhu", "major", "主"], ["fu", "woman", "妇"],
               ["jia ting zhu fu", "housewife", ""], ["shang", "trade; business", ""],
               ["shang ren", "businessman", ""], ["lu", "law; rule", ""], ["yin", "silver", ""],
               ["hang", "profession; business firm", ""], ["yin hang", "bank", ""], ["yin hang jia", "banker", ""],
               ["fu", "husband; man", ""], ["dai fu", "doctor", ""], ["hu", "protect", ""], ["shi", "scholar", ""],
               ["hu shi", "nurse", ""], ["si", "take charge of", ""], ["ji", "machine; engine", ""],
               ["si ji", "driver", ""]]]


run = 1
while run == 1:
    command = int(input("choose a chapter to revise (1-" + str(len(book_words)) + ")  "))
    for item in range(10):
        print(book_words[command-1])
        val1 = random.randint(0, len(book_words[command])-1)
        print("pinyin: " + book_words[command][val1][0])
        print("definition: " + book_words[command][val1][1])
        print("word: " + book_words[command][val1][2])
        print()
