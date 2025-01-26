#!/usr/bin/env python3.12

import platform
import time
import psutil
import humanize

def sysinfo():
    print("="*40,"SYSTEM INFORMATION","="*40)
    vm_info = platform.node();
    vm_architecture = platform.machine()
    vm_kernal = platform.release()
    vm_boottime = psutil.boot_time()
    print(f"System Name: {vm_info}")
    print(f"system architecure: {vm_architecture}")
    print(f"System Kernal: {vm_kernal}")
    print(f"System BootTime: {time.ctime(vm_boottime)}")

sysinfo()

def cpuinfo():
    print("="*40," CPU INFORMATION","="*40)
    vm_cpu = psutil.cpu_count()
    vm_cpu_freq = psutil.cpu_freq()
    vm_cpu_usage = psutil.cpu_percent()
    print(f"CPU Count: {vm_cpu}")
    print(f"CPU Frequency: {vm_cpu_freq[0] Mhz}")
    print(f"CPU Usage: {vm_cpu_usage}%")
    
cpuinfo()

def memoryinfo():
    print("="*40," Memory INFORMATION","="*40)
    vm_memory = psutil.virtual_memory()
    print(f"SYSTEM MEMORY: {humanize.naturalsize(vm_memory.total)}")
    print(f"Used MEMORY: {humanize.naturalsize(vm_memory.used)}")
    print(f"Avaible MEMORY: {humanize.naturalsize(vm_memory.available)}")
    print(f"Percentage Usage: {vm_memory.percent}%")

memoryinfo()

def swapinfo():
    print("="*40," Swap INFORMATION","="*40)
    vm_swap = psutil.swap_memory()
    print(f"ToTal Swap: {humanize.naturalsize(vm_swap.total)}")
    print(f"Used Swap: {humanize.naturalsize(vm_swap.used)}")
    print(f"Free Swap: {humanize.naturalsize(vm_swap.free)}")
    print(f"Percentage Usage: {vm_swap.percent}%")

swapinfo()

def infodiskpart():
    print("="*40," Disk INFORMATION","="*40)
    partitions = psutil.disk_partitions()
    for diskpart in partitions:
        print(f"Device : {diskpart.device}")
        print(f"Mountpoint : {diskpart.mountpoint}")
        print(f"Filesystem : {diskpart.fstype}")
        diskpart_usage = psutil.disk_usage(diskpart.mountpoint)
        print(f"Total Size: {humanize.naturalsize(diskpart_usage.total)}")
        print(f"Total Used: {humanize.naturalsize(diskpart_usage.used)}")
        print(f"Free Size: {humanize.naturalsize(diskpart_usage.free)}")
        print(f"Percentage Usage: {diskpart_usage.percent}%")

infodiskpart()


