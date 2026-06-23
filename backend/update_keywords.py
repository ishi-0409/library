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

# すべてのUPDATEをまとめてコミット（DBに確定）する
conn.commit()
cur.close()
conn.close()
print("完了")
