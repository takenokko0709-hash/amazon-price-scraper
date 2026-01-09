import requests
from bs4 import BeautifulSoup
import csv
import time

def search_amazon(keyword):
    # Amazonに「人間がブラウザで見ています」と思わせるための設定
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Accept-Language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    
    # 検索URLの作成
    search_url = f"https://www.amazon.co.jp/s?k={keyword}"
    
    try:
        response = requests.get(search_url, headers=headers)
        # もしアクセスが拒否されたらエラーを表示
        if response.status_code != 200:
            print(f"アクセスに失敗しました（ステータスコード: {response.status_code}）")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        products = []

        # 商品情報が入っているブロックを探す（Amazonの仕様変更により変わる可能性があります）
        items = soup.select(".s-result-item[data-component-type='s-search-result']")

        for item in items:
            title_el = item.select_one("h2 span")
            price_el = item.select_one(".a-price-whole")

            if title_el and price_el:
                title = title_el.get_text(strip=True)
                price = price_el.get_text(strip=True).replace(",", "")
                products.append([title, price])
        
        return products

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return []

# --- 実行部分 ---
keyword = "キーボード" # 検索したい言葉
print(f"「{keyword}」を検索中...")

result_data = search_amazon(keyword)

if result_data:
    # CSVファイルに保存（Excelがなくてもメモ帳やスプレッドシートで開けます）
    filename = "amazon_results.csv"
    with open(filename, "w", encoding="utf_8_sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["商品名", "価格(円)"]) # ヘッダー
        writer.writerows(result_data)
    
    print(f"成功！ {len(result_data)}件のデータを '{filename}' に保存しました。")
else:
    print("データが取得できませんでした。Amazonの対策にブロックされた可能性があります。")