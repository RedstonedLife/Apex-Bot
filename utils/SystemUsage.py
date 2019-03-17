def memory_usage_psutil():
    # return the memory usage in MB
    import psutil, os
    ram_used = psutil.virtual_memory()
    return ram_used[2]

def cpu_usage_psutil():
    import psutil
    # gives a single float value

    return psutil.cpu_percent()
