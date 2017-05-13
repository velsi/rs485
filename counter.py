#!/usr/bin/python
# coding: utf-8
#
#   Считывание показаний счетчика Энергомера CE102M-R5 по  ГОСТ Р МЭК 61107-2001, режим С
#
#   В связи с тем, что драйвер CH340/341 не поддерживает 7-1-чет, работа идёт в
# режиме 8-1-нет. Бит четности формируется внутри восьми бит данных программным
# способом.
#
# velsi@list.ru

import sys, io, serial,time
from pprint import pprint
import re

class Counter:
    #Init string for Energomera's counter
    _CMD_INIT = [0x2F, 0x3F, 0x21];
    _CMD_WRITE_MODE = [0x06, 0x30, 0x35, 0x31]
    _CMD_GET_REAL_SERIAL_NUMBER = [0x01, 0x52, 0x31, 0x02, 0x53, 0x4E, 0x55, 0x4D, 0x42, 0x28, 0x29, 0x03, 0x5E]
    _CMD_GET_ETOPE = [0x06,0x30,0x35,0x36,0x0D,0x0A]
    _CMD_GET_ETOPE1 = [0x00,0x0E,0xEC,0xBC,0x63,0xD7,0xF4]
    _CMD_GET_VOLTA = [0x01, 0x52, 0x31, 0x02, 0x56, 0x4F, 0x4C, 0x54, 0x41, 0x28, 0x29]
    _CMD_GET_CURRE = [0x01, 0x52, 0x31, 0x02, 0x43, 0x55, 0x52, 0x52, 0x45, 0x28, 0x29]
    _CMD_GET_POWEP = [0x01, 0x52, 0x31, 0x02, 0x50, 0x4F, 0x57, 0x45, 0x50, 0x28, 0x29]

    #End of line \r\n
    _EOL = [0x0D, 0x0A];

    # Brand of counter
    brand = ''

    # Boudrate
    _BOUD = [300, 600, 1200, 2400, 4800, 9600]

    # Boud index of connection
    Z = 5

    # Serial port
    port = '';

    # Serial port status
    port_status = False;

    # Debug flag
    debug = False;

    # Init flag
    _init = '';

    def __init__(self, port, debug = False, boud = 9600):
        self.port = port;
        self.debug = debug;
        # 8-n => 7-1
        self.ser = serial.Serial(self.port, boud, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout = 0.1);
        self.port_status = self.ser.is_open;
        # Needed for parity
        self.parity_lookup = [self.parallel_swar(i) for i in range(256)]
        self.init();

    # Needed for parity
    def parallel_swar(self, i):
        i = i - ((i >> 1) & 0x55555555)
        i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
        i = (((i + (i >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24
        return int(i % 2)

    # Count parity
    def parity(self, v):
        v = int(v)
        v ^= v >> 16
        v ^= v >> 8
        return str(self.parity_lookup[v & 0xff])

    # Add parity bit to 7-bit data
    def encode (self, data):
        return int(self.parity(data) + bin(int(data))[2:].zfill(7), 2)

    # Remove patity bit
    def decode(self, ch):
        bit = bin(ord(ch))[2:].zfill(8)[1:]
        return chr(int(bit, 2))

    # Read data from serial port
    def read_answer(self):
        out = ''
        while self.ser.inWaiting() > 0:
            ch = self.ser.read(1)
            out += self.decode(ch)
        return out

    # Write-mode cmd
    def getCmdWriteMode(self):
        return [0x06, 0x30, ord(str(self.Z)), 0x31] + self._EOL # ACK 0 Z 1 CR LF

    # Read-mode cmd
    def getCmdReadMode(self):
        return [0x06, 0x30, ord(str(self.Z)), 0x30] + self._EOL # ACK 0 Z 0 CR LF

    # Quick-mode cmd (Energomera only ??)
    def getCmdQuickReadMode(self):
        return [0x06, 0x30, ord(str(self.Z)), 0x36] + self._EOL # ACK 0 Z 6 CR LF

    # Init connection
    def init(self):
        init = self.read(self._CMD_INIT + self._EOL);
        if (init):
            self._init = True;
            self.brand = init[1:4];
            self.Z = int(init[4]);

            # reinit serial port
            if (self.ser.baudrate != self._BOUD[self.Z]):
                self.__init__( self.port, self._BOUD[self.Z]);
        else:
            self._init = False;

    # Get value of some counters
    def get(self):
        res1 = self.read(self.getCmdReadMode()); # init read mode
        self.init();

        res2 = self.read(self.getCmdQuickReadMode()); # quick read
        return res1 + res2;

    # Reading form serial port
    def read(self, cmd):
        if (not self._init and self._init != ''):
            self.init();
        if self.port_status:
            values = [];
            _cmd = '';
            for bit in (cmd):
                values.append(self.encode(bit))
                _cmd += chr(int(bit))
#             pprint(values)
            if (self.debug):
                print ">> \r\n"+_cmd

            self.ser.write(values)
            time.sleep(1)
            answer = self.read_answer()
            if (self.debug):
                print "<< " + answer
            return answer;

    # Command mode
    def cmd(self, cmd):
        _cmd = [0x01, 0x52, 0x31, 0x02] # SOH R 1 STH
        for ch in (cmd):
            _cmd.append(ord(ch));
        _cmd += self._EOL
        answer = self.read(_cmd)
        res = self.getValue(answer)
#         pprint(res);
        return res

    # Parse value from answer (xx.xx)
    def getValue(self, answer):
        value = map(float, re.findall('(\d+.\d+)',answer));
        if len(value) == 1:
            value = value[0];
        return value

    # Switch mode
    def mode(self, mode):
        if (mode == 'w'):
            confirm = self.read(self.getCmdWriteMode());

en = Counter('/dev/ttyU0');
# print en.get()
en.mode('w')
print 'T1 = {0[0]} Квт/ч\r\nT2 = {0[1]} Квт/ч'.format(en.cmd('ET0PE(2,2)'));
print "Напряжение = {:.2f} В".format(en.cmd('VOLTA()'));
print "Ток = {:.2f} A".format(en.cmd('CURRE()'));
print "Мощность = {:.2f} КВт".format(en.cmd('POWEP()') * 1000);
