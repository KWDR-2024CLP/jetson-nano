import cv2  # OpenCV 라이브러리 import

# 웹캠 초기화 함수
def initialize_camera(camera_index=0):
    """
    OpenCV를 사용하여 웹캠을 초기화하고 연결 여부를 확인하는 함수.
    
    Parameters:
        camera_index (int): 사용할 카메라의 인덱스. 기본값은 0이며, 첫 번째 카메라를 사용.

    Returns:
        cap (cv2.VideoCapture): 초기화된 OpenCV 웹캠 객체.
    """
    # 지정된 인덱스의 카메라를 엽니다.
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():  # 웹캠이 성공적으로 열리지 않은 경우
        print("웹캠을 열 수 없습니다. 카메라 연결을 확인하세요.")  # 오류 메시지 출력
        exit()  # 프로그램 종료
    print("웹캠이 성공적으로 열렸습니다.")  # 성공 메시지 출력
    return cap  # 초기화된 카메라 객체 반환

# 메인 함수
def main():
    """
    웹캠을 초기화하고, 실시간으로 캡처된 영상을 화면에 표시하는 메인 함수.
    
    실행 흐름:
        1. 웹캠 초기화.
        2. 실시간으로 캡처된 프레임을 화면에 표시.
        3. 'q' 키를 누르면 프로그램 종료.
    """
    # 웹캠 초기화 및 연결 확인
    cap = initialize_camera()

    try:
        # 실시간 프레임 읽기 및 화면에 표시
        while True:
            # 웹캠에서 프레임 캡처
            ret, frame = cap.read()  # ret: 성공 여부, frame: 캡처된 이미지 프레임
            if not ret:  # 프레임을 읽지 못한 경우
                print("프레임을 읽을 수 없습니다.")  # 오류 메시지 출력
                break  # 루프 종료

            # 캡처된 프레임을 화면에 표시
            cv2.imshow("Webcam Feed", frame)  # "Webcam Feed" 창에 프레임 출력

            # 사용자가 'q' 키를 누르면 프로그램 종료
            if cv2.waitKey(1) & 0xFF == ord('q'):  # 1ms 대기 후 키 입력 체크
                print("프로그램을 종료합니다.")  # 종료 메시지 출력
                break  # 루프 종료
    finally:
        # 리소스 해제
        cap.release()  # 웹캠 연결 해제
        cv2.destroyAllWindows()  # 모든 OpenCV 창 닫기

# 프로그램의 시작점
if __name__ == "__main__":
    # 메인 함수 실행
    main()
