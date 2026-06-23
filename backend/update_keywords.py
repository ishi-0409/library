# 入手した本のタイトルと単語をDBに反映させる機能S

import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    dbname=os.getenv("POSTGRES_DB")
)
cur = conn.cursor()

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['孤独', '自己否定', '人間不信', '疎外感'], '人間失格'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['純粋経験', '自己', '実在', '善悪'], '善の研究'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['罪悪感', '贖罪', '正義', '孤独'], '罪と罰'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['戦争', '愛国心', '運命', '人生の意味', '歴史'], '戦争と平和'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['不倫', '愛', '社会的抑圧', '自由', '罪悪感'], 'アンナ・カレーニナ'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['死', '孤独', '人生の意味', '恐怖', '虚偽'], 'イワン・イリイチの死/クロイツェル・ソナタ'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['神', '信仰', '罪悪感', '家族', '自由意志'], 'カラマーゾフの兄弟 完全版'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['純粋', '善意', '社会的疎外', '理想主義', '孤独'], '白痴(上)'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['虚無主義', '革命', '狂気', '社会批判', '自己破壊'], '悪霊'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['自意識過剰', '孤独', '疎外感', '自己嫌悪', '人間不信'], '地下室の手記'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['喪失', '変化', '郷愁', '時代の終わり', '無力感'], '[新訳] 桜の園'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['夢', '閉塞感', '孤独', '希望', '諦め'], '三人姉妹'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['夢', '挫折', '愛', '芸術', '自己破壊'], 'かもめ'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['狂気', '社会的抑圧', '孤独', '不条理', '自由'], 'ヴェーロチカ/六号室'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['社会的疎外', '不条理', '小市民', '夢', '幻想'], '外套・鼻'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['欲望', '社会批判', '虚偽', '人間の愚かさ', '風刺'], '死せる魂'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['世代間対立', '虚無主義', '愛', '変革', '孤独'], '父と子'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['初恋', '失恋', '憧れ', '青春', '切なさ'], 'はつ恋'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['悪魔', '自由', '愛', '全体主義', '芸術'], '巨匠とマルガリータ上'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['執着', '狂気', '道徳', '美', '倒錯'], 'ナボコフ・コレクションロリータ魅惑者'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['孤独', '挑戦', '老い', '誇り', '自然'], '老人と海'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['戦争', '愛', '喪失', '逃避', '絶望'], '武器よさらば'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['喪失', '虚無感', '愛', '戦後', '享楽'], '日はまた昇る'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['夢', '富', '愛', '幻滅', 'アメリカンドリーム'], 'グレート・ギャツビー'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['狂気', '愛', '喪失', '退廃', '自己破壊'], '夜はやさし'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['家族', '崩壊', '時間', '喪失', '南部社会'], '響きと怒り'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['人種差別', '孤独', '暴力', '宗教', '疎外感'], '八月の光'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['貧困', '家族', '社会批判', '希望', '連帯'], '怒りの葡萄'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['夢', '友情', '孤独', '社会的弱者', '挫折'], 'ハツカネズミと人間'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['執着', '復讐', '自然', '狂気', '運命'], '白鯨上'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['疫病', '不条理', '連帯', '死', '抵抗'], '新訳『ペスト』'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['不条理', '反抗', '意味', 'ニヒリズム', '生きる意志'], 'シーシュポスの神話'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['自由', '存在', '実存主義', '意識', '不安'], '存在と無 I'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['幻想', '退屈', '不倫', '現実', '理想'], 'ボヴァリー夫人'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['恋愛', '挫折', '青春', '社会', '理想と現実'], '感情教育（上）'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['野心', '階級', '愛', '嫉妬', '社会批判'], '赤と黒下'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['愛', '政治', '自由', '運命', '理想主義'], 'パルムの僧院'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['家族', '犠牲', '野心', '貧困', '愛'], 'ゴリオ爺さん'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['純愛', '憧れ', '社会', '理想', '自己犠牲'], '谷間の百合'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['正義', '贖罪', '社会批判', '愛', '革命'], 'レ・ミゼラブル④'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['美醜', '愛', '運命', '社会的排除', '宿命'], 'ノートルダム・ド・パリ(下)'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['記憶', '時間', '意識', '喪失', '芸術'], '失われた時を求めて 5'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['不条理', '疎外感', '孤独', '死', '感情の欠如'], '異邦人'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['実存主義', '孤独', '自由', '不安', '意識'], '嘔吐(新訳)'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['疎外感', '変容', '孤独', '家族', '不条理'], '変身 ～カフカ短篇傑作集～'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['罪悪感', '官僚主義', '不条理', '恐怖', '無力感'], '審判'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['官僚主義', '疎外感', '不条理', '孤独', '現実の不透明さ'], '城'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['知識欲', '悪魔', '救済', '人間の限界', '欲望'], 'ゲーテ「ファウスト」第2部'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['失恋', '感傷', '情熱', '孤独', '自己破壊'], '若きウェルテルの悩み'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['悟り', '宗教', '自己探求', '東洋哲学', '内なる旅'], 'シッダールタの旅'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['教育制度', '青春', '挫折', '社会的抑圧', '孤独'], '車輪の下で'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['自己発見', '成長', '善悪', '内なる声', '自由'], 'デミアン'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['孤独', '二重性', '現代社会', '芸術', '自己嫌悪'], '荒野のおおかみ'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['死', '時間', '知識', '退廃', '戦争'], '魔の山'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['美', '執着', '老い', '死', '芸術'], 'ベニスに死す'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['孤独', '詩', '感受性', '存在', '都市'], 'マルテの手記'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['強迫観念', '孤立', '精神的苦痛', '知性', '戦争'], 'チェスの話'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['超人', '神の死', '権力意志', 'ニヒリズム', '自己超越'], '黄金の星(ツァラトゥストラ)はこう語った上'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['復讐', '孤独', '死', '存在', '決断'], 'ハムレット'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['野心', '罪悪感', '権力', '狂気', '運命'], 'マクベス'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['階級', '成長', '幻想', '欲望', '自己発見'], '大いなる遺産（上）'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['執着', '復讐', '愛', '運命', '憎しみ'], '嵐が丘'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['自立', '愛', '階級', '尊厳', '女性'], 'Jane Eyre　ジェーン・エア'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['美', '退廃', '道徳', '快楽', '魂の腐敗'], '新訳　ドリアン・グレイの肖像'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['植民地主義', '人間の闇', '文明', '道徳的堕落', '自己'], '闇の奥'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['意識', '時間', '孤独', '社会', '精神'], 'ダロウェイ夫人'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['時間', '喪失', '家族', '芸術', '意識'], '灯台へ'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['運命', '社会的不正義', '女性', '純潔', '悲劇'], 'ダーバビル家のテス'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['植民地主義', '文化衝突', '偏見', '友情', '誤解'], 'インドへの道'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['全体主義', '監視', '自由', '真実', '支配'], '1984年'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['全体主義', '権力', '平等', '革命', '腐敗'], 'アニマル・ファーム ＜動物農場＞'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['管理社会', '自由', '幸福', 'テクノロジー', '人間性'], 'すばらしい新世界'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['孤独', '神話', '家族', '歴史', '魔法的現実主義'], '百年の孤独'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['愛', '忍耐', '老い', '時間', '執着'], 'コレラの時代の愛'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['無限', '時間', '迷宮', '記憶', '夢'], '砂の本'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['迷宮', '時間', '現実と虚構', '不思議', '知識'], '伝奇集'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['死', '記憶', '幽霊', '孤独', '過去'], 'ペドロ・パラモ'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['自由', '反抗', '都市', '実験', '自己探求'], '石蹴り遊び'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['女性', '家族', '政治', '魔法的現実主義', '歴史'], '精霊たちの家下'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['権力', '革命', '記憶', '死', '欲望'], 'アルテミオ・クルスの死'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['裏切り', '罪悪感', '孤独', '友情', '道徳'], 'こころ'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['美', '無常', '孤独', '儚さ', '官能'], '雪国（新潮文庫）'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['美', '執着', '破壊', 'コンプレックス', '狂気'], '金閣寺'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['喪失', '青春', '孤独', '死', '恋愛'], 'ノルウェイの森(上)'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['孤立', '自由', '実存', '逃避', '不条理'], '砂の女（新潮文庫）'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['自己欺瞞', '社会批判', '民族性', '屈辱', '革命'], '阿Q正伝・狂人日記他十二篇'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['暴力', '歴史', '記憶', '抵抗', '死'], '少年が来る'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['女性差別', '社会的抑圧', '結婚', '母性', 'アイデンティティ'], '82年生まれ、キム・ジヨン'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['正義', '無知の知', '死', '対話', '真理'], 'ソクラテスの弁明'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['正義', '理想社会', 'イデア', '知', '統治'], '国家'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['魂', '不死', '死後の世界', '知識', '真理'], 'パイドン'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['幸福', '徳', '倫理', '友情', '善'], 'ニコマコス倫理学'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['社会', '正義', '国家', '権力', '自由'], '政治学(下)'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['自己制御', '義務', '死', '理性', '内省'], '自省録'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['時間', '死', '人生の意味', '怠惰', '充実'], '人生の短さについて'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['快楽', '死の恐怖', '友情', '自然', '幸福'], '自然について他'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['理性', '懐疑', '思考', '確実性', '方法'], '方法序説'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['神', '自由', '感情', '幸福', '必然性'], 'エチカ(倫理学)下(スピノザ)'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['存在', '神', '調和', '宇宙', '精神'], '単子論'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['自由', '権利', '政府', '財産', '革命'], '統治二論'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['経験', '感情', '道徳', '因果', '懐疑'], '人間本性論 1'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['信仰', '理性', '人間の矛盾', '神', '賭け'], 'パンセ'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['自由', '平等', '社会', '一般意志', '契約'], '社会契約論'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['不平等', '社会批判', '自然', '文明', '所有'], '人間不平等起源論'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['理性', '認識', '知識の限界', '時間', '空間'], '純粋理性批判'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['義務', '道徳', '自律', '善意志', '普遍法則'], '道徳形而上学の基礎づけ'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['弁証法', '歴史', '精神', '自由', '矛盾'], '精神現象学上'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['意志', '苦しみ', '悲観主義', '欲望', '諦念'], '意志と表象としての世界'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['革命', '階級闘争', '平等', '資本主義批判', '労働'], '共産党宣言'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['資本主義', '労働', '搾取', '剰余価値', '疎外'], '☆新版☆ 資本論第5分冊'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['道徳批判', '権力意志', '超人', '価値の転換', '自由'], '善悪の彼岸'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['自由', '個人', '社会', '多数決の横暴', '寛容'], '自由論'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['言語', '論理', '沈黙', '世界の限界', '語りえぬもの'], '論理哲学論考'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['存在', '死', '時間', '不安', '本来性'], '存在と時間'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['権力', '監視', '規律', '身体', '制度'], '監獄の誕生'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['正義', '平等', '無知のヴェール', '社会契約', '分配'], '正義論'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['消費', '記号', '疎外', '欲望', '現代社会'], '消費社会の神話と構造'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['絶望', '信仰', '実存', '自己', '不安'], '死に至る病'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['全体主義', '悪', '政治', '権力', '孤独'], '全体主義の起原'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['市場', '自由競争', '分業', '富', '見えざる手'], '国富論 II'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['有効需要', '失業', '景気', '政府介入', '経済'], '要約　ケインズ　雇用と利子とお金の一般理論'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['自由', '計画経済批判', '全体主義', '個人', '市場'], '隷属への道'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['資本主義', '民主主義', '社会主義', '革新', '破壊'], '資本主義、社会主義、民主主義 2'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['宗教', '資本主義', '倫理', '労働', '合理化'], 'プロテスタンティズムの倫理と資本主義の《精神》'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['自殺', '社会的孤立', 'アノミー', '統合', '共同体'], '自殺論'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['政治', '権力', '責任', '倫理', '指導者'], '職業としての政治/職業としての学問'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['孤独', '大衆社会', '同調', '個性', '消費'], '孤独な群衆上'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['民主主義', '平等', '自由', '市民社会', '多数派'], 'アメリカのデモクラシー 1 上'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['言語', '記号', '差異', '構造', '意味'], '一般言語学講義抄'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['無意識', '夢', '欲望', '抑圧', '象徴'], '新訳夢判断'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['自由', '権威主義', '孤独', '逃避', '全体主義'], '自由からの逃走'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['愛', '自己', '成熟', '孤独', '依存'], '愛するということ'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['劣等感', '優越', '共同体感覚', '目的', '自己決定'], '人生の意味の心理学'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['野生の思考', '神話', '構造', '文明', '自然'], '野生の思考'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['日本文化', '恥', '名誉', '義務', '集団'], '菊と刀'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['権力', '君主', '現実主義', '統治', '政治'], 'マキャベリの「君主論」'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['権力', '国家', '自然状態', '契約', '秩序'], 'リヴァイアサン(下)'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['文明', '宗教', '対立', '政治', 'アイデンティティ'], '文明の衝突上'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['自由民主主義', '歴史', 'イデオロギー', '普遍', '終焉'], '「歴史の終わり」の後で'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['文明', '地理', '格差', '歴史', '病原菌'], '銃・病原菌・鉄上'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['人類', '歴史', '認知革命', '農業', '未来'], '文庫「サピエンス全史」「ホモ・デウス」【全4巻】セット'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['他者', '植民地主義', '権力', '表象', '東洋'], 'オリエンタリズム'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['理性', '啓蒙', '神話', '支配', '野蛮'], '啓蒙の弁証法'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s",
    (['言語', '意味', '言語ゲーム', '規則', '日常言語'], 'ウィトゲンシュタイン全集 8 哲学探究'))

cur.execute("UPDATE books SET genre_id = (SELECT id FROM genres WHERE name = '哲学') WHERE title = %s",
    ('ウィトゲンシュタイン全集 8 哲学探究',))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['官僚制', '合理的支配', '世俗化', '価値自由', '理解社会学'], '経済と社会'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['機械的連帯', '有機的連帯', 'アノミ', '集合意識', '社会事実'], '社会分業論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['社会事実', '物象化', '統計分析', '客観性', '実証主義'], '社会学的規則の基礎'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['剰余価値', '階級闘争', '疎外', '唯物史観', '商品物神化'], '資本論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['貨幣経済', '客観文化', '主観文化', '価値の尺度', '近代化'], '貨幣の哲学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['形式社会学', '社会的相互作用', '秘密', '大都市', '余暇'], '社会学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['返礼の義務', 'ポトラッチ', '全体的社会事実', '交換', '相互扶助'], '贈与論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['絶望', '実存主義', 'キリスト教', '自己疎外', '不安'], '死に至る病'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['一般意志', '人民主権', '自然状態', '社会契約', '自由'], '社会契約論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ハンナ・アーレント', '全体主義', '反ユダヤ主義', '帝国主義', 'テロル'], '全体主義の起源'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['労働', '仕事', '活動', '公共性', 'ポリス'], '人間の条件'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['鏡に映った自己', '一次集団', 'コミュニケーション', '社会意識', '相互作用'], '社会組織'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['主我', '客我', '一般化された他者', 'シンボリック相互作用論', '社会化'], '精神・自我・社会'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ドラマツルギー', '印象操作', '裏舞台', '表舞台', '社会的役割'], '日常生活における自己呈示'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['全制的施設', '精神病院', '日常の剥奪', '二次的適応', '患者アイデンティティ'], 'アサイラム'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['社会的アイデンティティ', '差別', '自己受容', '傷つけられた属性', '他者との関係'], 'スティグマの社会学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['主意主義的行為理論', 'AGIL理論', '社会構造', '機能主義', '動機づけ'], '行為の総合理論を目指して'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['構造機能主義', '社会システム', '均衡', '秩序維持', '制度化'], '社会体系論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['順機能', '逆機能', '中域の理論', '準拠集団', '予言の自己成就'], '社会理論と社会構造'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['個人的困難', '公的問題', '批判的思考', '知識人', '構造分析'], '社会学的想像力'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['軍産複合体', '支配階級', '権力集中', 'エリート循環', 'デモクラシーの危機'], 'パワー・エリート'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['知識社会学', '現実の社会的構成', '制度化', '内面化', '日常世界'], '社会的なものの構築'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['エスノメソドロジー', '日常の秩序', 'ブリーチング実験', '実践的記述', '説明可能性'], '方法の社会学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ハビトゥス', '文化資本', '趣味の闘争', '社会空間', '象徴的暴力'], 'ディスタンクシオン'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['反省的社会学', '認識論的断絶', 'プラクシス', 'フィールド論', '方法論的二元論の克服'], 'リフレクシブ・ソシオロジーへの招待'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['教育制度', '文化的再生産', '階級固定化', '隠れたカリキュラム', '象徴的支配'], '再生産'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['自己参照', 'オートポイエーシス', '環境とシステム', '複雑性の縮減', '二者択一コード'], '社会システム理論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['機能分化社会', '世界社会', 'コミュニケーションシステム', '進化のメカニズム', '偶発性'], '社会の社会'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['親密性', 'コミュニケーションメディア', '愛のコード化', '人間関係の制度化', '情熱'], '愛の構造'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['理想的発話状況', '生活世界の植民地化', '討議民主主義', '相互了解', '生活世界とシステム'], 'コミュニケーション行為論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['市民的公共圏', '言論空間', 'コーヒーハウス', 'マスメディア', '商業化'], '公共性の構造転換'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['パノプティコン', '規律権力', '一望監視方式', '身体の従属化', '刑罰の変容'], '監獄の誕生'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['非理性', '大閉じ込め', '臨床医学', '排除の論理', '理性と狂気'], '狂気の歴史'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['エピステーメー', '人間の終焉', '考古学的分析', '言語の秩序', '記号論'], '言葉と物'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['生政治', '性の管理', '告白の技術', '権力と知識', '抑制仮説への批判'], '性の歴史'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['消費の記号論', '差異化', '欲求の操作', '物神化', '大衆社会'], '消費社会の神話と構造'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['等価交換への批判', '死の排除', 'ポトラッチの再評価', 'シミュレーション', '記号経済'], '象徴交換と死'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ハイパーリアル', 'メディア社会', '複製の複製', '現実の消失', '湾岸戦争'], 'シミュラークルとシミュレーション'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['モダニティ', '都市の経験', '創造的破壊', '資本主義の発展', 'ファウスト的開発'], '現代性の経験'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['国民国家', '組織化された暴力', '行政権力', '監視社会', '戦争の歴史'], '近代国家と暴力'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['構造化理論', 'エージェンシー', '構造の二重性', '時間・空間の伸縮', '実践'], '社会の構成'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['福祉国家の改革', '新自由主義への対抗', '社会的公正', '中道左派', '包摂的社会'], '第三の道'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['純粋な関係性', 'プラスチック・セクシュアリティ', '再帰的近代化', '自己のアイデンティティ', '民主化'], '親密性の変容'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['富の分配からリスクの分配', '科学技術への不信', '破局のグローバル化', '再帰的モダニティ', '製造された不確実性'], 'リスク社会'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['伝統からの解放', '自己責任', 'アイデンティティの不確実性', '雇用流動化', '制度化された個人主義'], '個人化の進行'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['流動的近代', '消費主義', '不確実性', '人間関係の希薄化', '不安定性'], 'リキッド・モダニティ'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['合理性の歪み', '官僚制の犯罪', '道徳的盲目', '近代文明の危機', 'エンジニアリング'], '近代とホロコースト'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['時空の圧縮', '国家の衰退', 'グローバローカル', '不平等の拡大', '移動の自由'], 'グローバリゼーション'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['場所の喪失', 'プラセレスネス', '空間の経験', '近代の風景', '現象学的アプローチ'], '場所の現象学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['空間の歴史', '資本の空間', '空間的実践', '日常生活の批判', '都市空間'], '空間の生産'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['都市の民主化', '空間の私有化批判', '住民自治', '日常生活の奪還', '疎外からの解放'], '都市への権利'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['都市社会学', '集合的消費', '都市運動', '空間の階級闘争', '産業化と都市'], '都市の思想'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['情報社会', 'IT革命', '流動の空間', '再帰的アイデンティティ', 'グローバル経済'], 'ネットワーク社会の到来'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['新機能主義', '文化社会学', '社会的連帯', '理論の統合', 'アクション'], 'インサイダー・アウトサイダー'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['構造とエージェンシー', '社会変動の理論', '歴史社会学', '意味の二重性', '文化の自律性'], '構造革命'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['参与観察', 'スラム社会', 'インフォーマル組織', 'ギャングの生態', 'シカゴ学派'], 'ストリート・コーナー・ソサエティ'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['日常の危機', '死の意味づけ', '質的研究方法', '実存的解釈', 'エスノメソドロジー'], '自殺の社会学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ラベリング理論', '逸脱行動', '道徳的企業家', 'サブカルチャー', '社会的相互作用'], 'アウトサイダーズ'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['医学生の社会化', '参与観察', 'プロフェッショナリズム', '集団的適応', '状況の定義'], 'ボーイズ・イン・ホワイト'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['言語行為論', '制度的事実', '背景の能力', '集団的意図性', '構成的規則'], '社会的現実の構成'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['抽象的労働', '時間の支配', 'マルクス再解釈', '資本の論理', '価値形態'], '時間・労働・支配'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['リベラル・デモクラシー', '冷戦終結', '歴史の進歩', '承認の闘争', 'イデオロギーの終焉'], '歴史の終わり'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['文明圏の対立', '多極化世界', '文化的アイデンティティ', '西欧の衰退', 'グローバル政治'], '文明の衝突'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['中核・半周辺・周辺', '国際分業', '資本主義世界経済', '長期の16世紀', '覇権国家'], '世界システム論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['従属理論', 'ラテンアメリカの開発', '周辺国の停滞', '構造的不平等', '新植民地主義'], '従属と開発'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ポストコロニアル', '文化批判', 'インテリゲンチャ', '他者化', '知識と権力'], 'オリエンタリズム以後'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ハイブリディティ', '文化の翻訳', '第三の空間', 'ミミクリー', '植民地主義的言説'], '文化の場所'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['大きな物語の終焉', '言語ゲーム', '知識のパラダイムシフト', '情報化社会', '差異の肯定'], 'ポストモダンの条件'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['潜在能力アプローチ', '公共的理性', '不平等の是正', '自由の拡大', '比較の正義論'], '正義のアイデア'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ケイパビリティ', '開発の再定義', '実質的自由', '貧困削減', '人間中心の開発'], '自由と開発'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ジェンダーの誕生', '他者としての女性', '実存主義フェミニズム', '母性の解体', '家父長制批判'], '第二の性'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ジェンダー・パフォーマティヴィティ', '異性愛秩序の批判', '性の本質主義批判', 'クィア・スタディーズ', 'パロディ'], 'ジェンダー・トラブル'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['悲哀の政治学', '生政治の批判', '脆弱性', 'ケアの共同性', '暴力への抗議'], '触れ合えない身体'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['交差性', '黒人フェミニズム', '抑圧のマトリクス', '当事者研究', '日常の抵抗'], 'ブラック・フェミニズムの思想'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ヘゲモニー', '市民社会', '陣地戦と機動戦', '有機的知識人', '支配の同意'], 'プリズン・ノート'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ヘゲモニー理論', 'マルクス主義の発展', 'ファシズム批判', '知識人の役割', '文化支配'], '獄中記'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['階級意識', '物象化論', '弁証法', '西欧マルクス主義', 'プロレタリアート'], '歴史と階級意識'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['市場社会の誕生', '自己調整的市場', '二重の動き', '社会的埋め込み', '経済史'], '大転換'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['実在的経済', '形式的経済', '贈与と互酬', '市場主義批判', '経済人類学'], '人間の経済'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['認識論的アナーキズム', '自由な科学', '方法の相対化', '何でもあり', 'ドグマ批判'], '方法への挑戦'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['パラダイムシフト', '通常科学', '科学共同体', '不可測性', '科学史'], '科学革命の構造'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['記憶の記号学', '無意識の記憶', '近代のアイデンティティ', '時間の喪失', '主観的現実'], '見出された時'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ナショナリズム', '出版資本主義', '世俗化の進展', '言語の標準化', '国民意識の創出'], '想像の共同体'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['再分配と承認', '正義の三次元モデル', '公共圏の再生', 'フェミニズム政治学', 'ポストウェストファリア'], '国境なき正義'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ケアの倫理', '関係性の道徳', '異なる声', 'ジェンダーと発達', '他者への責任'], 'ケアの倫理'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['感情労働', '感情の管理', 'フライトアテンダント', '自己の疎外', 'サービス経済'], '感情労働'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ワークライフバランス', '家庭の市場化', '時間の貧困', 'ジェンダーの役割分担', '感情のマネジメント'], 'タイム・バインド'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['効率性・計算可能性', '予測可能性・制御', '合理性の不合理', '消費の均質化', '近代化の進展'], 'マクドナルド化する社会'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['消費のユートピア', '再呪術化', '大聖堂としてのモール', '過剰消費', 'シンボリックな価値'], '聖なる消費'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['新自由主義の統治性', 'ホモ・エコノミクス', '市場主義の浸透', '自己のテクノロジー', '国家権力の変容'], '生政治の誕生'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['条件なき贈与', '赦しの倫理', '他者への歓待', '脱構築', '正義と法'], '純粋贈与'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['脱構築', '差延', 'ロゴス中心主義批判', '音声中心主義', 'テクスト論'], 'エクリチュールと差異'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['構造人類学', '未開の思考', '民族誌', '自然と文化', '西洋中心主義批判'], '悲しき熱帯'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['近親相姦の禁忌', 'インセスト・タブー', '交換婚姻', '構造主義', 'アライアンス理論'], '親族の基本構造'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['都市の多様性', 'コミュニティの自律性', 'ストリートの治安', 'ゾーニング批判', '地域経済の発展'], '都市の経済学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ジェイン・ジェイコブズ', '近代都市計画批判', 'ストリートの目', '歩行者中心', '都市の生命力'], 'アメリカ大都市の死と生'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['知識社会学', '存在拘束性', '社会通念の分析', 'ユートピア精神', '知識人の役割'], 'イデオロギーとユートピア'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['社会診断', '危機の社会学', '理性的コントロール', '大衆社会論', '計画による自由'], '診断としての社会学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['恥と恐怖の感覚', '気配りの洗練', '心理の歴史的変容', '暴力の抑制', '宮廷化'], '文明化の過程'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['宮廷生活の社会学', '王権と貴族', '身分象徴としての作法', '相互依存関係', '感情のコントロール'], '宮廷社会'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['現象学的社会学', '意味構成', '日常世界の構造', '生活世界', '類型化'], '間主観性の社会学'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['古典派経済学', '労働価値説', '分業', '自由市場', '見えざる手'], '経済学の原理'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['共感', '道徳哲学', '市場倫理', '利己心', '社会秩序'], '道徳感情論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['比較優位', '地代論', '労働価値説', '自由貿易', '分配論'], '経済学および課税の原理'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['人口増加', '食糧供給', '貧困', '抑制', '農業経済'], '人口論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['功利主義', '自由主義', '生産論', '分配論', '労働'], '経済学原理'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['一般均衡', '価格理論', '需給均衡', '限界効用', '数理経済学'], '純粋経済学要論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['イノベーション', '企業家精神', '創造的破壊', '資本主義', '経済発展'], '経済発展の理論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['景気循環', '信用創造', '投資', '資本主義', '波動理論'], '景気循環論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['経済思想史', '分析手法', '古典派', 'ケインズ', '理論体系'], '経済分析の歴史'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['オーストリア学派', '資本理論', '景気循環', '金融政策批判', '自由市場'], '価格と生産'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['自由主義', '法の支配', '自生的秩序', '個人の自由', '福祉国家批判'], '自由の条件'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['社会主義批判', '分散知識', '計画経済の失敗', '市場秩序', '認識論'], '致命的な思いあがり'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['法の支配', '立憲主義', '自由秩序', '正義のルール', '自生的秩序'], '法と立法と自由'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['新自由主義', '市場の自由', '政府介入批判', 'マネタリズム', '個人の自由'], '資本主義と自由'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['消費者の選択', '市場経済', '規制緩和', '自由貿易', '経済的自由'], '選択の自由'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ゲーム理論', '戦略的行動', '均衡', '合理的選択', '数理経済学'], 'ゲームの理論と経済行動'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['社会的選択', '投票のパラドックス', '不可能性定理', '厚生経済学', '合理性'], '社会的選択と個人的評価'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['開発経済学', 'ケイパビリティ', '人間開発', '自由', '貧困'], '自由と経済開発'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['不平等', '分配の正義', 'ケイパビリティ', '福祉', '貧困'], '不平等の再検討'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['経済学と倫理', '合理性批判', '厚生経済学', '価値判断', '動機'], '倫理学と経済学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['外部性', '市場の失敗', '公共財', '環境経済学', '政府介入'], '厚生経済学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['不確実性', 'リスク', '利潤理論', '企業家', '市場競争'], 'リスク・不確実性・利潤'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['独占', '市場構造', '製品差別化', '不完全競争', '価格理論'], '独占的競争の理論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['不完全競争', '市場支配力', '寡占', '価格理論', 'フェミニスト経済学'], '不完全競争の経済学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['主流派経済学', 'ミクロ・マクロ経済学', '厚生経済学', '国際貿易', '入門経済学'], '経済学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['開発経済学', 'ランダム化比較試験', '貧困削減', '行動経済学', 'フィールド実験'], '貧乏人の経済学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['不平等', '資本収益率', '富の集中', '格差拡大', '累進課税'], '21世紀の資本'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['制度経済学', '国家の失敗', '収奪的制度', '包括的制度', '政治経済学'], '国家はなぜ衰退するのか'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['行動経済学', '選択アーキテクチャ', 'デフォルト設定', 'リバタリアン・パターナリズム', '意思決定'], 'ナッジ'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['行動経済学', '心理的バイアス', '合理性批判', 'ヒューリスティクス', 'プロスペクト理論'], '行動経済学の逆襲'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ケインズ経済学', '動物的本能', '不確実性', '金融市場', '心理と経済'], 'アニマルスピリット'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['グローバリゼーション', '自由貿易批判', '途上国', '不平等', 'IMF批判'], '世界を不幸にしたグローバリズムの正体'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['不平等', '格差社会', '富の集中', '機会の平等', '再分配政策'], '格差について'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['行動経済学', '認知バイアス', 'プロスペクト理論', 'ヒューリスティクス', '意思決定'], 'ファスト&スロー'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['行動経済学', '非合理的行動', '価格の錯覚', '社会規範', '意思決定'], '予想どおりに不合理'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['インセンティブ', '情報の非対称性', 'データ分析', '犯罪経済学', '応用ミクロ経済学'], 'ヤバい経済学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['消費社会', '豊かさの逆説', '需要管理', '制度派経済学', '軍産複合体'], '豊かな社会'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['産業社会', 'テクノクラート', '計画', '企業権力', '生産技術'], '新しい産業社会'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['株式市場崩壊', '投機バブル', '信用拡大', '金融恐慌', '大恐慌'], '大暴落1929'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['バブル経済', '株式市場', '非合理的熱狂', '行動ファイナンス', '資産価格'], '根拠なき熱狂'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['不確実性', '極端な事象', '確率論批判', 'リスク管理', '認識論'], 'ブラック・スワン'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['確率論', 'ランダム性', '認知バイアス', '金融市場', '運と実力'], 'まぐれ'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['反脆弱性', '不確実性', 'リスク', 'システム論', '強靭性'], '反脆弱性'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['効率的市場仮説', 'インデックス投資', '株式市場', 'ランダムウォーク', '資産運用'], 'ウォール街のランダム・ウォーカー'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['貨幣理論', '信用', '物価水準', '金融政策', '利子率'], '貨幣論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['環境経済学', '資源の限界', '持続可能性', 'システム思考', '経済成長批判'], '成長の限界'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['幸福経済学', '主観的幸福', '所得と幸福', '精神的健康', '公共政策'], '幸福の経済学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ゲーム理論', '繰り返しゲーム', '協力戦略', '囚人のジレンマ', '社会規範'], '協力の進化'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['経済発展段階論', '近代化論', '離陸理論', '工業化', '途上国開発'], '経済成長の段階'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['資本主義の精神', '宗教と経済', '合理化', '禁欲主義', '労働倫理'], 'プロテスタンティズムの倫理と資本主義の精神'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['制度派経済学', '誇示的消費', '余暇階級', '社会的地位', '消費文化'], '有閑階級の理論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['取引費用', '企業の本質', '市場と組織', '制度経済学', '所有権'], '企業・市場・法'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['一般均衡', '消費者理論', '需要理論', '資本理論', '厚生経済学'], '価値と資本'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['飢饉', '権原理論', '食糧安全保障', '貧困', '分配'], '貧困と飢饉'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['社会正義', '比較アプローチ', 'ケイパビリティ', '民主主義', '公共的理性'], '正義のアイデア'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['制度変化', '歴史的経路依存', '取引費用', '財産権', '経済パフォーマンス'], '制度・制度変化・経済成果'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['経済史', '制度', '財産権', '国家の役割', '技術変化'], '経済史の構造と変化'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['公共選択論', '投票行動', '政府の失敗', '官僚制', '憲法経済学'], '同意の計算'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['貨幣供給', '大恐慌', 'マネタリズム', '連邦準備制度', '金融政策'], 'アメリカ合衆国の金融史'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['帝国主義', '資本蓄積', '過少消費', '植民地主義', 'マルクス経済学'], '資本蓄積論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['帝国主義', '独占資本主義', '植民地支配', '資本輸出', 'マルクス主義'], '帝国主義論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['金融資本', '銀行と産業の融合', '独占', '帝国主義', 'マルクス主義'], '金融資本論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['帝国主義批判', '資本輸出', '過少消費', '植民地主義', '自由主義'], '帝国主義'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['不確かな時代', '経済思想史', '権力と経済', '企業支配', 'テレビ経済学'], '不確かさの時代'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['グローバリゼーション', '自由貿易の限界', '国家主権', '民主主義', 'トリレンマ'], 'グローバリゼーション・パラドクス'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['マクロ経済学', 'GDP', '財政政策', '金融政策', '経済成長理論'], 'マクロ経済学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ミクロ経済学', '消費者理論', '生産者理論', 'ゲーム理論', '市場均衡'], 'ミクロ経済学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['グローバリゼーション批判', '不平等', '途上国', '貿易政策', '開発経済学'], '世界に格差をバラ撒いたグローバリズムを正す'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['スポーツ経済学', '統計分析', '情報の非対称性', 'データ革命', '人材評価'], 'マネーボール'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['金融危機', 'サブプライムローン', '空売り', 'リスク', '金融工学'], '世紀の空売り'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['不平等', 'グローバル格差', '中間層の空洞化', '資本収益', '所得分配'], '大いなる不平等'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['気候変動', '環境経済学', '炭素税', '持続可能な開発', '外部性'], '気候変動の経済学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['選択のパラドックス', '意思決定', '消費者行動', '選好', '心理経済学'], '選択の科学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['比較制度分析', '日本経済', '組織と市場', '進化ゲーム理論', '制度設計'], '比較制度分析に向けて'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['分配的正義', '無知のヴェール', '格差原理', '社会契約', '平等主義'], '正義論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['貧困削減', '開発援助', 'ミレニアム開発目標', '経済成長', 'アフリカ開発'], '貧困の終焉'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['価値論', '生産価格', '剰余価値', '古典派経済学', '再生産表式'], '商品による商品の生産'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['限界効用', '価値論', '数理経済学', '交換理論', '古典派批判'], '経済学の理論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['貨幣論', '資本主義', '利子論', '哲学と経済学', '日本経済論'], 'ヴェニスの商人の資本論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['マルクス経済学', '宇野理論', '資本の運動', '価値形態論', '段階論'], '経済原論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['日本経済史', '高度成長', 'バブル経済', '産業政策', '戦後復興'], '戦後日本経済史'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['日本経済', '戦時体制', '官僚制', '金融統制', '制度的連続性'], '1940年体制'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['競争優位', '産業クラスター', 'ダイヤモンドモデル', '国際競争力', '経営戦略'], '国の競争優位'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['アイデンティティ', '社会規範', '帰属意識', '行動経済学', '自己概念'], 'アイデンティティ経済学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['リーマンショック', '金融危機', 'ケインズ政策', '流動性の罠', '財政出動'], '世界大不況への警告'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['デジタル資本主義', '行動データ', 'プライバシー', 'プラットフォーム', '監視社会'], '監視資本主義'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['ドーナツ経済学', '惑星の限界', '社会的基盤', '持続可能性', '成長批判'], 'ドーナツ経済'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['負債と貨幣', '贈与経済', '信用の歴史', '資本主義批判', '人類学的経済学'], '負債論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['イノベーション政策', '国家の役割', 'リスクと報酬', '産業政策', '公共投資'], '企業家としての国家'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['技術革新', '自動化', '労働市場', 'デジタル経済', '生産性'], 'ザ・セカンド・マシン・エイジ'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['技術と雇用', '自動化', '労働代替', '生産性', 'AI経済学'], '機械との競争'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['技術と経済成長', '産業革命', '自動化の歴史', '労働市場', '技術的失業'], 'テクノロジーの世界経済史'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['取引費用', '組織の経済学', '契約理論', '企業の境界', '制度経済学'], '資本主義の経済制度'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['組織論', '市場と階層', '取引費用経済学', '企業統治', '官僚制'], '市場と企業組織'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['イノベーション', '途上国開発', '市場創造', '雇用創出', '経済成長'], '繁栄のパラドクス'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['経済ナショナリズム', '保護貿易', '国民経済', '生産力理論', '自由貿易批判'], '国民経済学の体系'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['重農主義', '純生産物', '農業経済', '経済循環', 'フランス経済'], '経済表'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['不平等', '再分配政策', '資本課税', '労働市場', '技術変化'], '不平等'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['資本と格差', '21世紀の不平等', '参加型社会主義', '累進課税', '資産分配'], '新・資本論'))

cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['経済倫理', '合理化', '世界宗教', '資本主義', '比較社会'], '宗教社会学論集'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['一神教', '預言者', '律法', '賤民', '合理主義'], '古代ユダヤ教'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['カースト', '輪廻', '仏教', 'ヒンドゥー', '神義論'], 'インドの宗教'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['儒教', '道教', '家産制', '官僚制', '現世肯定'], '中国の宗教'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['集合意識', '聖俗', '儀礼', '社会統合', 'トーテム'], '宗教生活の原初形態'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['相互作用', '信仰', '形式', '敬虔', '社会関係'], '宗教の社会学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['世俗化', '正当化', '疎外', '意味', '社会構築'], '聖なる天蓋'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['超自然', '超越', '信仰', '兆候', '現代社会'], '噂の天使'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['選択', '多元化', '個人化', '相対主義', '現代宗教'], '異端の時代'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['反世俗化', '復興', '多元主義', '保守派', 'グローバル'], '脱世俗化の時代'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['個人化', '私事化', '主観主義', '意味体系', '自己'], '見えない宗教'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['聖俗', '顕聖', '宇宙化', '空間', '時間'], '聖と俗'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['円環', '初源', '神話', '模倣', '歴史'], '永遠の回帰の神話'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['脱魂', '忘我', '宇宙樹', '入巫', '呪術'], 'シャーマニズム'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['大母神', '農耕', '秘儀', '象徴', '再生'], '豊饒と再生'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['畏怖', '魅惑', '非合理', '神秘', '神聖'], '聖なるもの'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['心理', '神秘', '回心', '救済', '信仰'], '宗教経験の諸相'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['心学', '道徳', '経済倫理', '近代化', '価値'], '徳川時代の宗教'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['個人主義', '共同体', '道徳', '伝統', '市民'], '心の習慣'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['象徴', '進化', '神話', '儀礼', '人類史'], '宗教の進化'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['呪術', '王殺し', '植物神', '類感', '感染'], '金枝篇'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['霊魂', '進化', '残存', '文化', 'アニミズム'], '原始文化'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['供犠', '共同食', '氏族', 'トーテム', '儀礼'], 'セム族の宗教'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['機能', '心理', '感情', '未開', '文化'], '呪術・科学・宗教'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['部族', '精霊', '象徴', '構造', '人類学'], 'ヌアー族の宗教'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['妖術', '託宣', '合理性', '認識', 'アフリカ'], 'アザンデ人の呪術'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['分類', '境界', '汚穢', '秩序', '象徴'], '汚穢と禁忌'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['グリッド', 'グループ', '身体', '構造', '儀礼'], '自然象徴論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['境界', '移行', '象徴', '共同体', '儀礼'], '儀礼の過程'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['象徴', '機能', '紛争', '過程', '部族'], '象徴の森'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['分離', '過渡', '統合', '境界', '図式'], '通過儀礼'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['聖化', '贖罪', '交換', '媒介', '機能'], '供犠論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['マナ', '表象', '隠秘', '社会', '象徴'], '呪術論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['無意識', '父殺し', '罪悪感', '禁忌', '精神'], 'トーテムとタブー'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['批判', '無意識', '防衛', '科学', '願望'], '幻想の未来'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['記述', '象徴', '意味', '解釈', '文化'], '文化の解釈学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['劇場', '国家', '権力', '儀礼', '象徴'], 'ヌガラ'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['神話', '象徴', '対話', '精神', '普遍性'], '神話の力'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['英雄', '旅', '無意識', '通過', '構造'], '千の顔をもつ英雄'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['言語', '自然', '比較', '起源', '神話'], '宗教の起源と発展'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['世俗化', '都市化', '実用', '匿名', '現代'], '世俗の都市'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['神学', '脱呪術', '教会', '現代', '超克'], '神の世俗化'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['人道主義', '世俗', '近代', '信仰', '自己'], '世俗の時代'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['世俗化', 'セクト', '新宗教', '変動', '合理化'], '宗教と社会変動'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['衰退', '制度化', '現代', 'セクト', '世俗化'], '現代宗教の社会学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['セクト', '類型', '排他', '組織', '救済'], 'セクターと社会'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['公共圏', '市民', '分離', '公的', '宗教'], 'パブリック・レリジョン'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['概念', '権力', '規律', '近代', '系譜'], '宗教の系譜'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['世俗', '国家', '身体', '倫理', '形成'], '世俗の形成'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['選択', '人脈', '疫病', '改宗', '資本'], 'キリスト教興隆の社会学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['市場', 'カルト', 'セクト', '限界', '補償'], '宗教の未来'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['個人化', '霊性', '構造', '自己', '変容'], '神への信仰の変容'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['小集団', '共同体', '信仰', '人脈', '意味'], '意味の共同体'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['カルト', '新宗教', '洗脳', '報道', '反応'], 'カルトの社会学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['テロ', '戦争', '原理主義', '暴力', '殉教'], '神のテロル'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['国家主義', '自己', '政治', '紛争', '反発'], 'ナショナリズムと宗教'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['聖戦', 'テロ', '過激派', '運動', '復興'], 'アラーの聖戦'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['同胞団', '復興', '政治', '運動', '歴史'], '預言者とファラオ'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['部族', '国家', '分節', '構造', '社会'], 'イスラームの政治社会学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['記憶', '伝統', '継承', '世俗', '自己'], '記憶としての宗教'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['移動', '人脈', '個人', '霊性', '巡礼'], '巡礼の社会学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['制度外', '記憶', '代理', '世俗', '聖性'], '聖性を生きる'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['個人化', '信仰', '離脱', '所属', '現代'], '所属なき信仰'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['救世主', '異端', '中世', '理想', '終末'], '千年王国の社会学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['魔女', '悪魔', '迫害', '異端', '心理'], '悪魔の徴章'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['カルト', '反発', '終末', '運動', '解放'], '千年王国論'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['抑圧', '救済', '新宗教', '預言', '変革'], '偉大なる変革の宗教'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['異端', 'セクト', '抵抗', '社会', '分派'], '異端の社会学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['迫害', '模倣', '供犠', '暴力', '浄化'], '暴力と聖なるもの'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['神話', '迫害', '模倣', '犠牲', '批判'], '身代わりの山羊'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['記憶', '文字', '記念碑', '自己', '文化'], '文化の記憶'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['境界', '記憶', '暴力', '起源', '一神教'], '一神教の誕生'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['システム', '分化', '暗号', '偶然', '意味'], '宗教の機能'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['伝達', '世界', '観察', 'システム', '分化'], '社会の宗教'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['比較', '普遍', '霊性', '世界観', '伝統'], '世界の宗教'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['多元', '現象', '次元', '対話', '世界'], '比較宗教の世界'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['世界観', '神話', '儀礼', '経験', '制度'], '世界宗教の思想空間'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['中世', '文明', '形成', 'カトリック', '欧州'], 'ヨーロッパの形成'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['神秘', '実践', '他者', '歴史', '言説'], '天と地'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['主観', '癒やし', '個人', '現代', '霊性'], 'スピリチュアリティ革命'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['自己', '霊性', '代替', '消費', '神聖'], '聖なるエゴイズム'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['憑依', '忘我', '周辺', '女性', '構造'], '憑依の解剖学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['浄不浄', '階層', '全体論', '構造', '身分'], 'カーストの体系'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['階層', '批判', '社会', '比較', '全体論'], 'ホモ・ヒエラルキクス'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['実践', '信仰', '精霊', '人類学', '社会'], '仏教と社会'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['信仰', '習合', '儀礼', '心理', '仏教'], 'ビルマの宗教'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['批判', '家産制', '中東', '近代化', '分析'], 'イスラームの社会学的分析'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['比較', '資本', '合理化', '方法', '分析'], 'マックス・ウェーバーと宗教社会学'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['倫理', '資本', '社会', '興隆', '歴史'], '宗教と資本主義の興隆'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['天皇', '祭政', '神社', '近代', '思想'], '国家神道'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['新宗教', '民衆', '崇拝', '国家主義', '市民'], '日本の市民宗教'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['祖霊', '民俗', 'お盆', '死生観', '家族'], '先祖の話'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['来訪神', '文学', '祝詞', '神道', '民俗'], '古代研究'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['山岳', '習合', '儀礼', '組織', '民俗'], '修験道'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['憑依', '巫女', '神様', '社会', '構造'], 'シャーマニズムの構造'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['情報', 'カルト', '人脈', '世界', '教団'], '新宗教の解読'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['霊性', '若者', '癒やし', '現代', '流行'], '新新宗教と宗教ブーム'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['分離', '神道', '戦後', '公共', '慰霊'], '国家と宗教'))
cur.execute("UPDATE books SET ideology_keywords = %s WHERE title = %s", (['創唱', '自然', '世俗', '感覚', '信仰'], '日本人はなぜ無宗教なのか'))

# すべてのUPDATEをまとめてコミット（DBに確定）する
conn.commit()
cur.close()
conn.close()
print("完了")
