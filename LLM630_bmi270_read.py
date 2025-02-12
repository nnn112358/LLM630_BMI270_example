#!/usr/bin/env python3
import time
from bmi270.BMI270 import *

# -------------------------------------------------
# INITIALIZATION
# -------------------------------------------------
try:
    BMI270_1 = BMI270(I2C_PRIM_ADDR)
    BMI270_1.load_config_file()
except Exception as e:
    print("Error: " + str(e))
    print("Could not initialize BMI270_1. Check your wiring or try again.")
    exit(1)

# -------------------------------------------------
# HARDWARE CONFIGURATION
# -------------------------------------------------
BMI270_1.set_mode(PERFORMANCE_MODE)
BMI270_1.set_acc_range(ACC_RANGE_2G)
BMI270_1.set_gyr_range(GYR_RANGE_1000)
BMI270_1.set_acc_odr(ACC_ODR_200)
BMI270_1.set_gyr_odr(GYR_ODR_200)
BMI270_1.set_acc_bwp(ACC_BWP_OSR4)
BMI270_1.set_gyr_bwp(GYR_BWP_OSR4)
BMI270_1.disable_fifo_header()
BMI270_1.enable_data_streaming()
BMI270_1.enable_acc_filter_perf()
BMI270_1.enable_gyr_noise_perf()
BMI270_1.enable_gyr_filter_perf()

# -------------------------------------------------
# CONSTANTS
# -------------------------------------------------
start_time = time.time()

# -------------------------------------------------
# HELPER FUNCTIONS
# -------------------------------------------------
def get_milliseconds():
    return int(round((time.time() - start_time) * 1000))

def get_and_display_data():
    # センサーデータの取得
    acc_data = BMI270_1.get_raw_acc_data()
    gyr_data = BMI270_1.get_raw_gyr_data()
    time.sleep(0.1)
    # データを一行に集約して表示
    print(f"\nTime: {get_milliseconds():6d}ms | Acc: X={acc_data[0]:7.3f} Y={acc_data[1]:7.3f} Z={acc_data[2]:7.3f} | Gyr: X={gyr_data[0]:8.2f} Y={gyr_data[1]:8.2f} Z={gyr_data[2]:8.2f}", end="", flush=True)

# -------------------------------------------------
# MAIN
# -------------------------------------------------
def main():
    current_time = 0.0
    old_time = 0.0
    update_rate = 0.005  # 200Hz
    sensor_running = False
    
    print("BMI270 Sensor Data Monitor")
    print("=" * 100)  # 区切り線を長くして見やすく
    print("Press Ctrl+C to exit")
    
    try:
        while True:
            current_time = time.time() - start_time
            
            try:
                get_and_display_data()
                if not sensor_running:
                    print(f"\nSampling rate: {1/update_rate:.1f} Hz")
                    sensor_running = True
            except Exception as e:
                print(f"\nError: {e}")
                print("Sensor read error. Retrying in 5 seconds...")
                sensor_running = False
                time.sleep(5)
                
            time_delta = current_time - old_time
            old_time = current_time
            
            time.sleep(max(update_rate - time_delta, 0))
            
    except KeyboardInterrupt:
        print("\nProgram terminated by user")

if __name__ == "__main__":
    main()