# ゲームを作りながら楽しく学べるPythonプログラミング

## 第2章

### 演算

- %  (余りを求める)
- // (商を整数で求める)
- ** (べき乗を求める)

```py
# 商と余りを一度に求める
divmod(11, 4) # (2, 3)
```

### 変数

- 特に修飾子は不要？

```py
hoge = 1
```

### 関数

- 特定のオブジェクトに紐付いているものはメソッド
- そうでないものは関数

```py
max(2, 6) # 6
```

### 型

- type関数で調べられる

```py
type(5)       # int
type(3.14)    # float
type("hoge")  # str
type('fuga')  # str
type(True)    # bool
```

### キャスト

```py
int("-5")       # 整数型へ
float("-3.14")  # 浮動小数点型へ
str(7)          # 文字列型へ
bool(0)         # 真偽値型へ
```

### 配列

```py
# タプル(不変)
(78, 95, 68, 62)
# リスト(可変)
[78, 95, 68, 62]
```

#### リストの操作

```py
scores = [78, 95, 68, 62]
# 要素の追加
scores.append(55)
# 指定した位置に要素を挿入
scores.insert(3, 88)
# 要素の削除
del scores[2]
# 要素を取り出して削除
scores.pop(2)
```

#### タプルとアンパック

- タプルを展開して変数に格納する(アンパック)

```py
pos = (56, 74)
pos_x, pos_y = pos
# pos_x: 56, pos_Y: 74
```

- アンパックして格納し直すと変数の値を入れ替えられる

```py
x = 3
y = 6
(x, y) = (y, x)
```

### 辞書

- ハッシュテーブル、キーバリューペア

```py
score = {
	"math" : 78,
	"english" : 95,
	"chemistry" : 68,
	"science" : 62,
}
# 要素の追加
score["math"] = 82
```

### リストやタプルを扱うのに便利な関数

```py
# 要素の数を返す
len([1, 2, 3, 4, 5])

# リストを複製する
a = [1, 2, 3]
b = a.copy()

# 要素を含んでいるか調べる
greets = ("morning", "afternoon", "evening")
"noon" in greets #False
"afternoon" in greets #True
# 要素の位置を確認する場合はindex(存在しない場合はエラー)
greets.index("afternoon") # 1

# 並び替える
fruits = ["banana", "apple", "peach", "orange"]
fruits.sort()
# 並び替えた新しいリストを返す
sortedFruits = sorted(fruits)
```

### 標準出力

- printを使う

```py
print("hello")
# 可変長引数も使える
print("Hello,", "Python", 3) # Hello,Python3
```

### 書式付き文字列

- `書式付き文字列 % データを含むタプル`
- 書式
  - %s 文字列
  - %d 10進数
  - %x 16進数
  - %f 10進数float

```py
"1=%s 2=%s" % ("Hello", "World") # 1=Hello 2=World
```

#### formatメソッド

- `書式付き文字列.format(データの可変長引数)`

```py
"1={0} 2={1}".format("Hello", "World") # 1=Hello 2=World
```

### 行の折り返し

- コードの途中で改行したい場合はバックスラッシュを使う
- リストの要素などではバックスラッシュが不要な場合もある

## 第3章

### インデント

- Pythonは一段落に4つのスペースがよいとされている

### 条件式の評価

- 式の結果が「True」もしくは「0以外」の場合成立していることになる

#### 比較演算子

- A == B
- A != B
- A < B
- A <= B
- A > B
- A >= B
- A in B
  - AがB(リストやタプル)に含まれている場合True

#### ブール演算子

- 条件式1 and 条件式2
- 条件式1 or 条件式2
- not 条件式1
- ひとつ変数で複数のandは省略記法が使える

```py
x = 7
0 < x and x < 10 #True
0 < x < 10 #書き換え可能
```

### if文

- インデントがブロックになる

```py
fruit = "banana"

if fruit == "apple":
	print("red")
elif fruit == "banana":
	print("yellow")
else:
	print("unknown")
```

### ブール値以外の値

- bool関数で調べられる
  - 数値
    - ゼロ以外True
  - 文字列
    - 空文字はFalse
  - リスト・タプル
    - 空リスト・空タプルはFalse

```py
bool(0.0) # False
bool('') # False
bool([]) # False
```

### 三項演算子

```py
a = 5
x = 10 if a > 0 else 20 # 10
```
