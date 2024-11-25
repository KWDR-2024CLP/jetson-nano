# jetson-nano-test
잭슨 나노 안에 코드 저장소입니다.

## 주요 개발 내용
1. **웹캠 초기화 및 테스트**
   - OpenCV를 사용하여 Jetson Nano에 연결된 웹캠 피드를 캡처하고 출력합니다.

2. **객체 탐지 통합 (테스트 중)**
   - YOLOv5와 같은 사전 학습된 객체 인식 모델을 활용하여 웹캠 화면에서 객체를 탐지합니다.




## 프로젝트 파일 구조
```plaintext
jetson-nano-test/
│
├── README.md               # 프로젝트 설명 문서
├── requirements.txt        # 프로젝트에서 사용하는 Python 라이브러리 목록
├── .gitignore              # Git에서 제외할 파일/폴더 목록
├── src/                    # 소스 코드 디렉토리
│   ├── main.py             # 메인 실행 파일 (학습 모델과 OpenCV 통합 코드)
│   ├── camera_test.py      # 웹캠 초기화 및 테스트 코드
│   ├── yolo_integration.py # csi 카메라 테스트 코드






