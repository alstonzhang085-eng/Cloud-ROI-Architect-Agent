import json
import datetime
import random

def fetch_cloud_prices():
    """
    模拟爬取三大云厂商特定规格(如 8vCPU, 16GB RAM)的单价
    在生产环境中，这里会调用 Boto3 (AWS), Azure SDK 或 GCP API
    """
    print("正在启动全球云产品单价爬虫...")
    
    # 模拟最新单价数据（实际应用中这里是 API 调用结果）
    # 价格单位：USD/Hour
    latest_data = {
        "metadata": {
            "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "source": "Multi-Cloud Price Crawler v1.0",
            "status": "Success"
        },
        "prices": {
            "AWS": {
                "region": "us-east-1",
                "instance_type": "m5.2xlarge",
                "on_demand": 0.384,
                "spot_average": round(0.115 * (1 + random.uniform(-0.05, 0.05)), 4), # 模拟竞价实例波动
                "currency": "USD"
            },
            "Azure": {
                "region": "East US",
                "instance_type": "D8s_v3",
                "on_demand": 0.380,
                "spot_average": round(0.108 * (1 + random.uniform(-0.05, 0.05)), 4),
                "currency": "USD"
            },
            "GCP": {
                "region": "us-east1",
                "instance_type": "e2-standard-8",
                "on_demand": 0.268,
                "preemptible": round(0.080 * (1 + random.uniform(-0.05, 0.05)), 4),
                "currency": "USD"
            }
        },
        "audit_alert": {
            "threshold_exceeded": False,
            "message": "Price fluctuations are within normal range (±5%)."
        }
    }
    
    return latest_data

def save_to_json(data, filepath="data/latest_prices.json"):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"✅ 成功！最新价格已存入: {filepath}")
    except FileNotFoundError:
        print(f"❌ 失败：找不到目录。请先确保存在 'data' 文件夹。")

if __name__ == "__main__":
    prices = fetch_cloud_prices()
    save_to_json(prices)