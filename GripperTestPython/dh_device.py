# import serial
# serialPort = serial.Serial()
#
# class dh_device(object) :
#
#     def connect_device(self,portname, Baudrate) :
#         ret = -1
#         #print('portname: ', portname)
#         serialPort.port = portname
#         serialPort.baudrate = Baudrate
#         serialPort.bytesize = 8
#         serialPort.parity = 'N'
#         serialPort.stopbits = 1
#         serialPort.set_output_flow_control = 'N'
#         serialPort.set_input_flow_control = 'N'
#
#         serialPort.open()
#         if(serialPort.isOpen()) :
#             print('Serial Open Success')
#             ret = 0
#         else :
#             print('Serial Open Error')
#             ret = -1
#         return ret
import serial

class dh_device(object):
    def __init__(self):
        self.serialPort = serial.Serial()

    def connect_device(self, portname, baudrate):
        ret = -1
        try:
            self.serialPort.port = portname
            self.serialPort.baudrate = baudrate
            self.serialPort.bytesize = serial.EIGHTBITS
            self.serialPort.parity = serial.PARITY_NONE
            self.serialPort.stopbits = serial.STOPBITS_ONE
            self.serialPort.xonxoff = False
            self.serialPort.rtscts = False
            self.serialPort.dsrdtr = False

            self.serialPort.open()
            if self.serialPort.is_open:
                print('Serial Open Success')
                ret = 0
            else:
                print('Serial Open Error')
                ret = -1
        except Exception as e:
            print(f'Serial Open Error: {e}')
            ret = -1
        return ret

    def disconnect_device(self) :
        if(self.serialPort.isOpen()) :
            self.serialPort.close()
        else :
            return

    def device_wrire(self, write_data) :
        write_lenght = 0
        if(self.serialPort.isOpen()) :
            write_lenght = self.serialPort.write(write_data)
            if(write_lenght == len(write_data)) :
                return write_lenght
            else :
                print('write error ! send_buff :',write_data)
                return 0;
        else :
            return -1

    def device_read(self, wlen) :
        responseData = [0,0,0,0,0,0,0,0]
        if(self.serialPort.isOpen()) :
            responseData = self.serialPort.readline(wlen)
            #print('read_buff: ',responseData.hex())
            return responseData
        else :
            return -1
        

    """description of class"""


