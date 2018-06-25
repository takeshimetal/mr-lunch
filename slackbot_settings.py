import os

# botアカウントのトークンを指定
API_TOKEN = 'xoxb-119407525890-385446795888-knmgW0XNxuXRpMXMy6T8yzpu'

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = '日本語でおk'

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']

# デプロイ権限をもつ管理ユーザ名のリスト
# export paccho_admin_users=hoge,foo,bar のようにカンマ区切りで複数指定できる
#ADMIN_USER_NAME_LIST = os.environ.get('paccho_admin_users', '').split(',')
