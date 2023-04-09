<template>
  <div id="header-margin" style="height: 55px"></div>
  <section class="news-section">
    <div class="container">
      <header class="text-center pt-4 w-100">
        <div class="container">
          <div class="col">
            <div class="row">
              <div class="col">
                <h1
                  class="text-primary text-shadow"
                  style="font-family: 'M PLUS Rounded 1c', sans-serif"
                >
                  天沼教会ニュース
                </h1>
              </div>
            </div>
          </div>
        </div>
      </header>
    </div>
    <div
      class="container full-width pt-5 border-top border-bottom"
      id="news-container"
      style="background-color: #fff8e6"
    >
      <div class="row d-flex mx-auto pb-4 mb-4 news">
        <div class="col-lg-7 h-100">
          <div class="row">
            <div class="col">
              <div><span class="badge bg-primary mb-2">2023/1/14</span></div>
            </div>
          </div>
          <div class="row">
            <div class="col">
              <h5 class="fs-3 fw-bold mb-4">
                <strong>トルコ・シリア大地震</strong>
              </h5>
              <p class="text-muted">
                この度のトルコ・シリア大地震で被災された方々へ、心からのお見舞いを申し上げます。救援活動に携わる皆様が守られて、一人でも多くの人々の命が助かりますよう、また被災された皆様と、関係の皆様に天来の慰めがありますようお祈り申し上げます。NPO法人ADRAJapanによる、トルコ・シリア大地震被災者支援が開始されました。皆様からのご支援をお願い申し上げます。&nbsp;
              </p>
              <span class="d-flex justify-content-lg-end author">
                <br />
                <span style="color: rgb(119, 119, 119)"
                  >天沼教会主任牧師 近藤光顕</span
                >
              </span>
            </div>
          </div>
          <div class="row d-none d-lg-flex" id="large-link">
            <div class="col">
              <ul class="list-group mt-2">
                <li class="list-group-item btn btn-primary mb-2">
                  ADRA Japanのホームページ
                </li>
                <li class="list-group-item btn btn-primary mb-2">
                  支援に関するお知らせ
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div
          class="col-12 col-lg-5 d-flex justify-content-md-center m-lg-auto pt-4"
        >
          <div class="row">
            <div class="col">
              <img
                class="img-thumbnail img-fluid"
                src="@/assets/img/turky.jpg"
                loading="lazy"
              />
            </div>
          </div>
        </div>
        <div class="col-lg-7 d-lg-none">
          <div class="row" id="small-link">
            <div class="col">
              <ul class="list-group mt-2">
                <li class="list-group-item btn btn-primary mb-2">
                  ADRA Japanのホームページ
                </li>
                <li class="list-group-item btn btn-primary mb-2">
                  支援に関するお知らせ
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="row d-flex mx-auto pb-4 mb-4 news reverse">
        <div class="col-lg-7 h-100">
          <div class="row">
            <div class="col">
              <div><span class="badge bg-primary mb-2">2023/1/14</span></div>
            </div>
          </div>
          <div class="row">
            <div class="col">
              <h5 class="fs-3 fw-bold mb-4">安息日学校および礼拝について</h5>
              <p class="text-muted">
                現在、安息日プログラムは対面での礼拝参加を再開しています。ただ、依然としてコロナ感染状況が続いておりますので、密を避けるため参加人数を150名に制限して行います。このため体調のすぐれない方や配信でもご参加できる方はご無理なさらず、引き続き配信にてご参加くださいますようお願いいたします。
              </p>
              <span class="d-flex justify-content-lg-end author">
                <br />
                <span style="color: rgb(119, 119, 119)"
                  >天沼教会主任牧師 近藤光顕</span
                >
              </span>
            </div>
          </div>
          <div class="row d-none d-lg-flex" id="large-link-1">
            <div class="col">
              <ul class="list-group mt-2">
                <li class="list-group-item btn btn-primary mb-2">
                  ADRA Japanのホームページ
                </li>
                <li class="list-group-item btn btn-primary mb-2">
                  支援に関するお知らせ
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div
          class="col-12 col-lg-5 text-center d-flex justify-content-sm-center justify-content-md-center order-lg-first m-lg-auto my-4 pt-4"
        >
          <div class="row">
            <div class="col">
              <img
                class="img-thumbnail img-fluid"
                src="@/assets/img/YuRun_Church_Illustration_Adobe_Illustrator_simple_3D_7a605d24-141a-445a-b275-817200189b74.png"
                loading="lazy"
              />
            </div>
          </div>
        </div>
        <div class="col-lg-7 d-lg-none">
          <div class="row" id="small-link-1">
            <div class="col">
              <ul class="list-group mt-2">
                <li class="list-group-item btn btn-primary mb-2">
                  ADRA Japanのホームページ
                </li>
                <li class="list-group-item btn btn-primary mb-2">
                  支援に関するお知らせ
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'NewsView',
}
</script>
