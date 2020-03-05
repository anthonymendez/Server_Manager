import psutil

# Overall System Info List

def system_info():
    return {
        "cpu_count": cpu_count(),
        "cpu_percent_list": cpu_percent_list(),
        "cpu_stats": cpu_stats(),
        "mem_total": mem_total(),
        "mem_left": mem_left(),
        "disk_partition_list": disk_partition_list()
    }

# CPU Functions

def cpu_count():
    return psutil.cpu_count()

def cpu_percent_list():
    return psutil.cpu_percent(percpu = True)

def cpu_stats():
    return psutil.cpu_freq(percpu = True)

# Memory Functions

def mem_total():
    return psutil.virtual_memory().total

def mem_left():
    return psutil.virtual_memory().available

# Disk Functions

def disk_partition_list():
    return psutil.disk_partitions(all = True)

def disk_partition_usage(path):
    return psutil.disk_usage(path)

# Network Functions

def net_connections_list():
    return psutil.net_connections(king="all")
