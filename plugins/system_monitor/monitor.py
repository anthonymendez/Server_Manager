import time
import sched
import psutil
import os

# TODO: Check if OS supports certain functions

# System Info Variables
# CPU 
cpu_thread_count = psutil.cpu_count(logical = True)
cpu_physical_count = psutil.cpu_count(logical = False)
cpu_percent_overall = None
cpu_percent_list = None
cpu_stats = None
cpu_load_tuple = None
# Memory
mem_virtual = None
mem_virtual_total = None
mem_virtual_available = None
mem_virtual_used = None
# Disks
disk_partitions = None
disk_usage_list = None
disk_io_counters = None
# Network
net_io_counters = None
net_connections = None
net_if_addrs = None
net_if_stats = None
# Sensors 
# TODO: Add check if OS is Linux or FreeBSD
sensors_temperatures = None
sensors_fans = None
sensors_battery = None
# Other
boot_time = None
users = None

def save_system_info():
    # System Info Variables
    # CPU 
    cpu_percent_overall = psutil.cpu_percent(percpu = False)
    cpu_percent_list = psutil.cpu_percent(percpu = True)
    cpu_stats = psutil.cpu_stats()
    cpu_load_tuple = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
    # Memory
    mem_virtual = psutil.virtual_memory()
    mem_virtual_total = mem_virtual.total
    mem_virtual_available = mem_virtual.available
    mem_virtual_used = mem_virtual.used
    # Disks
    disk_partitions = psutil.disk_partitions(all = False)
    disk_usage = [None] * len(disk_partitions)
    for i, partition in enumerate(disk_partitions):
        if os.name == 'nt':
            if 'cdrom' in partition.opts or partition.fstype == '':
                # skip cd-rom drives with no disk in it; they may raise
                # ENOENT, pop-up a Windows GUI error for a non-ready
                # partition or just hang.
                continue
        disk_usage[i] = psutil.disk_usage(partition.mountpoint)
    disk_io_counters = psutil.disk_io_counters(perdisk = True)
    # Network
    net_io_counters = psutil.net_io_counters(pernic = True)
    net_connections = psutil.net_connections()
    net_if_addrs = psutil.net_if_addrs()
    net_if_stats = psutil.net_if_stats()
    # Sensors 
    # TODO: Add check if OS is Linux or FreeBSD
    # sensors_temperatures = psutil.sensors_temperatures(fahrenheit =  False)
    # sensors_fans = psutil.sensors_fans()
    sensors_battery = psutil.sensors_battery()
    # Other
    boot_time = psutil.boot_time()
    users = psutil.users()

save_system_info()

# Overall System Info List

def get_static_system_info():
    static_system_info_dict = {
        "cpu_thread_count": get_cpu_thread_count(),
        "cpu_physical_count": get_cpu_physical_count()
    }
    return static_system_info_dict

def get_dynamic_system_info():
    dynamic_system_info_dict = {
        "cpu_percent_overall": get_cpu_percent_overall(),
        "cpu_percent_list": get_cpu_percent_list(),
        "mem_total": get_mem_total(),
        "mem_left": get_mem_left()
    }
    return dynamic_system_info_dict

save_system_info()

# CPU Functions

def get_cpu_thread_count():
    return cpu_thread_count

def get_cpu_physical_count():
    return cpu_physical_count

def get_cpu_percent_overall():
    return cpu_percent_overall

def get_cpu_percent_list():
    return cpu_percent_list

def get_cpu_stats():
    return cpu_stats

def get_cpu_load():
    return cpu_load_tuple

# Memory Functions

def get_mem_total():
    return mem_virtual_total

def get_mem_left():
    return mem_virtual_available

# Disk Functions

def get_disk_partition_list():
    return disk_partitions

def get_disk_partition_usage():
    return disk_usage_list

# Network Functions

def get_net_connections_list():
    return net_connections

# System Info Logging Scheduler


# Schedule System Monitor
# TODO: Fix not scheduling properly
def save_system_info_sched():
    save_system_info()
    scheduler.enter(60, 1, save_system_info_sched, ())

scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(60, 1, save_system_info_sched, ())
scheduler.run(blocking = False)