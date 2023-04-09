import collections
import MeCab
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
sns.set(font='Hiragino Sans')

#textファイルの読み込み
f= open('.txt', 'r', encoding='UTF-8')
text=f.read()
f.close()

#読み込んだtextファイルで形態素解析を行う
tagger =MeCab.Tagger()
tagger.parse('')
node = tagger.parseToNode(text)

#取り出す品詞を決めている.今回は名詞と代名詞
word_list=[]
while node:
    word_type = node.feature.split(',')[0]
    if word_type in ["名詞",'代名詞']:
        word_list.append(node.surface)
    node=node.next
word_chain=' '.join(word_list)

c=collections.Counter(word_list)

#フォントパスの指定
font_path='/System/Library/Fonts/ヒラギノ明朝 ProN.ttc'
#wordcloud上から除外するワードの設定
words = ["もの","こと","あれ","それ","どれ","です","ます","こと"]

#wordcloudを実行する
#regexp=r"[\w']+"で1文字のものも取り出す
#result.to_fileでpngファイルとして出力
#printでよく使われている単語top20を出力
result = WordCloud(width=800, height=600, background_color='white', 
                   font_path=font_path,regexp=r"[\w']+", 
                   stopwords=words).generate(word_chain)
result.to_file("./wordcloud_sample1.png")
print(c.most_common(20))

#形態素解析の結果と合わせてグラフ化する
fig = plt.subplots(figsize=(8, 10))
sns.set(font="Hiragino Maru Gothic Pro",context="talk",style="white")
sns.countplot(y=word_list,order=[i[0] for i in c.most_common(20)],palette="Blues_r")
