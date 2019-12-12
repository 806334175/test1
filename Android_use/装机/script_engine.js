function close_other_script() {
    var res = engines.all()
    for (i = 0; i < res.length; i++) {
        if (res[i].source.toString().indexOf("main") < 0) {
            res[i].forceStop()
        }  
    }
}

if (!requestScreenCapture()) {
    toastLog("请求截图失败");
    stop();
}

while (true) {
    if (files.exists("/sdcard/abc/taskinfonmd.txt")) {
        close_other_script()
        sleep(2000)
        files.move("/sdcard/abc/taskinfonmd.txt", "/sdcard/taskInfo.txt")
        var json_str = files.read("/sdcard/taskInfo.txt")
        var json_obj = JSON.parse(json_str)
        var script = json_obj.script_name
        toastLog("开始" + script)
        files.move("/sdcard/abc/" + script + ".js", "/sdcard/script/" + script + ".js")
        shell("rm -rf /sdcard/abc/*", false)
        engines.execScriptFile("/sdcard/script/" + script + ".js");
    }
    sleep(5000)
    device.keepScreenOn(6000)
    if (device.isCharging()){

    }else{
        close_other_script()
        confirm("USB断开");
    }
}

