## pretend_superuser

djangoのmanage.py関連コマンド入力時の挙動を模した、パロディプログラムです。  
  
pythonの標準ライブラリ(os, sys, argparse, csv, unittestなど)の  
実践練習、復習を主な目的として作成しました。  
  
#### 動作に関して

このリポジトリで管理されている他のプログラムとは違い、  
`~/pretend_superuser/manage.py`が起動の起点になっています。  
  
コマンドについては、現状、以下の２種が利用可能です。
```
$ python3 manage.py createsuperuser  
$ python3 manage.py runserver
```  
csvファイルを利用したUserの作成、データの閲覧、削除ができます。  
  