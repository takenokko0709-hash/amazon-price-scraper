# amazon-price-scraper
【Python】Amazon商品情報自動取得ツール（CSV出力機能付き）
工夫した点: 「Excelを持っていないユーザーでも使えるようCSV形式を採用し、文字化け防止のためにUTF-8(BOM付き)で出力しました」

苦労した点: 「Amazonのロボット判定を回避するために、User-Agentの設定を工夫しました」
[amazon_results.csv](https://github.com/user-attachments/files/24517960/amazon_results.csv)


## 🚀 使い方（cmdで入力)
1. ライブラリをインストール
   `pip install requests beautifulsoup4`
2. プログラムを実行
   `py amazon_search.py`

   ## 🛠 特徴
- **環境を選ばない:** ExcelがなくてもGoogleスプレッドシート等で閲覧可能なCSV形式を採用。
- **実用性:** 収集したデータは `amazon_results.csv` として保存され、文字化け対策（UTF-8 with BOM）済み。
- **回避策:** Amazonのアクセス制限を考慮したヘッダー設定。

実行するとこのような感じになります


商品名,価格(円)
Amazonベーシック 有線キーボード 日本語配列 ブラック,1267
【Amazon.co.jp限定】ロジクール MX KEYS mini KX700GRd ミニマリスト ワイヤレス イルミネイテッド キーボード グラファイト 充電式 Bluetooth Logi Bolt Unifying非対応 USB-C-A 日本語配列 無線 KX700 国内正規品,16698
AIM1 瞬 MATATAKI ラピッドトリガー ポーリングレート8000Hz対応 日本語配列 有線 75%サイズ バックライトLED ゲーミングキーボード 磁気式スイッチ,14980
"Flow2 ロープロファイル 68キー メカニカルキーボード - Void リニアスイッチ搭載・アルミニウム合金ボディ 充電式ワイヤレス3モード接続対応 Windows/MacOS用、英语配列 技適認証取得 (シルバー静音, 68)",28600
エレコム 有線キーボード メンブレン ブラック TK-FFCM01BK,1099
ロジクール ワイヤレスキーボード K295GP 静音 耐水 キーボード 無線 Unifying K295 windows chrome グラファイト 国内正規品,3163
ワイヤレス Bluetooth キーボード 折りたたみ式 スタンド付き 薄型 IOS/Android/Windows/Mac 兼用 コンパクト 充電式 ホワイト,3999
エレコム ワイヤレスキーボード メンブレン 薄型 フルキーボード テンキー ブラック TK-FDM110TXBK,1899
エレコム ワイヤレスキーボード マウスセット メンブレン 薄型 フルキーボード ブラック TK-FDM110MBK,2499
バッファロー BUFFALO USB接続 有線スタンダードキーボード ブラック BSKBU105BK【Windows/PS4/Nintendo Switch対応】,1080
エレコム ワイヤレスキーボード 静音 テンキー付 薄型コンパクトサイズ Windows ChromeOS macOS対応 ブラック TK-QT30DMBK,3099
ゲーミングキーボード 赤軸 98 キー メカニカル LED バックライト付き ワード発光 USB 有線 高速応答 数字キー付き 音量調整ノブ オフィス/ゲーミング コンピューター キーボード (ゲーミングキーボード) 贈り物 白色,5699
ProtoArc キーボード ワイヤレス マウスセット 折りたたみ式 3台同時接続 Bluetooth/USB接続 無線 軽量 コンパクト フルサイズ USB-C充電式 スマホ用スタンド 収納バッグ付属 マウス キーボードBluetooth ビジネス/出張/旅行用 Ｗindows/Mac/iOS/Android対応 XKM01 黒,8980
"EPOMAKER TH87 JIS 日本語配列 TKL ワイヤレスゲーミングキーボード 2.4GHz/BT5.0/有線 テンキーレス ホットスワップ対応 10000mAh 無線 メカニカルキーボード 91キーリニアスイッチ RGBバックライト ガスケット構造 PBTキーキャップ Windows mac対応 (Blue&White, Sea Salt Silent)",12499
TK-PN10FMPWH ホワイト フルサイズ ワイヤレスキーボード Bluetooth & 無線2.4GHz両対応 日本語配列 超薄型,7280
【Amazon.co.jp限定】 Logicool G PRO ゲーミングキーボード G-PKB-002LNd テンキーレス リニア 赤軸 静かなタイピング GXスイッチ 有線 ゲーミング メカニカルキーボード 日本語配列 LIGHTSYNC RGB 充電 着脱式ケーブル 国内正規品 ※Amazon限定の壁紙ダウンロード付き,13829
エレコム USB キーボード ワイヤレス (レシーバー付属) メンブレン コンパクトキーボード ブラック TK-FDM105TXBK,1453
ロジクール ワイヤレスキーボード K295OW 静音 耐水 キーボード 無線 Unifying K295 windows chrome オフホワイト 国内正規品,3200
[ 2025年新開発 ] iPad Air 11インチ キーボード M3 2025/M2 2024 iPad Air5 Air4 キーボード ケース 7色バックライト 人気 超軽量 脱着式 iPad Pro 第4/3/2/1 兼用 ペンシルホルダー付き Bluetooth i-Pad Air 第5/4世代 キーボ ード オートスリープ機能 全面保護 多角度調整 耐久性 ブルー,3599
"YUNZII RT68 ゲーミングキーボード ラピッドトリガー メカニカルTKL ゲーミング 磁気スイッチ RGB 有線 USB コンパクト 65%配列68キーノブ付きPBT キーキャップ 調節可能作動 (ベージュ, OUTEMUスイッチ)",7499
【最新型】ProtoArc XK01 折りたたみキーボード Bluetooth 薄型 軽量 3台同時接続 iphone ipad キーボード 日本語配列 Type-C充電式 フルサイズ iOS/Android/Mac/Windows対応 ipad mini パソコン タブレット スマホ用 テンキー付き パンダグラフ シルバー＆ホワイト,5580
【Amazon.co.jp限定】RK ROYAL KLUDGE R65 ゲーミングキーボード 有線 日本語配列 メカニカルキーボード 60%コンパクトキーボード 70キー テンキーレス ホットスワップ可能 ボリュームノブ搭載 クリームスイッチ RGBバックライト PBTキーキャップ ガスケットマウント ブラック,9500
ロジクール 有線 キーボード 耐水 K120 USB接続 日本語配列 テンキー 薄型 有線キーボード 国内正規品,2200
ロジクール ワイヤレスキーボード PEBBLE KEYS 2 K380sGR 薄型 軽量 415g 小型 Bluetooth Logi Bolt ワイヤレス 無線 キーボード Easy-Switch 日本語配列 電池寿命36ケ月 Windows Mac iPad iOS Android Chrome K380s グラファイト 国内正規品,4618
エレコム ゲーミングキーボード 有線 TK-G02UMBK 着脱式リストレスト付 ボリュームダイヤル メンブレン フルキー ブラック,3408
エレコム キーボード 有線 パンタグラフ ミニキーボード ブラック TK-FCP096BK,1991
エレコム キーボード 有線 メンブレン 薄型 フルキーボード ブラック TK-FCM108XBK,1280
バッファロー ワイヤレス 無線 コンパクト キーボード 薄型 持ち運び テンキーレス メンブレン USB レシーバー付属 ブラック BSKBW145BK,1480
UGREEN ワイヤレス 無線 キーボード Bluetooth +2.4G 三台切替可能 静音設計 キーボード 超軽量 薄型 人間工学デザイン 78キー 日本語配列 高耐久 簡単接続,3205
【Amazon.co.jp限定】 ロジクール Bluetooth ワイヤレスマウス キーボード セット MK250GRd テンキー コンパクト 日本語配列 耐水 無線 ワイヤレス MK250 Windows Mac Chrome グラファイト 国内正規品 ※Amazon.co.jp限定 壁紙ダウンロード付き,3539
ロジクール SIGNATURE SLIM ワイヤレス キーボード K950GR 薄型 静かなタイピング Bluetooth Logi Bolt ワイヤレスキーボード テンキー 無線 Easy-Switch 日本語配列 電池寿命36ケ月 Windows Mac Chrome Android K950 グラファイト 国内正規品,9817
【日本語配列】HyperX Alloy Core RGB ゲーミングキーボード ゲーマー向け LEDバックライト 耐水性 2年保証 HX-KB5ME2-JP ( 4P4F5AJ#ABJ ),4527
ロジクール K835OWR 有線 メカニカルキーボード 赤軸 リニア テンキーレス コンパクト メカニカル キーボード 有線 有線キーボード オフホワイト windows surface K835 国内正規品 2年間メーカー保証,7475
【日本語配列】e元素メカニカル式ゲーミングキーボード 赤軸・青軸を採用 フルサイズ109キー Type-C USB有線接続 全キー防衝突 RGB発光LEDバックライト付き Windows/Mac OS対応 オフィス/ゲーム用JP配列キーボード (青軸・ブラック),6399
エレコム ワイヤレスキーボード 静音 テンキー付 薄型コンパクトサイズ Windows ChromeOS macOS対応 ブラック TK-QT30DMBK,3099
ロジクール WAVE KEYS K820 疲れにくい エルゴノミックキーボード Bluetooth Logi Bolt 日本語配列 ワイヤレスキーボード ワイヤレス 無線 テンキー パームレスト Windows Mac Chrome Android グラファイト 国内正規品,10300
ロジクール KX850FT MX MECHANICAL ワイヤレス メカニカル パフォーマンス キーボード 茶軸 タクタイル テンキー 静かな打鍵感 特に静か Logi Bolt bluetooth Unifying非対応 薄型 無線 メカニカルキーボード windows mac chrome Android ワイヤレスキーボード KX850 国内正規品 グラファイト,18073
Logicool G ロジクール G ゲーミングキーボード 有線 G213r パームレスト 日本語配列 独自のMech-domeスイッチ キーボード 静音 LIGHTSYNC RGB 国内正規品 【 ファイナルファンタジーXIV 推奨周辺機器 】,7072
【Amazon.co.jp限定】RK ROYAL KLUDGE R98 Pro ゲーミングキーボード 日本語配列フルサイズ｜メカニカルキーボード 有線｜ボリュームノブ・ガスケットマウント構造・RGBバックライト搭載｜PBTキーキャップ（Cherry Profile）・ホットスワップ対応クリームリニアスイッチ｜ソフトウェアカスタマイズ可能,11900
【Amazon.co.jp限定】Keychron C3 Pro カスタムゲーミングキーボード、コンパクトテンキーレスレイアウト/JISレイアウト/RGBバックライト/有線接続メカニカルキーボード/ホットスワップ対応/ガスケットマウント/ダブルショットPBTキーキャップ/Mac Windows Linux対応 (Keychron Superスイッチ赤軸),8910
【Amazon.co.jp限定】ロジクール MX KEYS mini KX700GRd ミニマリスト ワイヤレス イルミネイテッド キーボード グラファイト 充電式 Bluetooth Logi Bolt Unifying非対応 USB-C-A 日本語配列 無線 KX700 国内正規品,16698
Amazonベーシック 有線キーボード 日本語配列 ブラック,1267
バッファロー 静音 キーボード 有線 USB Type-A フルキーボード 109キー 日本語配列 ブラック BSKBU345BK,1730
PFU キーボード HHKB Studio 日本語配列／墨（ポインティングスティック メカニカルキーボード）,44000
UGREEN ワイヤレスキーボード 【Bluetooth＆2.4G】 無線 フルキーボード テンキー付 USB-C充電式 薄型 JIS 日本語配列 最大3台マルチペアリング対応 IOS/Android/Windows/Mac OS対応,5280
Anker ウルトラスリム Bluetooth ワイヤレスキーボード iOS/Android/Mac/Windows対応/長時間稼働 ホワイト テレワーク リモート 在宅勤務,2000
Logicool G ゲーミングキーボード G512r-LN 有線 リニア 赤軸 静かなタイピング GXスイッチ 日本語配列 LIGHTSYNC RGB USB パススルー ゲーミング キーボード メカニカルキーボード G512 PC window mac Chrome ブラック 国内正規品 【 ファイナルファンタジー XIV 推奨モデル 】,11955
ロジクール Bluetooth ワイヤレスキーボード K250GR キーボード テンキー コンパクト 日本語配列 耐水 無線 ワイヤレス K250 Windows Mac Chrome グラファイト 国内正規品,2500
エレコム キーボード 有線 メンブレン 薄型 コンパクトキーボード ブラック TK-FCM107XBK,1331
REALFORCE R4 キーボード ハイブリッド テンキーレス かな有 45g 日本語配列 ブラック R4HC61,36520
エレコム USB-A キーボード ワイヤレス (レシーバー付属) メンブレン フルキーボード ホワイト TK-FDM106TXWH,1630
ロジクール ワイヤレスキーボード K275 ワイヤレス キーボード 無線 薄型 テンキー USB接続 Unifying windows 国内正規品,2800
エレコム(ELECOM) キーボード 有線 メンブレン コンパクトキーボード ブラック TK-FCM103XBK,1171
"EPOMAKER TH87 JIS 日本語配列 TKL ワイヤレスゲーミングキーボード 2.4GHz/BT5.0/有線 テンキーレス ホットスワップ対応 10000mAh 無線 メカニカルキーボード 91キーリニアスイッチ RGBバックライト ガスケット構造 PBTキーキャップ Windows mac対応 (Blue&White, Sea Salt Silent)",12499
【Amazon.co.jp限定】Logicool G ラピッドトリガー G515 RAPID TKL 薄型 ゲーミングキーボード G515-TKL-RTBKd アクチュエーションポイント 調整可能 日本語配列 押下圧 35g 有線 テンキーレス 磁気式アナログスイッチ ロープロファイル LIGHTSYNC RGB キーボード 国内正規品※Amazon.co.jp限定 壁紙ダウンロード付き,23500
【Amazon.co.jp限定】RK ROYAL KLUDGE R65 ゲーミングキーボード 有線 日本語配列 メカニカルキーボード 60%コンパクトキーボード 70キー テンキーレス ホットスワップ可能 ボリュームノブ搭載 クリームスイッチ RGBバックライト PBTキーキャップ ガスケットマウント ブラック,9500
Logicool G ゲーミングキーボード G413TKLSE 有線 テンキーレス タクタイル 確かな打鍵感 日本語配列 高耐久性 PTB キーキャップ ゲーミング キーボード メカニカルキーボード G413 PC window mac Chrome 国内正規品 【 ファイナルファンタジー XIV 推奨モデル 】,8500
ロジクール ERGO K860 エルゴノミック スプリット キーボード bluetooth Unifying Windows Mac ワイヤレスキーボード ワイヤレス 無線 パームレスト 国内正規品 グラファイト,19191
【Amazon.co.jp限定】RK ROYAL KLUDGE M87 ワイヤレスゲーミングキーボード｜日本語配列｜LCDスクリーン＆デュアルノブ搭載｜75%サイズ・ガスケットマウント構造｜2.4G/Bluetooth/USB-C接続｜7500mAhバッテリー・RGBバックライト｜ホットスワップ対応クリームスイッチ｜レッド,13900
エレコム ワイヤレスキーボード Bluetooth フルキーボード テンキー付 薄型 メンブレン 抗菌 最大3台マルチペアリング対応 iPad/Surface/テンキー付 ブラック TK-FBM120KBK/EC,2399
