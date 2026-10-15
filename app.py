from datetime import datetime
from io import BytesIO
import pandas as pd
import streamlit as st

# 設定網頁標題與寬版面
st.set_page_config(
    page_title="醫療物資請領登記系統", page_icon="📋", layout="wide"
)

st.title("📋 醫療物資請領清單登記系統")
st.write(
    "請在下方各分頁中勾選您需要請領的物品，系統將自動在下方產生完整清單。"
)

# ==================== 分頁 1 資料 ====================
items_data_page1 = [
    ("庫存品", "M6CEE010038", "愛喜優克萊福藥物準備系統組件-輸液管轉接頭"),
    ("庫存品", "M6CEE010049", "普惠靜注延長管-T型"),
    ("庫存品", "M6NAN010075", "注射針/Sterican 18G"),
    ("庫存品", "M6W0C010003", "治療紙巾(抗汗紙卷)"),
    ("庫存品", "M6W0C020079", "外科手術口罩(醫療口罩)"),
    ("庫存品", "M6W0C020133", "舜堡外科手術用口罩-N95"),
    ("庫存品", "M6W0C030006", "紙帽/shanluen\\不織布, 圓形"),
    ("庫存品", "M6W1F010166", "中衛鞋套(未滅菌)"),
    ("庫存品", "M6W7ST10040", "無粉多倍乳膠健檢手套 L"),
    ("庫存品", "M6W7ST10041", "無粉多倍乳膠健檢手套 M"),
    ("庫存品", "M6W7ST10042", "無粉多倍乳膠健檢手套 S"),
    ("庫存品", "M6W7ST10096", "華新手術手套(無粉)(滅菌/未滅菌) 無粉, #6.0"),
    ("庫存品", "M6W7ST10097", "華新手術手套(無粉)(滅菌/未滅菌) 無粉, #6.5"),
    ("庫存品", "M6W7ST10098", "華新手術手套(無粉)(滅菌/未滅菌) 無粉, #7.0"),
    ("庫存品", "M6W7ST10099", "華新手術手套(無粉)(滅菌/未滅菌) 無粉, #7.5"),
    ("庫存品", "M6W7ST10100", "華新手術手套(無粉)(滅菌/未滅菌) 無粉, #8.0"),
    ("庫存品", "M6W7ST10101", "華新手術手套(無粉)(滅菌/未滅菌) 無粉, #8.5"),
    ("庫存品", "M6W9A010009", "滅菌防塵墊(地板藍色)"),
    ("庫存品", "M6W9A010074", "保盾拋棄式醫用衣物-隔離衣(潑灑箱用)"),
    ("庫存品", "M6W9A050024", "護目鏡-輕便型"),
    ("庫存品", "M6W9A070045", "基因毒性廢棄物收集桶(22公升)"),
    ("庫存品", "M6WDD010009", "大紗布，10片/包"),
    ("庫存品", "M6WDD010041", "酒精棉片"),
    ("庫存品", "M6W9A010007", "Surgical Gown 保盾一次性使用手術衣(抽藥外衣)"),
    ("單一品項", "M600RB00034", "Parafilm M"),
    ("單一品項", "M6E01001532", "凱普森液體轉換管組KAPSAM FLUID TRANSFER TUBE SET"),
    ("單一品項", "M6NAN010089", "SOL-CARE safety needle(25G皮下針頭)"),
    ("單一品項", "M6NBS010010", "塑膠注射筒Syringe 3cc"),
    ("單一品項", "M6NBS010011", "塑膠注射筒Syringe 5cc"),
    ("單一品項", "M6NBS010012", "塑膠注射筒Syringe 10cc"),
    ("單一品項", "M6NBS010014", "塑膠注射筒Syringe 30cc"),
    ("單一品項", "M6NBS010043", "康德萊一次性使用無菌注射器-螺旋式空針 50 cc"),
    ("單一品項", "M6NCS010030", "塑膠注射筒Syringe 1cc"),
    ("單一品項", "M6W7ST10061", "康德樂無粉手術用手套(滅菌)-化療用 #6"),
    ("單一品項", "M6W7ST10062", "康德樂無粉手術用手套(滅菌)-化療用 #6.5"),
    ("單一品項", "M6W7ST10063", "康德樂無粉手術用手套(滅菌)-化療用 #7"),
    ("單一品項", "M6W7ST10064", "康德樂無粉手術用手套(滅菌)-化療用 #7.5"),
    ("單一品項", "M6W7ST10065", "康德樂無粉手術用手套(滅菌)-化療用 #8"),
    ("單一品項", "M6W7ST10072", "康德樂無粉手術用手套(滅菌)-化療用 #8.5"),
    ("單一品項", "M6CLPA20003", "LV10,1Day Infusor,10ml/h奶瓶"),
    ("單一品項", "M6CLPA20004", "LV5,2Day Infusor,5ml/h奶瓶"),
]

# ==================== 分頁 2 資料 ====================
items_data_page2 = [
    (
        "調撥領用西藥",
        "庫存品",
        "CSTER03",
        "Disterile Water(支) 20ml/amp(Water for inj)",
    ),
    (
        "調撥領用西藥",
        "庫存品",
        "CDIST01",
        "Disterile Water(支) 20ml/amp(Water for inj)",
    ),
    (
        "調撥領用西藥",
        "庫存品",
        "CNS01",
        "0.9% Saline(支) 20ml/amp(Sodium Chloride)",
    ),
    (
        "調撥領用西藥",
        "庫存品",
        "CSALI08",
        "Sodium Chloride (小) 0.9%,100ml/軟袋(Saline Injection)",
    ),
    (
        "調撥領用西藥",
        "庫存品",
        "CSALI05",
        "0.9% Saline(小) 250ml/bag(Sodium Chloride),軟袋",
    ),
    (
        "調撥領用西藥",
        "庫存品",
        "CSALI02",
        "0.9% Sodium Chloride(中) 500ml/軟袋",
    ),
    (
        "調撥領用西藥",
        "庫存品",
        "CSALI10",
        "0.9% Sodium Chloride (大) 1000mL/軟袋",
    ),
    (
        "調撥領用西藥",
        "庫存品",
        "CGITO01",
        "5% Dextrose(小) 250ml/bag(Gitose)",
    ),
    (
        "調撥領用西藥",
        "庫存品",
        "CGITO04",
        "5% Dextrose(大) 500ml/bag(Gitose)",
    ),
    ("調撥領用西藥", "庫存品", "WKESP02", "克司博75%酒精液4000ml/瓶"),
    (
        "調撥領用西藥",
        "庫存品",
        "WANTIG03",
        "Antigerm抑平菌殺菌液(紅色洗手液)",
    ),
    (
        "調撥領用西藥",
        "庫存品",
        "CHAFO01",
        "Haforman Injection 500ml/bag(L-Ringer)",
    ),
]

# ==================== 分頁 3 資料 ====================
items_data_page3 = [
    (
        "一般品項",
        "一般品",
        "VA100001161",
        "影印紙 A5/1箱10包(請領單位為包)",
    ),
    ("一般品項", "一般品", "VB071200002", "10號夾鍊袋"),
    ("一般品項", "一般品", "VB071200005", "7號夾鍊袋"),
    ("一般品項", "一般品", "VB225401002", "珍珠洗手液"),
    ("一般品項", "一般品", "VB401304016", "細胞毒性藥物避光袋"),
    ("一般品項", "一般品", "VE9R22A0552", "化療藥品標籤貼紙(白底11.8*17.6cm)"),
]

# ==================== 分頁 4 資料 ====================
items_data_page4 = [
    (
        "盤點撥補ZZ",
        "醫材庫存品",
        "VB401304111",
        "感染性垃圾袋-紅、特大(86*87，25個/折=1.14KG)",
    ),
    (
        "盤點撥補ZZ",
        "醫材庫存品",
        "VB401304113",
        "感染性垃圾袋-紅、特小(40*49，50個/折=0.424KG)",
    ),
    ("盤點撥補ZZ", "醫材庫存品", "VE9A29A1155", "基因毒性廢棄物標示貼紙(小)"),
]

# 建立 4 個分頁
tab1, tab2, tab3, tab4 = st.tabs(
    ["盤點撥補醫材", "調撥領用西藥 (出庫請點441 請領點541)", "一般品項", "盤點撥補ZZ"]
)


# --- 共用匯出 Excel 函式 ---
def get_excel_download_button(df, filename_prefix):
  output = BytesIO()
  with pd.ExcelWriter(output, engine="openpyxl") as writer:
    df.to_excel(writer, index=False, header=False, sheet_name="請領清單")
  excel_data = output.getvalue()
  return st.download_button(
      label="📥 下載此清單 Excel 檔",
      data=excel_data,
      file_name=f"請領清單_{filename_prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
      mime=(
          "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
      ),
  )


# --- 分頁 1 介面 ---
with tab1:
  st.subheader("📦 盤點撥補醫材 - 勾選區")
  selected_records_p1 = []
  cols = st.columns(2)
  for i, (source, code, name) in enumerate(items_data_page1):
    with cols[i % 2]:
      if st.checkbox(f"{name} ({source})", key=f"p1_item_{i}"):
        selected_records_p1.append(("盤點撥補醫材", source, code, name))

  st.markdown("---")
  st.subheader("📋 盤點撥補醫材產生的清單")
  if selected_records_p1:
    df_p1 = pd.DataFrame(selected_records_p1)
    st.dataframe(df_p1, use_container_width=True, hide_index=True)
    get_excel_download_button(df_p1, "盤點撥補醫材")
  else:
    st.info("👆 請在上方勾選項目。")

# --- 分頁 2 介面 ---
with tab2:
  st.subheader("💊 調撥領用西藥 (出庫請點441 請領點541) - 勾選區")
  selected_records_p2 = []
  cols = st.columns(2)
  for i, (col1_val, col2_val, code, name) in enumerate(items_data_page2):
    with cols[i % 2]:
      if st.checkbox(name, key=f"p2_item_{i}"):
        selected_records_p2.append((col1_val, col2_val, code, name))

  st.markdown("---")
  st.subheader("📋 調撥領用西藥產生的清單")
  if selected_records_p2:
    df_p2 = pd.DataFrame(selected_records_p2)
    st.dataframe(df_p2, use_container_width=True, hide_index=True)
    get_excel_download_button(df_p2, "調撥領用西藥")
  else:
    st.info("👆 請在上方勾選項目。")

# --- 分頁 3 介面 ---
with tab3:
  st.subheader("📄 一般品項 - 勾選區")
  selected_records_p3 = []
  cols = st.columns(2)
  for i, (col1_val, col2_val, code, name) in enumerate(items_data_page3):
    with cols[i % 2]:
      if st.checkbox(f"{name} ({code})", key=f"p3_item_{i}"):
        selected_records_p3.append((col1_val, col2_val, code, name))

  st.markdown("---")
  st.subheader("📋 一般品項產生的清單")
  if selected_records_p3:
    df_p3 = pd.DataFrame(selected_records_p3)
    st.dataframe(df_p3, use_container_width=True, hide_index=True)
    get_excel_download_button(df_p3, "一般品項")
  else:
    st.info("👆 請在上方勾選項目。")

# --- 分頁 4 介面 ---
with tab4:
  st.subheader("🗑️ 盤點撥補ZZ - 勾選區")
  selected_records_p4 = []
  cols = st.columns(2)
  for i, (col1_val, col2_val, code, name) in enumerate(items_data_page4):
    with cols[i % 2]:
      if st.checkbox(f"{name} ({code})", key=f"p4_item_{i}"):
        selected_records_p4.append((col1_val, col2_val, code, name))

  st.markdown("---")
  st.subheader("📋 盤點撥補ZZ產生的清單")
  if selected_records_p4:
    df_p4 = pd.DataFrame(selected_records_p4)
    st.dataframe(df_p4, use_container_width=True, hide_index=True)
    get_excel_download_button(df_p4, "盤點撥補ZZ")
  else:
    st.info("👆 請在上方勾選項目。")
