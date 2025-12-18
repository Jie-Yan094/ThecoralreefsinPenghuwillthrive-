import solara

# 1. 建立一個「響應式」變數
name = solara.reactive("Guest")

@solara.component
def Page():
    
    # 標題區塊
    with solara.Column(align="center"):
        solara.Markdown("""
        ## 澎湖珊瑚礁與相關生態網站
        """)

    # 簡介區塊
    solara.Markdown("## 簡介")
    solara.Markdown("澎湖島在台灣本專案運用 Google Earth Engine 的開放資料，分類與分析 2015 年至 2025 年間的衛星影像，試圖從數據中拼湊出珊瑚礁棲地的消長。是一份關於時間、海洋與變化的故事，希望能透過視覺化的數據，讓我們看見海洋的呼吸，並共同思考永續共存的未來。")

    # 圖片區塊標題
    solara.Markdown("## 好餓海星")
    
    # 使用 solara.Row 建立並排佈局
    # gap="16px": 圖片之間的間距
    # wrap=True: 螢幕變窄時自動換行 (這比寫 style={"flex-wrap": "wrap"} 更簡潔)
    with solara.Row(gap="16px", justify="center", style={"flex-wrap": "wrap"}):
        
        # --- 圖片容器開始 ---
        with solara.Div(style={
            "flex": "1 1 400px",                # 響應式關鍵：基本寬度 400px，可縮放
            "max-width": "600px",               # 限制最大寬度，避免在大螢幕太巨大
            "border-radius": "12px",            # 圓角
            "box-shadow": "0 4px 12px rgba(0,0,0,0.15)", # 陰影讓圖片浮起來
            "overflow": "hidden",               # 確保圖片圓角不被切掉
            "margin-bottom": "20px"             # 下方留白
        }):
            # ✅ 關鍵修改：
            # 1. 路徑直接寫 "/您的檔名.jpg" (對應 public 資料夾內的檔案)
            # 2. 這裡假設您的檔名是 pic_01.jpg，如果是 cots.jpg 請修改這裡
            solara.Image(
                "/pic_01.jpg", 
                width="100%"
            )
        # --- 圖片容器結束 ---