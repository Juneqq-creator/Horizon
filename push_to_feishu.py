import os
import requests
import glob
from datetime import datetime

def send_feishu():
    webhook_url = os.getenv("FEISHU_WEBHOOK")
    # 查找最新的日报文件
    list_of_files = glob.glob('data/summaries/*.md')
    if not list_of_files:
        print("No summary file found.")
        return
    latest_file = max(list_of_files, key=os.path.getctime)
    
    with open(latest_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 简单处理 Markdown 以适应飞书（飞书不支持复杂的 HTML 或部分 MD 语法）
    today = datetime.now().strftime('%Y-%m-%d')
    
    payload = {
        "msg_type": "markdown",
        "content": {
            "text": f"🚀 **AI 科技情报日报 ({today})**\n\n{content[:4000]}"
        }
    }
    
    response = requests.post(webhook_url, json=payload)
    print(f"Feishu Response: {response.text}")

if __name__ == "__main__":
    send_feishu()
