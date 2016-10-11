$("#drag-and-drop-zone").dmUploader({
  url:'{{uploadpath}}',
  method:'post',
  dataType:'json',
  extFilter:'{{extfile}}',
  maxFiles:'99',
  onFileTypeError: function(file){
    console.log("请上传csv格式文件");
  },
  onFilesMaxError: function(file){
    console.log("单次上传上限暂定为99，请分开上传");
  },
  onInit: function(){
    $.danidemo.addLog('#demo-debug', 'default', '插件正常加载');
  },
  onBeforeUpload: function(id){
    $.danidemo.addLog('#demo-debug', 'default', '开始上传 #' + id);

    $.danidemo.updateFileStatus(id, 'default', '正在上传...');
  },
  onNewFile: function(id, file){
    $.danidemo.addFile('#demo-files', id, file);
  },
  onComplete: function(){
    $.danidemo.addLog('#demo-debug', 'default', '文件传输全部完成');
  },
  onUploadProgress: function(id, percent){
    var percentStr = percent + '%';

    $.danidemo.updateFileProgress(id, percentStr);
  },
  onUploadSuccess: function(id, data){
    $.danidemo.addLog('#demo-debug', 'success', '第 #' + id + ' 文件上传完成');

    $.danidemo.addLog('#demo-debug', 'info', '第 #' + id + ': 文件的服务器响应信息' + JSON.stringify(data));

    $.danidemo.updateFileStatus(id, 'success', '上传完成');

    $.danidemo.updateFileProgress(id, '100%');
  },
  onUploadError: function(id, message){
    $.danidemo.updateFileStatus(id, 'error', message);

    $.danidemo.addLog('#demo-debug', 'error', '第 #' + id + ': 文件上传失败' + message);
  },
  onFileExtError: function(file){
    $.danidemo.addLog('#demo-debug', 'error', '无法上传 \'' + file.name + '\' : 文件必须为csv格是');
  },
  onFallbackMode: function(message){
    $.danidemo.addLog('#demo-debug', 'info', '浏览器不支持: ' + message);
    // $.danidemo.addLog('#demo-debug', 'info', 'Browser not supported(do something else here!): ' + message);
  }
});
