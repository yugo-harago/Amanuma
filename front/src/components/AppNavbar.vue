<template>
  <nav
    class="navbar navbar-light navbar-expand-md fixed-top text-light d-flex align-items-center navbar-shrink pt-2"
  >
    <div class="container">
      <router-link
        class="navbar-brand d-flex justify-content-center align-items-center align-content-center py-2"
        to="/"
      >
        <img class="logo d-flex mx-2" src="@/assets/img/Adventist_Symbol.svg" />
        <span
          class="brand-text d-flex justify-content-center align-items-center"
        >
          天沼教会
        </span>
      </router-link>
      <button
        data-bs-toggle="collapse"
        class="navbar-toggler"
        data-bs-target="#navcol-1"
      >
        <span class="visually-hidden">Toggle navigation</span>
        <span class="navbar-toggler-icon"> </span>
      </button>
      <div class="collapse navbar-collapse" id="navcol-1">
        <ul class="navbar-nav mx-auto">
          <li
            class="nav-item d-flex flex-column justify-content-lg-center align-items-lg-center mx-2"
          >
            <router-link class="nav-link" to="/" active-class="active">
              <i
                class="icon-home d-flex justify-content-center"
                style="font-size: 28px"
              >
              </i>
              <span>ホーム</span>
            </router-link>
          </li>
          <li
            class="nav-item d-flex flex-column justify-content-center align-items-center mx-2"
          >
            <router-link
              class="nav-link d-flex flex-column justify-content-center align-items-center"
              to="news"
              active-class="active"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="1em"
                height="1em"
                fill="currentColor"
                viewBox="0 0 16 16"
                class="bi bi-file-text"
                style="font-size: 28px"
              >
                <path
                  d="M5 4a.5.5 0 0 0 0 1h6a.5.5 0 0 0 0-1H5zm-.5 2.5A.5.5 0 0 1 5 6h6a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5zM5 8a.5.5 0 0 0 0 1h6a.5.5 0 0 0 0-1H5zm0 2a.5.5 0 0 0 0 1h3a.5.5 0 0 0 0-1H5z"
                ></path>
                <path
                  d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2zm10-1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1z"
                ></path>
              </svg>
              <span class="d-block">お知らせ</span>
            </router-link>
          </li>
          <li
            class="nav-item d-flex flex-column justify-content-center align-items-center mx-2"
          >
            <router-link
              class="nav-link d-flex flex-column justify-content-center align-items-center"
              to="about-church"
              active-class="active"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="1em"
                height="1em"
                viewBox="0 0 24 24"
                stroke-width="2"
                stroke="currentColor"
                fill="none"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="icon icon-tabler icon-tabler-building-church"
                style="font-size: 36px"
              >
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <line x1="3" y1="21" x2="21" y2="21"></line>
                <path d="M10 21v-4a2 2 0 0 1 4 0v4"></path>
                <line x1="10" y1="5" x2="14" y2="5"></line>
                <line x1="12" y1="3" x2="12" y2="8"></line>
                <path d="M6 21v-7m-2 2l8 -8l8 8m-2 -2v7"></path>
              </svg>
              <span>教会案内</span>
            </router-link>
          </li>
          <li
            class="nav-item d-flex flex-column justify-content-center align-items-center mx-2"
          >
            <router-link
              class="nav-link d-flex flex-column align-items-center"
              to="worship"
              active-class="active"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 512 512"
                width="1em"
                height="1em"
                fill="currentColor"
                style="font-size: 36px"
              >
                <!--! Font Awesome Free 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2022 Fonticons, Inc. -->
                <path
                  d="M495.9 132.2C505.8 137.9 512 148.5 512 160V480C512 497.7 497.7 512 480 512C462.3 512 448 497.7 448 480V178.6L256 68.86L64 178.6V480C64 497.7 49.67 512 32 512C14.33 512 0 497.7 0 480V160C0 148.5 6.153 137.9 16.12 132.2L240.1 4.216C249.1-1.405 262-1.405 271.9 4.216L495.9 132.2zM216 168C216 145.9 233.9 128 256 128C278.1 128 296 145.9 296 168C296 190.1 278.1 208 256 208C233.9 208 216 190.1 216 168zM224 512C210.7 512 200 501.3 200 488V313.5L173.1 363.4C166.8 375 152.3 379.4 140.6 373.1C128.1 366.8 124.6 352.3 130.9 340.6L168.7 270.3C184.1 241.8 213.9 223.1 246.2 223.1H265.8C298.1 223.1 327.9 241.8 343.3 270.3L381.1 340.6C387.4 352.3 383 366.8 371.4 373.1C359.7 379.4 345.2 375 338.9 363.4L312 313.5V488C312 501.3 301.3 512 288 512C274.7 512 264 501.3 264 488V400H248V488C248 501.3 237.3 512 224 512V512z"
                ></path>
              </svg>
              <span>礼拝情報</span>
            </router-link>
          </li>
          <li
            class="nav-item d-flex flex-column justify-content-center align-items-center mx-2"
          >
            <router-link
              class="nav-link d-flex flex-column align-items-center"
              to="links"
              active-class="active"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="1em"
                height="1em"
                fill="currentColor"
                viewBox="0 0 16 16"
                class="bi bi-link-45deg"
                style="font-size: 37px"
              >
                <path
                  d="M4.715 6.542 3.343 7.914a3 3 0 1 0 4.243 4.243l1.828-1.829A3 3 0 0 0 8.586 5.5L8 6.086a1.002 1.002 0 0 0-.154.199 2 2 0 0 1 .861 3.337L6.88 11.45a2 2 0 1 1-2.83-2.83l.793-.792a4.018 4.018 0 0 1-.128-1.287z"
                ></path>
                <path
                  d="M6.586 4.672A3 3 0 0 0 7.414 9.5l.775-.776a2 2 0 0 1-.896-3.346L9.12 3.55a2 2 0 1 1 2.83 2.83l-.793.792c.112.42.155.855.128 1.287l1.372-1.372a3 3 0 1 0-4.243-4.243L6.586 4.672z"
                ></path>
              </svg>
              <span>リンク</span>
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <div v-if="this.$route.name !== 'HomeView'" style="height: 57pt"></div>
</template>

<script>
export default {
  name: 'AppNavbar',
}
</script>

<style scoped>
.navbar {
  background: rgba(129, 129, 129, 0.603);
}
.navbar-brand {
  background: rgba(0, 0, 0, 0.59);
  padding-right: 16px;
}
.logo {
  width: 40px;
  height: 30px;
  filter: invert(100);
}
.brand-text {
  display: block;
}
</style>
