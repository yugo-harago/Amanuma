<template>
  <nav class="navbar navbar-dark align-items-start sidebar sidebar-dark accordion bg-gradient-primary p-0">
    <div class="container-fluid d-flex flex-column p-0">
      <a class="navbar-brand d-flex justify-content-center align-items-center sidebar-brand m-0" href="#">
        <div class="sidebar-brand-icon rotate-n-15" style="transform: initial">
          <img class="d-flex mx-2" style="width: 40px; height: 30px; filter: invert(100%)"
            src="@/assets/img/Adventist_Symbol.svg" />
        </div>
        <router-link class="nav-link" to="/" active-class="active">
          <div class="sidebar-brand-text mx-3"><span>天沼オフィス</span></div>
        </router-link>
      </a>
      <hr class="sidebar-divider my-0" />
      <ul class="navbar-nav text-light" id="accordionSidebar">
        <li class="nav-item">
          <router-link to="/" class="nav-link">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -32 576 576" width="1em" height="1em" fill="currentColor">
              <!--! Font Awesome Free 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2022 Fonticons, Inc. -->
              <path
                d="M511.8 287.6L512.5 447.7C512.5 450.5 512.3 453.1 512 455.8V472C512 494.1 494.1 512 472 512H456C454.9 512 453.8 511.1 452.7 511.9C451.3 511.1 449.9 512 448.5 512H392C369.9 512 352 494.1 352 472V384C352 366.3 337.7 352 320 352H256C238.3 352 224 366.3 224 384V472C224 494.1 206.1 512 184 512H128.1C126.6 512 125.1 511.9 123.6 511.8C122.4 511.9 121.2 512 120 512H104C81.91 512 64 494.1 64 472V360C64 359.1 64.03 358.1 64.09 357.2V287.6H32.05C14.02 287.6 0 273.5 0 255.5C0 246.5 3.004 238.5 10.01 231.5L266.4 8.016C273.4 1.002 281.4 0 288.4 0C295.4 0 303.4 2.004 309.5 7.014L416 100.7V64C416 46.33 430.3 32 448 32H480C497.7 32 512 46.33 512 64V185L564.8 231.5C572.8 238.5 576.9 246.5 575.8 255.5C575.8 273.5 560.8 287.6 543.8 287.6L511.8 287.6z">
              </path>
            </svg><span class="mx-1">ホーム</span></router-link>
        </li>
        <li class="nav-item">
          <router-link to="/news" class="nav-link"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
              fill="currentColor" class="bi bi-megaphone" viewBox="0 0 16 16">
              <path
                d="M13 2.5a1.5 1.5 0 0 1 3 0v11a1.5 1.5 0 0 1-3 0v-.214c-2.162-1.241-4.49-1.843-6.912-2.083l.405 2.712A1 1 0 0 1 5.51 15.1h-.548a1 1 0 0 1-.916-.599l-1.85-3.49a68.14 68.14 0 0 0-.202-.003A2.014 2.014 0 0 1 0 9V7a2.02 2.02 0 0 1 1.992-2.013 74.663 74.663 0 0 0 2.483-.075c3.043-.154 6.148-.849 8.525-2.199V2.5zm1 0v11a.5.5 0 0 0 1 0v-11a.5.5 0 0 0-1 0zm-1 1.35c-2.344 1.205-5.209 1.842-8 2.033v4.233c.18.01.359.022.537.036 2.568.189 5.093.744 7.463 1.993V3.85zm-9 6.215v-4.13a95.09 95.09 0 0 1-1.992.052A1.02 1.02 0 0 0 1 7v2c0 .55.448 1.002 1.006 1.009A60.49 60.49 0 0 1 4 10.065zm-.657.975 1.609 3.037.01.024h.548l-.002-.014-.443-2.966a68.019 68.019 0 0 0-1.722-.082z" />
            </svg>
            <span class="mx-1">お知らせ</span></router-link>
        </li>
        <li class="nav-item">
          <router-link to="/article" class="nav-link"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em"
              fill="currentColor" viewBox="0 0 16 16" class="bi bi-file-text" style="font-size: 17px">
              <path
                d="M5 4a.5.5 0 0 0 0 1h6a.5.5 0 0 0 0-1H5zm-.5 2.5A.5.5 0 0 1 5 6h6a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5zM5 8a.5.5 0 0 0 0 1h6a.5.5 0 0 0 0-1H5zm0 2a.5.5 0 0 0 0 1h3a.5.5 0 0 0 0-1H5z">
              </path>
              <path
                d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2zm10-1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1z">
              </path>
            </svg><span class="mx-1">記事</span></router-link>
        </li>
        <li class="nav-item">
          <router-link to="/worship" class="nav-link"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em"
              viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"
              stroke-linejoin="round" class="icon icon-tabler icon-tabler-building-church" style="font-size: 22px">
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <line x1="3" y1="21" x2="21" y2="21"></line>
              <path d="M10 21v-4a2 2 0 0 1 4 0v4"></path>
              <line x1="10" y1="5" x2="14" y2="5"></line>
              <line x1="12" y1="3" x2="12" y2="8"></line>
              <path d="M6 21v-7m-2 2l8 -8l8 8m-2 -2v7"></path>
            </svg><span class="mx-1">教会案内</span></router-link>
        </li>
        <li class="nav-item">
          <router-link to="/worship" class="nav-link"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"
              width="1em" height="1em" fill="currentColor" style="font-size: 17px">
              <!--! Font Awesome Free 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2022 Fonticons, Inc. -->
              <path
                d="M495.9 132.2C505.8 137.9 512 148.5 512 160V480C512 497.7 497.7 512 480 512C462.3 512 448 497.7 448 480V178.6L256 68.86L64 178.6V480C64 497.7 49.67 512 32 512C14.33 512 0 497.7 0 480V160C0 148.5 6.153 137.9 16.12 132.2L240.1 4.216C249.1-1.405 262-1.405 271.9 4.216L495.9 132.2zM216 168C216 145.9 233.9 128 256 128C278.1 128 296 145.9 296 168C296 190.1 278.1 208 256 208C233.9 208 216 190.1 216 168zM224 512C210.7 512 200 501.3 200 488V313.5L173.1 363.4C166.8 375 152.3 379.4 140.6 373.1C128.1 366.8 124.6 352.3 130.9 340.6L168.7 270.3C184.1 241.8 213.9 223.1 246.2 223.1H265.8C298.1 223.1 327.9 241.8 343.3 270.3L381.1 340.6C387.4 352.3 383 366.8 371.4 373.1C359.7 379.4 345.2 375 338.9 363.4L312 313.5V488C312 501.3 301.3 512 288 512C274.7 512 264 501.3 264 488V400H248V488C248 501.3 237.3 512 224 512V512z">
              </path>
            </svg><span class="mx-1">礼拝情報</span></router-link>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="register.html"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
              fill="currentColor" class="bi bi-door-closed" viewBox="0 0 16 16">
              <path d="M3 2a1 1 0 0 1 1-1h8a1 1 0 0 1 1 1v13h1.5a.5.5 0 0 1 0 1h-13a.5.5 0 0 1 0-1H3V2zm1 13h8V2H4v13z" />
              <path d="M9 9a1 1 0 1 0 2 0 1 1 0 0 0-2 0z" />
            </svg><span class="mx-1">部室</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="chat.html"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em"
              fill="currentColor" viewBox="0 0 16 16" class="bi bi-chat-fill" style="font-size: 14px">
              <path
                d="M8 15c4.418 0 8-3.134 8-7s-3.582-7-8-7-8 3.134-8 7c0 1.76.743 3.37 1.97 4.6-.097 1.016-.417 2.13-.771 2.966-.079.186.074.394.273.362 2.256-.37 3.597-.938 4.18-1.234A9.06 9.06 0 0 0 8 15z">
              </path>
            </svg><span class="mx-1">チャット</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="table.html"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em"
              fill="currentColor" viewBox="0 0 16 16" class="bi bi-person-fill" style="font-size: 17px">
              <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path>
            </svg>
            <span class="mx-1">ユーザー管理</span></a>
        </li>
      </ul>
    </div>
  </nav>
  <div v-if="this.$route.name !== 'HomeView'" style="height: 57pt"></div>
</template>

<script>
export default {
  name: 'Sidebar',
}
</script>

<style scoped></style>
