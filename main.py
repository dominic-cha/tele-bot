import requests
import schedule
import time
import os
from datetime import datetime

# 환경변수에서 봇 정보 가져오기
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def send_hello_message():
    """텔레그램으로 Hello World 메시지 보내기"""
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"🌟 Hello World! 🌟\n현재 시간: {current_time}"
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print(f"✅ 메시지 전송 성공: {current_time}")
        else:
            print(f"❌ 전송 실패: {response.text}")
    except Exception as e:
        print(f"🚨 오류 발생: {e}")

# 매일 오전 9시(한국시간)에 실행하도록 설정
# Render는 UTC 시간을 사용하므로 한국시간 9시 = UTC 0시
schedule.every().day.at("00:00").do(send_hello_message)

# 추가 테스트: 매시간 정각에도 실행 (테스트용)
schedule.every().hour.at(":00").do(send_hello_message)

print("🤖 텔레그램 봇이 시작되었습니다!")
print(f"📱 BOT_TOKEN: {'✅ 설정됨' if BOT_TOKEN else '❌ 미설정'}")
print(f"💬 CHAT_ID: {'✅ 설정됨' if CHAT_ID else '❌ 미설정'}")

# 봇 시작 시 즉시 테스트 메시지 전송
if BOT_TOKEN and CHAT_ID:
    print("📤 시작 메시지를 전송합니다...")
    send_hello_message()
else:
    print("⚠️ 환경변수가 설정되지 않았습니다!")

# 스케줄러 실행 (무한 루프)
print("⏰ 스케줄러를 시작합니다...")
while True:
    schedule.run_pending()
    time.sleep(60)  # 1분마다 스케줄 확인
