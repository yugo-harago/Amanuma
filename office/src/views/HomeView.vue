<template>
  <div class="d-flex flex-column" id="content-wrapper">
    <div id="content">
      <nav
        class="navbar navbar-light navbar-expand bg-white shadow-sm mb-4 topbar static-top"
      >
        <div class="container-fluid">
          <ul class="navbar-nav flex-nowrap ms-auto">
            <li class="nav-item dropdown d-sm-none no-arrow">
              <a
                class="dropdown-toggle nav-link"
                aria-expanded="false"
                data-bs-toggle="dropdown"
                href="#"
                ><i class="fas fa-search"></i
              ></a>
              <div
                class="dropdown-menu dropdown-menu-end p-3 animated--grow-in"
                aria-labelledby="searchDropdown"
              >
                <form class="me-auto navbar-search w-100">
                  <div class="input-group">
                    <input
                      class="bg-light form-control border-0 small"
                      type="text"
                      placeholder="Search for ..."
                    />
                    <div class="input-group-append">
                      <button class="btn btn-primary py-0" type="button">
                        <i class="fas fa-search"></i>
                      </button>
                    </div>
                  </div>
                </form>
              </div>
            </li>
            <li class="nav-item dropdown no-arrow mx-1">
              <div class="nav-item dropdown no-arrow">
                <a
                  class="dropdown-toggle nav-link"
                  aria-expanded="false"
                  data-bs-toggle="dropdown"
                  href="#"
                  ><span class="badge bg-danger badge-counter">3+</span
                  ><i class="fas fa-bell fa-fw"></i
                ></a>
                <div
                  class="dropdown-menu dropdown-menu-end dropdown-list animated--grow-in"
                >
                  <h6 class="dropdown-header">alerts center</h6>
                  <a class="dropdown-item d-flex align-items-center" href="#">
                    <div class="me-3">
                      <div class="bg-primary icon-circle">
                        <i class="fas fa-file-alt text-white"></i>
                      </div>
                    </div>
                    <div>
                      <span class="small text-gray-500">December 12, 2019</span>
                      <p>A new monthly report is ready to download!</p>
                    </div> </a
                  ><a class="dropdown-item d-flex align-items-center" href="#">
                    <div class="me-3">
                      <div class="bg-success icon-circle">
                        <i class="fas fa-donate text-white"></i>
                      </div>
                    </div>
                    <div>
                      <span class="small text-gray-500">December 7, 2019</span>
                      <p>$290.29 has been deposited into your account!</p>
                    </div> </a
                  ><a class="dropdown-item d-flex align-items-center" href="#">
                    <div class="me-3">
                      <div class="bg-warning icon-circle">
                        <i class="fas fa-exclamation-triangle text-white"></i>
                      </div>
                    </div>
                    <div>
                      <span class="small text-gray-500">December 2, 2019</span>
                      <p>
                        Spending Alert: We've noticed unusually high spending
                        for your account.
                      </p>
                    </div> </a
                  ><a
                    class="dropdown-item text-center small text-gray-500"
                    href="#"
                    >Show All Alerts</a
                  >
                </div>
              </div>
            </li>
            <li class="nav-item dropdown no-arrow mx-1">
              <div class="nav-item dropdown no-arrow">
                <a
                  class="dropdown-toggle nav-link"
                  aria-expanded="false"
                  data-bs-toggle="dropdown"
                  href="#"
                  ><span class="badge bg-danger badge-counter">7</span
                  ><i class="fas fa-envelope fa-fw"></i
                ></a>
                <div
                  class="dropdown-menu dropdown-menu-end dropdown-list animated--grow-in"
                >
                  <h6 class="dropdown-header">alerts center</h6>
                  <a class="dropdown-item d-flex align-items-center" href="#">
                    <div class="dropdown-list-image me-3">
                      <img
                        class="rounded-circle"
                        src="@/assets/img/avatars/avatar4.jpeg"
                      />
                      <div class="bg-success status-indicator"></div>
                    </div>
                    <div class="fw-bold">
                      <div class="text-truncate">
                        <span
                          >Hi there! I am wondering if you can help me with a
                          problem I've been having.</span
                        >
                      </div>
                      <p class="small text-gray-500 mb-0">Emily Fowler - 58m</p>
                    </div> </a
                  ><a class="dropdown-item d-flex align-items-center" href="#">
                    <div class="dropdown-list-image me-3">
                      <img
                        class="rounded-circle"
                        src="@/assets/img/avatars/avatar2.jpeg"
                      />
                      <div class="status-indicator"></div>
                    </div>
                    <div class="fw-bold">
                      <div class="text-truncate">
                        <span
                          >I have the photos that you ordered last month!</span
                        >
                      </div>
                      <p class="small text-gray-500 mb-0">Jae Chun - 1d</p>
                    </div> </a
                  ><a class="dropdown-item d-flex align-items-center" href="#">
                    <div class="dropdown-list-image me-3">
                      <img
                        class="rounded-circle"
                        src="@/assets/img/avatars/avatar3.jpeg"
                      />
                      <div class="bg-warning status-indicator"></div>
                    </div>
                    <div class="fw-bold">
                      <div class="text-truncate">
                        <span
                          >Last month's report looks great, I am very happy with
                          the progress so far, keep up the good work!</span
                        >
                      </div>
                      <p class="small text-gray-500 mb-0">
                        Morgan Alvarez - 2d
                      </p>
                    </div> </a
                  ><a class="dropdown-item d-flex align-items-center" href="#">
                    <div class="dropdown-list-image me-3">
                      <img
                        class="rounded-circle"
                        src="@/assets/img/avatars/avatar5.jpeg"
                      />
                      <div class="bg-success status-indicator"></div>
                    </div>
                    <div class="fw-bold">
                      <div class="text-truncate">
                        <span
                          >Am I a good boy? The reason I ask is because someone
                          told me that people say this to all dogs, even if they
                          aren't good...</span
                        >
                      </div>
                      <p class="small text-gray-500 mb-0">
                        Chicken the Dog · 2w
                      </p>
                    </div> </a
                  ><a
                    class="dropdown-item text-center small text-gray-500"
                    href="#"
                    >Show All Alerts</a
                  >
                </div>
              </div>
              <div
                class="shadow dropdown-list dropdown-menu dropdown-menu-end"
                aria-labelledby="alertsDropdown"
              ></div>
            </li>
            <div class="d-none d-sm-block topbar-divider"></div>
            <li class="nav-item dropdown no-arrow">
              <div class="nav-item dropdown no-arrow">
                <a
                  class="dropdown-toggle nav-link"
                  aria-expanded="false"
                  data-bs-toggle="dropdown"
                  href="#"
                  ><span class="d-none d-lg-inline me-2 text-gray-600 small"
                    >Valerie Luna</span
                  ><img
                    class="border rounded-circle img-profile"
                    src="@/assets/img/avatars/avatar1.jpeg"
                /></a>
                <div
                  class="dropdown-menu shadow dropdown-menu-end animated--grow-in"
                >
                  <a class="dropdown-item" href="#"
                    ><i class="fas fa-user fa-sm fa-fw me-2 text-gray-400"></i
                    >&nbsp;Profile</a
                  ><a class="dropdown-item" href="#"
                    ><i class="fas fa-cogs fa-sm fa-fw me-2 text-gray-400"></i
                    >&nbsp;Settings</a
                  ><a class="dropdown-item" href="#"
                    ><i class="fas fa-list fa-sm fa-fw me-2 text-gray-400"></i
                    >&nbsp;Activity log</a
                  >
                  <div class="dropdown-divider"></div>
                  <a class="dropdown-item" href="#"
                    ><i
                      class="fas fa-sign-out-alt fa-sm fa-fw me-2 text-gray-400"
                    ></i
                    >&nbsp;Logout</a
                  >
                </div>
              </div>
            </li>
          </ul>
        </div>
      </nav>
      <div class="container-fluid">
        <div class="d-sm-flex justify-content-between align-items-center mb-4">
          <h3 class="text-dark mb-0">ホーム</h3>
        </div>
        <div class="row">
          <div class="col-md-6 col-xl-3 mb-4">
            <div class="card shadow-sm border-start-primary py-2">
              <div class="card-body">
                <div class="row align-items-center">
                  <div class="col-auto">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="1em"
                      height="1em"
                      fill="currentColor"
                      viewBox="0 0 16 16"
                      class="bi bi-file-text fa-2x text-gray-300"
                    >
                      <path
                        d="M5 4a.5.5 0 0 0 0 1h6a.5.5 0 0 0 0-1H5zm-.5 2.5A.5.5 0 0 1 5 6h6a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5zM5 8a.5.5 0 0 0 0 1h6a.5.5 0 0 0 0-1H5zm0 2a.5.5 0 0 0 0 1h3a.5.5 0 0 0 0-1H5z"
                      ></path>
                      <path
                        d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2zm10-1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1z"
                      ></path>
                    </svg>
                  </div>
                  <div class="col">
                    <div class="text-uppercase text-primary">
                      <router-link to="/news" class="text-decoration-none">
                        <span>お知らせ</span>
                      </router-link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-6 col-xl-3 mb-4">
            <div class="card shadow-sm border-start-primary py-2">
              <div class="card-body">
                <div class="row align-items-center">
                  <div class="col-auto">
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
                      class="icon icon-tabler icon-tabler-building-church fa-2x text-gray-300"
                    >
                      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                      <line x1="3" y1="21" x2="21" y2="21"></line>
                      <path d="M10 21v-4a2 2 0 0 1 4 0v4"></path>
                      <line x1="10" y1="5" x2="14" y2="5"></line>
                      <line x1="12" y1="3" x2="12" y2="8"></line>
                      <path d="M6 21v-7m-2 2l8 -8l8 8m-2 -2v7"></path>
                    </svg>
                  </div>
                  <div class="col">
                    <div class="text-uppercase text-primary">
                      <span>教会案内</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-6 col-xl-3 mb-4">
            <div class="card shadow-sm border-start-primary py-2">
              <div class="card-body">
                <div class="row align-items-center">
                  <div class="col-auto">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 512 512"
                      width="1em"
                      height="1em"
                      fill="currentColor"
                      class="fa-2x text-gray-300"
                    >
                      <!--! Font Awesome Free 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2022 Fonticons, Inc. -->
                      <path
                        d="M495.9 132.2C505.8 137.9 512 148.5 512 160V480C512 497.7 497.7 512 480 512C462.3 512 448 497.7 448 480V178.6L256 68.86L64 178.6V480C64 497.7 49.67 512 32 512C14.33 512 0 497.7 0 480V160C0 148.5 6.153 137.9 16.12 132.2L240.1 4.216C249.1-1.405 262-1.405 271.9 4.216L495.9 132.2zM216 168C216 145.9 233.9 128 256 128C278.1 128 296 145.9 296 168C296 190.1 278.1 208 256 208C233.9 208 216 190.1 216 168zM224 512C210.7 512 200 501.3 200 488V313.5L173.1 363.4C166.8 375 152.3 379.4 140.6 373.1C128.1 366.8 124.6 352.3 130.9 340.6L168.7 270.3C184.1 241.8 213.9 223.1 246.2 223.1H265.8C298.1 223.1 327.9 241.8 343.3 270.3L381.1 340.6C387.4 352.3 383 366.8 371.4 373.1C359.7 379.4 345.2 375 338.9 363.4L312 313.5V488C312 501.3 301.3 512 288 512C274.7 512 264 501.3 264 488V400H248V488C248 501.3 237.3 512 224 512V512z"
                      ></path>
                    </svg>
                  </div>
                  <div class="col">
                    <div class="text-uppercase text-primary">
                      <span>礼拝情報</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-6 col-xl-3 mb-4">
            <div class="card shadow-sm border-start-primary py-2">
              <div class="card-body">
                <div class="row align-items-center">
                  <div class="col-auto">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-door-closed" viewBox="0 0 16 16">
  <path d="M3 2a1 1 0 0 1 1-1h8a1 1 0 0 1 1 1v13h1.5a.5.5 0 0 1 0 1h-13a.5.5 0 0 1 0-1H3V2zm1 13h8V2H4v13z"/>
  <path d="M9 9a1 1 0 1 0 2 0 1 1 0 0 0-2 0z"/>
</svg>
                  </div>
                  <div class="col">
                    <div class="text-uppercase text-primary">
                      <span>部室</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col">
            <div class="card shadow mb-4">
              <div
                class="card-header d-flex justify-content-between align-items-center"
              >
                <h6 class="text-primary fw-bold m-0">新着情報</h6>
                <div class="dropdown no-arrow">
                  <button
                    class="btn btn-link btn-sm dropdown-toggle"
                    aria-expanded="false"
                    data-bs-toggle="dropdown"
                    type="button"
                  >
                    <i class="fas fa-ellipsis-v text-gray-400"></i>
                  </button>
                  <div
                    class="dropdown-menu shadow dropdown-menu-end animated--fade-in"
                  >
                    <p class="text-center dropdown-header">dropdown header:</p>
                    <a class="dropdown-item" href="#">&nbsp;Action</a
                    ><a class="dropdown-item" href="#">&nbsp;Another action</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="#"
                      >&nbsp;Something else here</a
                    >
                  </div>
                </div>
              </div>
              <div class="card-body" style="padding-bottom: 0">
                <div class="row">
                  <div class="col">
                    <div
                      class="card text-bg-secondary border-start-primary py-2"
                      style="margin-bottom: 20px"
                    >
                      <div class="card-body">
                        <div class="row align-items-center">
                          <div class="col">
                            <div class="text-uppercase text-primary">
                              <h5>青年部からのメッセージ</h5>
                              <p>メッセージ</p>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div
                      class="card text-bg-secondary border-start-primary py-2"
                      style="margin-bottom: var(--bs-card-spacer-x)"
                    >
                      <div class="card-body">
                        <div class="row align-items-center">
                          <div class="col">
                            <div class="text-uppercase text-primary">
                              <h5>メディア伝道部からのメッセージ</h5>
                              <p>メッセージ</p>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <footer class="bg-white sticky-footer">
      <div class="container my-auto">
        <div class="text-center my-auto copyright">
          <span>Copyright © Brand 2023</span>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'AppHomeView',
  computed: {},
}
</script>

<style scoped></style>
