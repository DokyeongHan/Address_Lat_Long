from PyKakao import KakaoLocal
import pandas as pd

# kakao developers에서 발급받은 REST API 키	
service_key = ""

# kakao local API 세션 정의
KL = KakaoLocal(service_key)

# 파일 불러오기
df = pd.read_excel('input.xlsx')

for i in range(len(df)):
    # 위도 경도 조회
    address = df['주소입력'][i]
    result = KL.search_address(address)
    
    # 파일쓰기
    if(result['documents'] == []):
        pass
    else:
        df['위도'][i] = result['documents'][0]['address']['y']
        df['경도'][i] = result['documents'][0]['address']['x']
        df['주소정제'][i] = result['documents'][0]['address']['address_name']
        
    
# 파일저장
df.to_excel("output.xlsx")