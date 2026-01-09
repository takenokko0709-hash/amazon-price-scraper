import requests
from bs4 import BeautifulSoup
import csv
import time

def search_amazon(keyword):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Accept-Language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    
    search_url = f"https://www.amazon.co.jp/s?k={keyword}"
    
    try:
        response = requests.get(search_url, headers=headers)
        if response.status_code != 200:
            print(f"アクセスに失敗しました（エラーコード: {response.status_code}）")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        products = []
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
        print(f"エラー: {e}")
        return []

# --- 実行部分 ---
print("================================")
print("   Amazon価格調査ツール")
print("================================")

# 入力機能を追加！
keyword = input("何を探しますか？（例：マウス、本など）: ")

if not keyword:
    print("キーワードが入力されませんでした。終了します。")
else:
    print(f"\n「{keyword}」を検索中...少々お待ちください...")
    result_data = search_amazon(keyword)

    if result_data:
        # ファイル名もキーワードを含めるようにすると親切
        filename = f"amazon_{keyword}.csv"
        with open(filename, "w", encoding="utf_8_sig", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["商品名", "価格(円)"])
            writer.writerows(result_data)
        
        print("-" * 30)
        print(f"完了！ '{filename}' に保存しました。")
        print("-" * 30)
    else:
        print("データが見つからなかったか、ブロックされました。")
