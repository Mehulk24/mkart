function toggleMenu(event, targetId) {
    event.preventDefault(); // Prevent default link behavior
    const menuItems = document.getElementsByClassName('nav-item1');
    const conavs = document.getElementsByClassName('conav');
  
    // Hide all conavs and deactivate all menu items
    for (let i = 0; i < conavs.length; i++) {
      conavs[i].classList.remove('active');
      menuItems[i].classList.remove('active');
    }
  
    // Show the clicked conav and activate the menu item
    const targetconav = document.getElementById(targetId);
    const targetMenuItem = event.target;
    targetconav.classList.add('active');
    targetMenuItem.classList.add('active');
  }

  function activateMenuItem(event, index) {
    event.preventDefault();
    const menuItems = document.getElementsByClassName('nav-item1');
    
    for (let i = 0; i < menuItems.length; i++) {
      menuItems[i].classList.remove('active');
    }
    
    const menuItem = event.target;
    menuItem.classList.add('active');
    
    const underline = document.querySelector('.underline');
    const menuItemWidth = menuItem.offsetWidth;
    const menuItemOffsetLeft = menuItem.offsetLeft;
    
    underline.style.width = menuItemWidth + 'px';
    underline.style.transform = `translateX(${menuItemOffsetLeft}px)`;
  }