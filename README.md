# rs485


Чтение в режиме команд
----------------------

    en = Counter('/dev/ttyU0');
    en.mode('w')
    print 'T1 = {0[0]} Квт/ч\r\nT2 = {0[1]} Квт/ч'.format(en.cmd('ET0PE(2,2)'));
    print "Напряжение = {:.2f} В".format(en.cmd('VOLTA()'));
    print "Ток = {:.2f} A".format(en.cmd('CURRE()'));
    print "Мощность = {:.2f} КВт".format(en.cmd('POWEP()') * 1000);

T1 = 636.6 Квт/ч<br>
T2 = 246.45 Квт/ч<br>
Напряжение = 231.90 В<br>
Ток = 1.24 A<br>
Мощность = 285.82 КВт<br>


Быстрое чтение
--------

        en = Counter('/dev/ttyU0');
        print en.get()

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
