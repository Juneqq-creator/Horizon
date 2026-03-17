import os
import requests
import glob

def send_feishu():
    webhook_url = os.getenv("FEISHU_WEBHOOK")
    print(f"检查 Webhook 是否加载: {webhook_url[:15] if webhook_url else '空'}...")
    # ... 其余代码
    webhook_url = os.getenv("FEISHU_WEBHOOK")
    if not webhook_url:
        print("❌ 错误: 未配置 FEISHU_WEBHOOK")
        return

    # 寻找 data/summaries 目录下最新的 .md 文件
    list_of_files = glob.glob('data/summaries/*.md')
    if not list_of_files:
        print("❌ 错误: 没有找到生成的日报文件")
        return
    
    latest_file = max(list_of_files, key=os.path.getctime)
    print(f"正在读取文件: {latest_file}")
    
    with open(latest_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 构造飞书消息体
    payload = {
        "msg_type": "markdown",
        "content": {
            "text": f"🚀 **AI 科技情报日报**\n\n{content[:4000]}" # 飞书单条消息有字数限制
        }
    }
    
    res = requests.post(webhook_url, json=payload)
    print(f"飞书返回结果: {res.text}")

if __name__ == "__main__":
    send_feishu()
