// 获取所有锚点链接
const anchors = document.querySelectorAll('nav a');

// 绑定点击事件
anchors.forEach(a => {

  a.addEventListener('click', e => {

    // 阻止默认跳转
    e.preventDefault();

    // 获取href
    const id = e.target.getAttribute('href');

    // 找到对应锚点元素  
    const anchor = document.querySelector(id);

    // 滚动到锚点位置 
    anchor.scrollIntoView({ 
      behavior: 'smooth',
      block: 'start',
    });

  });

});