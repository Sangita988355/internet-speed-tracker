import speedtest
import requests
import pandas as pd
from datetime import datetime

# Function to get speed test results
def get_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download = round(st.download() / (10**6), 2)  # Convert to Mbps
    upload = round(st.upload() / (10**6), 2)      # Convert to Mbps
    ping = round(st.results.ping, 2)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = get_public_ip()

    # Save results to CSV
    data = {
        "Download (Mbps)": [download],
        "Upload (Mbps)": [upload],
        "Ping (ms)": [ping],
        "IP Address": [ip],
        "Timestamp": [timestamp]
    }

    df = pd.DataFrame(data)

    try:
        df_existing = pd.read_csv("speed_log.csv")
        df = pd.concat([df_existing, df], ignore_index=True)
    except FileNotFoundError:
        pass

    df.to_csv("speed_log.csv", index=False)

    return download, upload, ping, timestamp

# Function to get public IP address
def get_public_ip():
    try:
        ip = requests.get("https://api64.ipify.org").text
        return ip
    except:
        return "Unavailable"
