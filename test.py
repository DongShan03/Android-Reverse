import frida

rdev = frida.get_remote_device()
print(rdev)

processes = rdev.enumerate_processes()
for process in processes:
    print(process)

#Application(identifier="com.che168.autotradercloud", name="车智赢+", pid=3119, parameters={})
front_app = rdev.get_frontmost_application()
print(front_app)