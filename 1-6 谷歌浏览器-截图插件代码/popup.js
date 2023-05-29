document.addEventListener('DOMContentLoaded', function () {
  var screenshotButton = document.getElementById('screenshotButton');
  screenshotButton.addEventListener('click', function () {
    chrome.tabs.captureVisibleTab(function (screenshotUrl) {
      // 在这里可以处理截图的URL（screenshotUrl），例如显示在页面上或进行其他操作
      //console.log(screenshotUrl);
	  
	  var previewImage = document.getElementById('previewImage');
      previewImage.src = screenshotUrl;
    });
  });
  
   saveButton.addEventListener('click', function () {
    var previewImage = document.getElementById('previewImage');
    var screenshotUrl = previewImage.src;

    // 创建一个虚拟的 <a> 元素来触发文件下载
    var link = document.createElement('a');
    link.href = screenshotUrl;
    link.download = 'screenshot.png';

    // 模拟点击虚拟的 <a> 元素来触发下载
    link.click();
  });
});
