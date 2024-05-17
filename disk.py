import psutil


class Disk:
    @staticmethod
    def detect_drives():
        drives = []
        partitions = psutil.disk_partitions(all=True)
        for partition in partitions:
            usage = psutil.disk_usage(partition.device)
            drive = {
                "Drive": partition.device,
                "Total": usage.total / (1024 ** 3),
                "Free": usage.free / (1024 ** 3),
                "Percent": usage.percent
            }
            drives.append(drive)
        return drives
