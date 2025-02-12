# LLM630_BMI270_example

## bmi270 run

Using BMI270 I2C Python Library
https://github.com/CoRoLab-Berlin/bmi270_python

```
root@m5stack-kit# pip install bmi270
root@m5stack-kit# python3 LLM630_bmi270_read.py
```

## Result
```
LM630_bmi270_read.pyt/usr/250212_test/bmi270_python-main/examples# python LLM630_bmi270_read.py
---- I2C BUS FOUND ----
0x68  --> Chip ID: 0x24
0x68  --> Initialization already done
0x68  --> Initialization status: 00000001       (00000001 --> OK)
0x68  --> Mode set to: PERFORMANCE_MODE
0x68  --> ACC range set to: 2G
0x68  --> GYR range set to: 1000
0x68  --> ACC ODR set to: 200
0x68  --> GYR ODR set to: 200
0x68  --> ACC BWP set to: OSR4
0x68  --> GYR BWP set to: OSR4
0x68  --> FIFO Header disabled (ODR of all enabled sensors need to be identical)
0x68  --> Streaming Mode enabled (no data will be stored in FIFO)
0x68  --> Accelerometer filter performance enabled (performance optimized)
0x68  --> Gyroscope noise performance enabled (performance optimized)
0x68  --> Gyroscope filter performance enabled (performance optimized)
BMI270 Sensor Data Monitor
====================================================================================================
Press Ctrl+C to exit

Time:    102ms | Acc: X=-263.000 Y=-343.000 Z=-16342.000 | Gyr: X=    4.00 Y=    5.00 Z=    0.00
Sampling rate: 200.0 Hz

Time:    222ms | Acc: X=-240.000 Y=-344.000 Z=-16345.000 | Gyr: X=    2.00 Y=    9.00 Z=    1.00
Time:    332ms | Acc: X=-215.000 Y=-339.000 Z=-16372.000 | Gyr: X=    1.00 Y=    7.00 Z=    0.00
Time:    442ms | Acc: X=-240.000 Y=-318.000 Z=-16359.000 | Gyr: X=    1.00 Y=    5.00 Z=    0.00
Time:    552ms | Acc: X=-226.000 Y=-355.000 Z=-16353.000 | Gyr: X=    4.00 Y=    7.00 Z=    0.00
Time:    662ms | Acc: X=-218.000 Y=-355.000 Z=-16355.000 | Gyr: X=    2.00 Y=    5.00 Z=    0.00
Time:    772ms | Acc: X=-249.000 Y=-347.000 Z=-16358.000 | Gyr: X=    4.00 Y=    8.00 Z=    1.00
Time:    882ms | Acc: X=-245.000 Y=-358.000 Z=-16356.000 | Gyr: X=    2.00 Y=    9.00 Z=    1.00
Time:    992ms | Acc: X=-261.000 Y=-368.000 Z=-16377.000 | Gyr: X=    1.00 Y=    8.00 Z=    0.00
Time:   1102ms | Acc: X=-262.000 Y=-361.000 Z=-16375.000 | Gyr: X=    3.00 Y=    5.00 Z=    1.00
```


## I2C Investivate
I2C Grove is Red Port(No.03).
![image](https://github.com/user-attachments/assets/0b3e7e02-a303-43d3-868a-7b675222b0e7)

BMI270 belongs to sys-I2C.  
sys-I2C is i2c-1.
![image](https://github.com/user-attachments/assets/8823fcdb-4d76-4786-ba93-34f22cc86fca)


```
root@m5stack-kit# i2cdetect -y -r 0
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```
```
root@m5stack-kit# i2cdetect -y -r 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- UU -- -- -- -- -- -- -- -- --
40: -- -- -- UU -- -- -- UU -- 49 -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- 68 -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```
 * 0x36 - AW99703: LEDバックライトドライバー
 * 0x43 - PI4IOE5V6408: I/O Expander
 * 0x47 - SGM7220: USB Type-C PDコントローラ
 * 0x49 - ????
 * 0x68 - BMI270: 6軸IMUセンサー（IMU）

0x36と0x43と0x47は"UU"と表示されており、カーネルドライバによって既に使用中であることを示しています

```
root@m5stack-kit# ls /sys/bus/i2c/devices/
1-0014  1-0036  1-0043  1-0047  1-0055  1-0068  i2c-0  i2c-1

root@m5stack-kit# cat /sys/bus/i2c/devices/1-0014/name
OF_NAME=gt911
OF_FULLNAME=/soc/i2c@4851000/gt911@14
OF_COMPATIBLE_0=goodix,gt911
OF_COMPATIBLE_N=1
MODALIAS=of:Ngt911T<NULL>Cgoodix,gt911

root@m5stack-kit# cat /sys/bus/i2c/devices/1-0036/name
DRIVER=aw99703-bl
OF_NAME=aw99703-bl
OF_FULLNAME=/soc/i2c@4851000/aw99703-bl@36
OF_COMPATIBLE_0=awinic,aw99703-bl
OF_COMPATIBLE_N=1
MODALIAS=of:Naw99703-blT<NULL>Cawinic,aw99703-bl

root@m5stack-kit# cat /sys/bus/i2c/devices/1-0043/name
DRIVER=pi4ioxx-gpio
OF_NAME=pinctrl
OF_FULLNAME=/soc/i2c@4851000/pinctrl@43
OF_COMPATIBLE_0=pericom,pi4ioe5v6408
OF_COMPATIBLE_N=1
MODALIAS=of:NpinctrlT<NULL>Cpericom,pi4ioe5v6408

root@m5stack-kit# cat /sys/bus/i2c/devices/1-0047/name
DRIVER=sgm7220
OF_NAME=sgm7220
OF_FULLNAME=/soc/i2c@4851000/sgm7220@47
OF_COMPATIBLE_0=axera,sgm7220
OF_COMPATIBLE_N=1
MODALIAS=of:Nsgm7220T<NULL>Caxera,sgm7220


root@m5stack-kit# cat /sys/bus/i2c/devices/1-0055/name
OF_NAME=bq27220
OF_FULLNAME=/soc/i2c@4851000/bq27220@55
OF_COMPATIBLE_0=ti,bq27220
OF_COMPATIBLE_N=1
MODALIAS=of:Nbq27220T<NULL>Cti,bq27220


root@m5stack-kit# cat /sys/bus/i2c/devices/1-0068/name
OF_NAME=imu
OF_FULLNAME=/soc/i2c@4851000/imu@68
OF_COMPATIBLE_0=bosch,bmi270
OF_COMPATIBLE_N=1
MODALIAS=of:NimuT<NULL>Cbosch,bmi270
```


