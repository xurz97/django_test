// 获取textarea元素
var textarea = document.getElementById('input_data');

// 获取提交按钮元素
var submitButton = document.getElementById('submit_button');

// 保存输入文本
submitButton.addEventListener('click', function() {
  localStorage.setItem('input_data', textarea.value);
});

// 恢复输入文本
window.onload = function() {
  var savedData = localStorage.getItem('input_data');
  if (savedData !== null) {
    textarea.value = savedData;
  }
};