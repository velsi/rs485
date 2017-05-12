# rs485

en = Counter('/dev/ttyU0');<br>
en.mode('w')<br>
print "T1, T2 = " + str(en.cmd('ET0PE(2,2)'));<br>
print "Напряжение = " + str(en.cmd('VOLTA()'));<br>
print "Ток = " + str(en.cmd('CURRE()'));<br>
print "Мощность = " + str(en.cmd('POWEP()'));<br>
<hr>
T1, T2 = ['634.41', '243.94']<br>
Напряжение = ['229.72']<br>
Ток = ['1.451']<br>
Мощность = ['0.333696']<br>

