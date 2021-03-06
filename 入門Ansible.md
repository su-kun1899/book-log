# 入門Ansible

- 構成管理ツール
- sshだけがあればいい
- inventoryファイルだけがあればいい
  - 実際にはplaybookも使う
- inventoryファイル
  - ホストの情報を書く
- playbook
  - varsで変数を宣言
    - 入れ子にできる
    - vars_filesを使えば別ファイルから読み込める
  - task
    - sudo(become)はtaskごとにも指定できる
  - handler
    - taskのnotifyにhandlerのnameを指定
    - taskに変更があった場合だけhanlerが実行される
    - serviceの再起動等に使える
    - notifyで複数のhandlerを起動することも可能

## よく使うモジュール

- script
  - シェルスクリプトが実行できる
  - createsでファイル有無による実行制御ができる
- command
  - コマンドを対象ホストで実行する
  - chdir引数で作業場所を変更できる
  - リダイレクトやパイプは使えない
- shell
  - リダイレクトやパイプが使える
- file
  - ファイルやディレクトリの作成
  - ownerやgroupの変更
  - シンボリックリンクの作成
- copy
  - 管理ホストのファイルを対象ホストにコピーする
- fetch
  - 対象ホストから管理ホスト側にファイルを送る
  - ログの収集に使える？
- template
  - jinja2を使う
  - テンプレートの変数を展開して、対象ホストでファイルを作成する
- get_url
  - URLからファイルをダウンロードする
  - destをファイルにすると、既にファイルがあるとダウンロードしない
    - 冪等性を考えるならこちらの方がよいかも
- lineinfile
  - ファイルの中の任意の一行を設定・削除する
  - regexpで対象行を指定する
    - 指定がなければ末尾に追記
- replace
  - 複数行をまとめて置換したい場合はこちら
- unarchive
  - 管理ホストにある圧縮ファイルを対象ホストに転送して解凍する
- yum
  - yumコマンドを使ってパッケージをインストールする
- service
  - serviceコマンドを使える
  - sleepで停止起動のインターバルを指定できる
  - enabled=yesでホスト起動時にサービスが起動するようにできる
- user
  - ユーザーを追加・削除する
  - passwordはハッシュ化して指定する
    - mkpasswdが使えれば `mkpasswd --method=SHA-512`
    - pipで `passlib` を使ってもいい
      - `python -c "from passlib.hash import sha512_crypt; print (sha512_crypt.encrypt('hogehoge'))"`
- authorized_key
  - SSHのauthorized keyを追加
- wait for
  - 状態の監視による待機ができる
    - ポートが開くまで待つ、ファイルが消えるまで待つ、logに特定の文字が吐かれるまで待つ
    - etc
  - 単純に時間で待つだけならcommandモジュールでsleepする方が楽
- irc
  - ircにメッセージを送れる
  - Slackやメール通知のモジュールもあった
- debug
  - 任意の内容を表示する
  - 変数の確認などに使える
  - `stdout.find()` を使うと文字列が含まれているか調べられる

## 複雑な処理

- 繰り返し
  - with_items
  - 入れ子ループ
    - with_nested
    - ただし１階層
  - key-valueのマッピングをループ
    - with_dict
  - 管理ホスト側のファイルをループ
    - with_fileglob
    - ファイルがない場合スキップされる（エラーも出ない）
- 出力を使い回す
  - register
  - モジュールの出力を保存しておける
  - debugで中身を確認しながら使うと良い
- 条件付き実行
  - when
  - is definedで変数が定義されているかどうかチェックできる
  - andやorも指定可能
  - registerとの連携も可能
    - failed
    - success
    - skipped
    - changed
- 成功するまで繰り返す
  - until
- 外部情報の参照
  - lookup
  - プラグインを使って値を取り出せる
    - 環境変数、redis、file
    - 実行は管理ホスト側
- 変数を処理する
  - filter
- キーボードから入力する
  - vars_prompt
- 管理ホストで実行する
  - local_action
  - 事前に送信ファイルを圧縮したりとか
- 実行するモジュールを変数で変更する
  - action
  - あまり使わないかも
- 環境変数を設定する
  - environment
- 失敗しても無視する
  - ignore_errors
  - 終了コードで動作を変えられる
  - 失敗条件を定義
    - failed_when
  - 変更条件を定義
    - changed_when
- 非同期でtaskを実行する
  - async

## 大規模なplaybook

- 他のplaybookを読み込む
  - include
- taskファイルは分割可能
  - 変数を渡すこともできる
- 推奨ディレクトリ構成がある
- role
  - 再利用する一連のtask
  - roleの推奨ディレクトリ構造もある
  - tasksだけあればよい
  - 変数名のprefixにrole名をつけてあげると衝突が避けやすい
- 並列実行
  - fork
- 順々に実行
  - serial
- ホストのリストを動的に作成
  - dynamic inventory
  - AWS の EC2 hostリストを取得できる
  - inventory ファイルにディレクトリを指定するとすべてのファイルを inventory ファイルとして扱う
    - 静的なファイルと動的なファイルの共存が可能になる

## コマンドラインオプション

- ssh認証
  - ユーザとかパスワードとか
- 対象ホストを制限
  - limit
- 実行するタスクを制限
  - tags
- dry-run
  - check
- taskを確認しながら実行
  - step
- 差分表示
  - diff

## 変数ファイルの暗号化

- ansible-vault
- 暗号化ファイルを作成
  - create
- 既にあるファイルを暗号化
  - encrypt
- 復号化
  - decrypt
- 編集
  - edit
- パスワードの変更
  - rekey
- 使い方
  - vars_files に設定
  - ask-vault-pass オプションか vault-password-file オプションを使う

## よくあるご質問

- 一つの playbook が複雑になってしまった
  - role に分割していく

## モジュールを自作する

- 既存のモジュールの組み合わせでできるなら作成しないほうがよい

## plugin を自作する

- Ansibleの動作を拡張できる
- lookup plugin
  - 変数を動的に設定する
  - 環境変数や redis から取得した値を変数に格納する
- filter pluguin
  - Jinja2 で使う filter を拡張する
  - base64 encode/decode
  - failed, success, changed に必ずする
    - テストで有用
  - 正規表現
  - ファイルパス
  - ランダムな数字
- callback plugin
  - playbook 開始時、task 終了時、エラー発生時の callback を設定できる
  - 標準で提供されているものはない
  - チャットやメールに通知するサンプルがある
- action plugin
  - モジュールと組み合わせて使う
  - 管理ホスト側でモジュール実行の前準備をさせる
- connection type plugin
  - 操作対象に対して接続する
  - 自作することはほぼない
- vars plugin
  - group_vars や host_vars の変数を設定する
  - 自作が非推奨
  - inventory スクリプトで変数を扱う方が容易
