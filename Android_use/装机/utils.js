importClass('java.net.Socket');

//找一张图并点击，返回坐标
function look_and_click(rename) {
    var firstcolor = rename.firstcolor
    var colors = rename.colors
    var x1 = rename.x1
    var y1 = rename.y1
    var x2 = rename.x2
    var y2 = rename.y2
    var img = captureScreen();
    try {
        //可能发生异常的代码 
        var point = findMultiColors(img, firstcolor, colors, { region: [x1, y1, x2 - x1, y2 - y1] })
    } catch (error) { }
    if (point) {
        log(rename.name + "-click:" + point.x + "," + point.y)
        click(point.x, point.y)
        return [point.x, point.y]
    } else {
        // toastLog(rename.name+":未找到")
        return [-1, -1]
    }
}

//找一张图，返回是否找到
function look_and_judge(rename) {
    var firstcolor = rename.firstcolor
    var colors = rename.colors
    var x1 = rename.x1
    var y1 = rename.y1
    var x2 = rename.x2
    var y2 = rename.y2
    var img = captureScreen();
    try {
        //可能发生异常的代码 
        var point = findMultiColors(img, firstcolor, colors, { region: [x1, y1, x2 - x1, y2 - y1] })
    } catch (error) { }

    if (point) {
        log(rename.name + "-jidge:" + point.x + "," + point.y)
        // return [point.x,point.y]
        return true
    } else {
        // toastLog(rename.name+":未找到")
        // return [-1,-1]
        return false
    }
}

//在一定时间内找一张图，找到返回true
function look_in_time_judge(rename, t) {
    var firstcolor = rename.firstcolor
    var colors = rename.colors
    var x1 = rename.x1
    var y1 = rename.y1
    var x2 = rename.x2
    var y2 = rename.y2
    var time = 0
    while (time > t) {
        var img = captureScreen();
        try {
            //可能发生异常的代码 
            var point = findMultiColors(img, firstcolor, colors, { region: [x1, y1, x2 - x1, y2 - y1] })
        } catch (error) { }
        if (point) {
            log(rename.name + "-jidge:" + point.x + "," + point.y)
            // return [point.x,point.y]
            return true
        } else {
            // toastLog(rename.name+":未找到")
            // return [-1,-1]
            time += 1
            sleep(t * 1000)
        }
    }
    return false
}

//在一定时间内找一张图，找到点击
function look_in_time_click(rename, t) {
    var firstcolor = rename.firstcolor
    var colors = rename.colors
    var x1 = rename.x1
    var y1 = rename.y1
    var x2 = rename.x2
    var y2 = rename.y2
    var time = 0
    while (time > t) {
        var img = captureScreen();
        try {
            //可能发生异常的代码 
            var point = findMultiColors(img, firstcolor, colors, { region: [x1, y1, x2 - x1, y2 - y1] })
        } catch (error) { }
        if (point) {
            log(rename.name + "-jidge:" + point.x + "," + point.y)
            // return [point.x,point.y]
            click(point.x, point.y)
            return true
        } else {
            // toastLog(rename.name+":未找到")
            // return [-1,-1]
            time += 1
            sleep(t * 1000)
        }
    }
    return false
}

//点击一张图，后等待2秒
function look_click_wait(rename) {
    var firstcolor = rename.firstcolor
    var colors = rename.colors
    var x1 = rename.x1
    var y1 = rename.y1
    var x2 = rename.x2
    var y2 = rename.y2
    var img = captureScreen();
    try {
        //可能发生异常的代码 
        var point = findMultiColors(img, firstcolor, colors, { region: [x1, y1, x2 - x1, y2 - y1] })
    } catch (error) { }
    if (point) {
        log(rename.name + "-click:" + point.x + "," + point.y)
        click(point.x, point.y)
        sleep(2000)
        return [point.x, point.y]
    } else {
        // toastLog(rename.name+":未找到")
        return [-1, -1]
    }
}

//找一张图，找到后在偏移位置点击
function look_deviation_click(rename, my_x, my_y) {
    var firstcolor = rename.firstcolor
    var colors = rename.colors
    var x1 = rename.x1
    var y1 = rename.y1
    var x2 = rename.x2
    var y2 = rename.y2
    var img = captureScreen();
    try {
        //可能发生异常的代码 
        var point = findMultiColors(img, firstcolor, colors, { region: [x1, y1, x2 - x1, y2 - y1] })
    } catch (error) { }
    if (point) {
        log(rename.name + "-click:" + point.x + "," + point.y)
        click(point.x + my_x, point.y + my_y)
        return [point.x, point.y]
    } else {
        // toastLog(rename.name+":未找到")
        return [-1, -1]
    }
}

//返回找到图的坐标
function look_coordinate(rename) {
    var firstcolor = rename.firstcolor
    var colors = rename.colors
    var x1 = rename.x1
    var y1 = rename.y1
    var x2 = rename.x2
    var y2 = rename.y2
    var img = captureScreen();
    try {
        //可能发生异常的代码 
        var point = findMultiColors(img, firstcolor, colors, { region: [x1, y1, x2 - x1, y2 - y1] })
    } catch (error) { }
    if (point) {
        log(rename.name + "-click:" + point.x + "," + point.y)
        return [point.x, point.y]
    } else {
        // toastLog(rename.name+":未找到")
        return [-1, -1]
    }
}

//设置手机为可获取新IP状态
function IP_open() {
    files.write("/sdcard/script/IP_state.txt", "1") //将 string 内容存入文件，成功返回 true
}

//设置手机为不可获取新IP状态
function IP_close() {
    files.write("/sdcard/script/IP_state.txt", "0") //将 string 内容存入文件，成功返回 true
}

//获取手机是否可获取新IP
function read_IP_state() {
    try {
        var res = files.read("/sdcard/script/IP_state.txt")
    } catch (error) {
        return false
    }
    return res
}

//将这次任务的包名记录
function write_package(pac) {
    files.append("/sdcard/script/package_now.txt", pac + "\r\n") //将 string 内容存入文件，成功返回 true
}

//清除包名记录
function clear_package() {
    files.remove("/sdcard/script/package_now.txt")
}

//获取包名记录
function read_package() {
    try {
        var res = files.read("/sdcard/script/package_now.txt")
    } catch (error) {
        return false
    }
    return res
}

//通过手机中的配置文件，来决定切换IP的方法
function change_ip(country) {
    var ip_mode = files.read("/sdcard/script/ip_mode.txt")
    if (ip_mode == "1") {
        change_lum(country)
    } else {
        change_911(country)
    }
}

//字符串转字节序列
function stringToByte(str) {
    var bytes = new Array();
    var len, c;
    var len = str.length;
    for (var i = 0; i < len; i++) {
        c = str.charCodeAt(i);
        if (c >= 0x010000 && c <= 0x10FFFF) {
            bytes.push(((c >> 18) & 0x07) | 0xF0);
            bytes.push(((c >> 12) & 0x3F) | 0x80);
            bytes.push(((c >> 6) & 0x3F) | 0x80);
            bytes.push((c & 0x3F) | 0x80);
        } else if (c >= 0x000800 && c <= 0x00FFFF) {
            bytes.push(((c >> 12) & 0x0F) | 0xE0);
            bytes.push(((c >> 6) & 0x3F) | 0x80);
            bytes.push((c & 0x3F) | 0x80);
        } else if (c >= 0x000080 && c <= 0x0007FF) {
            bytes.push(((c >> 6) & 0x1F) | 0xC0);
            bytes.push((c & 0x3F) | 0x80);
        } else {
            bytes.push(c & 0xFF);
        }
    }
    return bytes;
}

//通过socket方法，来切换911
function change_911(country) {
    info_log("change_911")
    if (read_IP_state() != "0") {
        try {
            var phone_prot = files.read("/sdcard/script/phone_prot.txt")
            var hostandport = files.read("/sdcard/script/PC_hostandport.txt")
            var pc_res = hostandport.split("-")
            var socket = new Socket(pc_res[0], pc_res[1]);
            var os = socket.getOutputStream();
            os.write(stringToByte(phone_prot + "-" + country));
            os.close()
            IP_close()
        } catch (error) {
            info_log(error)
        }

    }
}

//通过局域网请求，来切换lum
function change_lum(country) {
    info_log("change_lum")
    if (read_IP_state() != "0") {
        try {
            var hostandport = files.read("/sdcard/script/PC_lum_hostandport.txt")
            var pc_res = hostandport.split("-")
            var res = http.get("http://" + pc_res[0] + ":22999/api/refresh_sessions/" + pc_res[1], "", "", true)
            if (res.statusCode == "200" || res.statusCode == "204") {
                info_log("lum IP Change Success")
                sleep(3000)
                IP_close()
            } else {
                mylog("<-error->:lum IP Change fail")
                sleep(3000)
                IP_open()
            }
        } catch (error) {
            info_log(error)
        }
    }
}

//通过传入的国家来判断是否和本地的ip匹配，并返回国家和ip
function check_ip_local(mycountry) {
    try {
        var res = http.get("http://ip-api.com/json")
        var json_str = res.body.string()
        var json_obj = JSON.parse(json_str)
        var country = json_obj.countryCode
        var query = json_obj.query
        if (country == mycountry) {
            info_log("IP_NOW:" + country + " " + query)
            sleep(3000)
            return [country, query]
        } else {
            mylog("<-error->:IP_ERROR:country error :" + country)
            sleep(3000)
            IP_open()
            return false
        }
    } catch (error) {
        mylog("<-error->:IP_ERROR:" + error)
        sleep(3000)
        IP_open()
        return false
    }
}

function mylog(str) {
    // files.ensureDir("/sdcard/abc/")
    files.append("/sdcard/Armstrong_Cyclotron_Armstrong_Cannon.txt", str + "\r\n")
    log(str)
}

function info_log(str) {
    // files.ensureDir("/sdcard/abc/")
    var time = new Date()
    files.append("/sdcard/Armstrong_Cyclotron_Armstrong_Cannon.txt", "<-info->[" + time.getHours() + ":" + time.getMinutes() + ":" + time.getSeconds() + "]:" + str + "\r\n")
    log("<-info->[" + time.getHours() + ":" + time.getMinutes() + ":" + time.getSeconds() + "]:" + str)
}


//生成从minNum到maxNum的随机数
function randomNum(minNum, maxNum) {
    switch (arguments.length) {
        case 1:
            return parseInt(Math.random() * minNum + 1, 10);
            break;
        case 2:
            return parseInt(Math.random() * (maxNum - minNum + 1) + minNum, 10);
            break;
        default:
            return 0;
            break;
    }
}



function back_to_autojs() {
    launch("com.ning.script.engine")
    // launch("org.autojs.autojs")
    // var endflag = 0
    // var back_to_autojs_thread = threads.start(function () {
    //     while (true) {
    //         if (className("android.widget.TextView").text("管理").exists()) {
    //             try{
    //                 className("android.widget.TextView").text("管理").findOnce().parent().click()
    //             }catch(error){

    //             }
    //             endflag = 1
    //             break
    //         }
    //     }
    // })
    // var end_time = get_time() + (30 * 1000)
    // while (true) {
    //     if (get_time() > end_time) {
    //         break
    //     }
    //     if (endflag == 1) {
    //         break
    //     }
    //     sure_start("org.autojs.autojs")
    // }
    // back_to_autojs_thread.interrupt()

}

function get_time() {
    var d = new Date()
    return d.getTime()
}

function kill_app(my_package) {
    adb = "am force-stop " + my_package
    shell(adb, true)
    // launch(package)
    // sleep(1000)
    // openAppSetting(package)
    // while (true) {
    //     if (id("right_button").packageName("com.android.settings").exists()) {
    //         id("right_button").packageName("com.android.settings").findOnce().click()
    //     }
    //     // if (packageName("com.android.settings").className("android.widget.Button").depth(6).exists()) {
    //     //     var a = packageName("com.android.settings").className("android.widget.Button").find()
    //     //     a[1].click()
    //     //     break
    //     // }
    //     if (id("android:id/button1").exists()) {
    //         id("android:id/button1").findOnce().click()
    //         break
    //     }
    // }
}

function isFrontApp(package) {
    try {
        // result = shell("dumpsys activity top ", true)
        // if (result.code == 0) {
        //     str = result.result
        //     front_list = str.match(/ACTIVITY (.*)\//g)
        //     if (front_list[2].search(package) != -1) {
        //         return true
        //     }
        // } else {
        //     return false
        // }
        // return false

        if (package == currentPackage()) {
            return true
        } else {
            return false
        }

    } catch (error) {
        info_log("isFrontApp:" + error)
        sleep(3000)
        return false
    }
}

function sure_start(package) {
    if (isFrontApp(package) == false) {
        launch(package)
    }
}

function track_offer(wait_time) {
    info_log("track_offer")
    kill_app("oor.paocai.com.jumpurl")
    launch("oor.paocai.com.jumpurl")
    var endflag1 = 0
    var track_offer_thread_1 = threads.start(function () {
        while (true) {
            if (Find_Control(id("button"))) {
                setText(0, wait_time)
                sleep(2000)
                info_log("start track " + offer_url)
                Click_Control(id("button"))
                sleep(5000)
                endflag1 = 1
                break
            }
        }
    })
    var end_time1 = get_time() + (30 * 1000)
    while (true) {
        if (get_time() > end_time1) {
            mylog("<-error->:track_offer error 1")
            sleep(3000)
            track_offer()
            break
        }
        if (endflag1 == 1) {
            break
        }
        sure_start("oor.paocai.com.jumpurl")
    }
    track_offer_thread_1.interrupt()
    //-------------------------------
    var end_time2 = get_time() + (120 * 1000)
    while (true) {
        if (get_time() > end_time2) {
            mylog("<-error->:track_fail")
            return false
        }
        var track_info = files.read("/sdcard/Armstrong_Cyclotron_Armstrong_Cannon.txt")
        var res_success = track_info.indexOf("___track_url_success___")
        // var res_fail = track_info.indexOf("___track_url_fail___")
        if (res_success >= 0) {
            info_log("track_success")
            return true
        }
        sleep(1000)
        // sure_start("oor.paocai.com.jumpurl")
    }
}

function Prepare_retention() {
    info_log("Prepare_retention")
    kill_app("oor.paocai.com.jumpurl")
    launch("oor.paocai.com.jumpurl")
    var endflag1 = 0
    var Prepare_retention_thread_1 = threads.start(function () {
        while (true) {
            if (Find_Control(id("startRemain"))) {
                files.remove("/sdcard/backup.zip")
                info_log("start compress")
                Click_Control(id("startRemain"))
                sleep(5000)
                endflag1 = 1
                break
            }
        }
    })
    var end_time1 = get_time() + (30 * 1000)
    while (true) {
        if (get_time() > end_time1) {
            mylog("<-error->:Prepare_retention error 1")
            sleep(3000)
            Prepare_retention()
        }
        if (endflag1 == 1) {
            break
        }
        sure_start("oor.paocai.com.jumpurl")
    }
    Prepare_retention_thread_1.interrupt()
    //---------------------

    var end_time2 = get_time() + (30 * 1000)
    while (true) {
        if (get_time() > end_time2) {
            break
        }
        // var track_info = files.read("/sdcard/Armstrong_Cyclotron_Armstrong_Cannon.txt")
        // var res_success = track_info.indexOf("<-success->")
        // // var res_fail = track_info.indexOf("___track_url_fail___")
        // if (res_success >= 0) {
        //     // sleep(5000)
        //     // mylog("<-success->")
        //     break
        // }
        // sleep(1000)
        // if (files.exists("/sdcard/backup.zip")) {
        //     // utils.info_log("compress success")
        //     sleep(5000)
        //     break
        // }
    }

    // var end_time2 = get_time() + (120 * 1000)
    // while (true) {
    //     if (get_time() > end_time2) {
    //         mylog("<-error->:Prepare_retention error 2")
    //         sleep(3000)
    //         // Prepare_retention()
    //         break
    //     }
    //     if (files.exists("/sdcard/backup.zip")) {
    //         // utils.info_log("compress success")
    //         sleep(5000)
    //         break
    //     }
    // }
}

function Retention_mode() {
    info_log("Retention_mode")
    kill_app("oor.paocai.com.jumpurl")
    launch("oor.paocai.com.jumpurl")
    var endflag1 = 0
    var Retention_mode_thread_1 = threads.start(function () {
        while (true) {
            if (Find_Control(id("RemainMode"))) {
                Click_Control(id("RemainMode"))
                info_log("start decompression")
                sleep(5000)
                endflag1 = 1
                break
            }
        }
    })
    var end_time1 = get_time() + (30 * 1000)
    while (true) {
        if (get_time() > end_time1) {
            mylog("<-error->:Retention_mode error 1")
            sleep(3000)
            Retention_mode()
            break
        }
        if (endflag1 == 1) {
            break
        }
        sure_start("oor.paocai.com.jumpurl")
    }
    Retention_mode_thread_1.interrupt()
    //--------------------
    var end_time2 = get_time() + (120 * 1000)
    while (true) {
        if (get_time() > end_time2) {
            mylog("<-error->:Retention_mode error 2")
            sleep(3000)
            Retention_mode()
            break
        }
        if (files.exists("/sdcard/abc/taskInfo.txt")) {
            info_log("decompression success")
            sleep(5000)
            break
        }
    }
}


function Click_Control(Control_object) {
    try {
        if (Control_object.exists()) {
            Control_object.findOnce().click()
            sleep(2000)
            log(Control_object + "被点击");
        }
    } catch (error) {
        log("Click_Control:" + error);
    }
}

function Find_Control(Control_object) {
    try {
        if (Control_object.exists()) {
            log(Control_object + "被找到");
            return true
        } else {
            return false
        }
    } catch (error) {
        log("Find_Control:" + error);
    }
}






exports.look_and_click = look_and_click
exports.look_and_judge = look_and_judge
exports.look_in_time_judge = look_in_time_judge
exports.look_in_time_click = look_in_time_click
exports.look_click_wait = look_click_wait
exports.look_deviation_click = look_deviation_click
exports.look_coordinate = look_coordinate

exports.IP_open = IP_open
exports.IP_close = IP_close
exports.read_IP_state = read_IP_state
exports.write_package = write_package
exports.clear_package = clear_package
exports.read_package = read_package

exports.change_ip = change_ip
exports.change_911 = change_911
exports.change_lum = change_lum
exports.check_ip_local = check_ip_local

exports.mylog = mylog
exports.info_log = info_log

exports.randomNum = randomNum

exports.back_to_autojs = back_to_autojs
exports.get_time = get_time
exports.kill_app = kill_app
exports.isFrontApp = isFrontApp
exports.sure_start = sure_start
exports.track_offer = track_offer
exports.Prepare_retention = Prepare_retention
exports.Retention_mode = Retention_mode

exports.Click_Control = Click_Control
exports.Find_Control = Find_Control









