# rs485

Чтение в режиме команд<br>
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

<strong>Быстрое чтение</strong><br>
en = Counter('/dev/ttyU0');<br>
print en.get()<br>
<hr>
STAT_(03000002)<br>
RECPW(95E641EE)<br>
DATE_(06.13.05.17)<br>
TIME_(00:08:14)<br>
WATCH(00:08:14,06.13.05.17,0)<br>
DELTA(23)<br>
TTOFF(5)<br>
TRANS(0)<br>
HOURS(770)<br>
VINFO(v01.0401;Jul 20 2015)<br>
SCSD_(1,1,1034,1,1,1)<br>
ASMBL(D2F8S3P0N0)<br>
MODEL(0)<br>
SNUMB(010748104609396)<br>
VOLTA(232.57)<br>
CURRE(1.015)<br>
POWEP(0.208894)<br>
COS_f(0.884)<br>
FREQU(50.01)<br>
HVOLT(253)<br>
LVOLT(198)<br>
V_RAT(16647)<br>
I_RAT(19198)<br>
GCOR1(16072)<br>
POFF1(7600)<br>
PCOR1(9)<br>
MPCHS(0212)<br>
!
t<br>ET0PE(878.44)<br>
(634.41)<br>
(244.03)<br>
(0.00)<br>
(0.00)<br>
(0.00)<br>
STAT_(03000002)<br>
DATE_(06.13.05.17)<br>
TIME_(00:08:16)<br>
SNUMB(010748104609396)<br>
IDPAS(104609396)<br>
POWEP(0.209814)<br>
GRF01(07:00:01)<br>
(23:00:02)<br>
(00:00:00)<br>
(00:00:00)<br>
(00:00:00)<br>
(00:00:00)<br>
(00:00:00)<br>
(00:00:00)<br>
(00:00:00)<br>
(00:00:00)<br>
(00:00:00)<br>
(00:00:00)<br>
!
P
