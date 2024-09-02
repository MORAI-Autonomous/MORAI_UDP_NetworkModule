from lib.network.UDP import Sender
from lib.define.TurnSignalLampControl import TurnSignalLampControl

IP = '127.0.0.1' 
PORT = 9097

#Protocol 정보 
#https://help-morai-sim.scrollhelp.site/ko/morai-sim-drive/24.R2/ros-1#id-(24.R2-ko)통신메시지프로토콜-TurnSignalLampControl.1
#Turn Signal의 경우 Simulator Graphics 옵션을 Medium 이상선택해야 표시됩니다.
def main():
    turnsignalcontrol = Sender(IP, PORT)

    data = TurnSignalLampControl()
    data.turnsignal = 0  #  0 : No  1 : Left   2 : Right
    data.emergencySignal = 0 #  0 : No  1 : Signal
    turnsignalcontrol.send(data)


if __name__ == '__main__':
    main()