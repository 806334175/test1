if (!requestScreenCapture()) {
    toast("请求截图失败");
    stop();
}
