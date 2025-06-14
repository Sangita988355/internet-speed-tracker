import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from speed_checker import get_speed, get_public_ip

# --- Streamlit UI Configuration ---
st.set_page_config(page_title="Advanced Speed Checker", layout="centered")
st.title("🌐 Internet Speed Tracker")
st.write("Track your internet speed, ping, and IP address over time.")

# --- Run Speed Test ---
if st.button("▶️ Run Speed Test"):
    download, upload, ping, timestamp = get_speed()
    ip = get_public_ip()
    
    st.success("✅ Test Completed")
    st.markdown(f"### 📥 Download Speed\n{download} Mbps")
    st.markdown(f"### 📤 Upload Speed\n{upload} Mbps")
    st.markdown(f"### 🛰️ Ping\n{ping} ms")
    st.markdown(f"### 🌐 IP Address\n{ip}")
    st.markdown(f"### 🕒 Time\n{timestamp}")

# --- Load CSV Data ---
try:
    df = pd.read_csv("speed_log.csv")
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # --- Graph Display ---
    st.markdown("## 📊 Speed Trend Over Time")
    fig, ax = plt.subplots()
    ax.plot(df['Timestamp'], df['Download (Mbps)'], marker='o', color='green', label='Download')
    ax.plot(df['Timestamp'], df['Upload (Mbps)'], marker='x', color='blue', label='Upload')
    ax.set_xlabel("Time")
    ax.set_ylabel("Speed (Mbps)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # --- View Test History ---
    st.markdown("## 🧾 Test History")
    st.dataframe(df.tail(10), use_container_width=True)

    # --- Average Speed Stats ---
    avg_download = round(df['Download (Mbps)'].mean(), 2)
    avg_upload = round(df['Upload (Mbps)'].mean(), 2)
    avg_ping = round(df['Ping (ms)'].mean(), 2)

    st.markdown("## 📈 Average Speed Statistics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Download", f"{avg_download} Mbps")
    col2.metric("Avg Upload", f"{avg_upload} Mbps")
    col3.metric("Avg Ping", f"{avg_ping} ms")

except FileNotFoundError:
    st.warning("⚠️ No speed tests logged yet. Please run a test first.")

# --- Internet Tips ---
st.markdown("## 💡 Smart Internet Tips")
with st.expander("Show Smart Tips"):
    st.markdown("""
    - 🛜 Use wired connections for stable speeds.
    - 📶 Place your router centrally to improve signal.
    - 🚫 Avoid running multiple downloads during tests.
    - 🔄 Restart your router weekly.
    - ⚙️ Update network drivers regularly.
    """)

# --- Footer ---
st.markdown("---")
st.caption("Developed by Sangita Gorai | Advanced Internet Speed Checker © 2025")