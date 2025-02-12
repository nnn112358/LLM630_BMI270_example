# LLM630_BMI270_example

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


```
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

 * 0x14 - GT911: Goodixのタッチスクリーンコントローラ
 * 0x36 - AW99703: LEDバックライトドライバー
 * 0x43 - PI4IOE5V6408: I/O Expander
 * 0x47 - SGM7220: USB Type-C PDコントローラ
 * 0x55 - BQ27220: バッテリー管理IC
 * 0x68 - BMI270: 6軸IMUセンサー（お探しのデバイス）





