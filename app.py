import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- PHẦN XỬ LÝ DỮ LIỆU ---
data = {
    'Họ tên': ['An', 'Bình', 'Cường', 'Dũng', 'Giang', 'Hải', 'Khanh', 'Linh', 'Minh', 'Nam'],
    'Chuyên cần': [9, 8, 7, 10, 6, 8, 9, 5, 10, 7],
    'Giữa kỳ': [8, 7, 6, 9, 5, 8, 7, 6, 9, 8],
    'Cuối kỳ': [8.5, 8, 5, 9.5, 6, 9, 7.5, 4, 9, 7.5]
}
df = pd.DataFrame(data)
df['Tổng kết'] = (df['Chuyên cần'] * 0.2) + (df['Giữa kỳ'] * 0.3) + (df['Cuối kỳ'] * 0.5)

def xep_loai(diem):
    if diem >= 8.5: return 'Giỏi'
    elif diem >= 7.0: return 'Khá'
    elif diem >= 5.0: return 'Trung bình'
    else: return 'Yếu'
    
df['Xếp loại'] = df['Tổng kết'].apply(xep_loai)

diem_tb = df['Tổng kết'].mean()
sv_cao_nhat = df.loc[df['Tổng kết'].idxmax(), 'Họ tên']
sv_thap_nhat = df.loc[df['Tổng kết'].idxmin(), 'Họ tên']
so_sv_dat = len(df[df['Tổng kết'] >= 5])

# --- PHẦN GIAO DIỆN WEB ---
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.write("### 1. Bảng điểm lớp")
st.dataframe(df)

st.write("### 2. Thống kê")
st.write("- **Điểm trung bình của lớp:**", round(diem_tb, 2))
st.write("- **Sinh viên điểm cao nhất:**", sv_cao_nhat)
st.write("- **Sinh viên điểm thấp nhất:**", sv_thap_nhat)
st.write("- **Số lượng sinh viên đạt:**", so_sv_dat)

st.write("### 3. Tra cứu điểm")
ten_duoc_chon = st.selectbox("Chọn tên sinh viên:", df['Họ tên'])
bang_tra_cuu = df[df['Họ tên'] == ten_duoc_chon]
st.dataframe(bang_tra_cuu)

st.write("### 4. Biểu đồ")
fig, ax = plt.subplots()
ax.bar(df['Họ tên'], df['Tổng kết'])
st.pyplot(fig)

st.write("---")
st.write("Người tạo: Lê Đình Nghiêm - MSSV: [038208032415]")
