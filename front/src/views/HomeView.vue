<template>
  <div class="home" @scroll="onScroll">
    <header class="text-center d-flex justify-content-center align-items-center pt-5 w-100" :style="`${jambotron}`">
      <div class="container d-flex flex-column align-items-center" style="
          height: 50%;
          background: linear-gradient(
              90deg,
              rgba(0, 0, 0, 0) 0%,
              rgba(0, 0, 0, 0.63) 35%,
              rgba(0, 0, 0, 0.66) 62%,
              rgba(255, 255, 255, 0) 100%
            ),
            rgba(27, 27, 27, 0);
        ">
        <div class="col d-flex">
          <div class="row">
            <div class="col d-flex align-items-center">
              <h3 class="text-light text-shadow mb-0" style="font-family: 'M PLUS Rounded 1c', sans-serif">
                セブンスデー・アドベンチスト天沼教会
              </h3>
            </div>
          </div>
        </div>
        <div class="col d-flex">
          <div class="row">
            <div class="col">
              <h1 class="text-light text-shadow" style="font-family: 'M PLUS Rounded 1c', sans-serif">
                あたたかな開かれた教会
              </h1>
            </div>
          </div>
        </div>
        <div class="col d-flex">
          <div class="row">
            <div class="col">
              <h2 class="text-light text-shadow" style="font-family: 'M PLUS Rounded 1c', sans-serif">
                Since1914
              </h2>
            </div>
          </div>
        </div>
      </div>
    </header>
    <section>
      <youtube-thumbnails>
      </youtube-thumbnails>
      <div class="container pb-2 pt-2 mt-4" style="
          margin-right: 0;
          background: rgba(255, 209, 141, 0.46);
          margin-left: 0;
          width: 100%;
          display: block;
          max-width: none;
        ">
        <div class="row">
          <div class="col">
            <h3 class="text-white d-flex d-lg-flex justify-content-center text-shadow"
              style="font-family: 'M PLUS 1', sans-serif">
              インスタグラム
            </h3>
          </div>
        </div>
        <div class="row gy-3 row-cols-1 row-cols-md-2 row-cols-lg-3 pb-4 instagram">
          <div class="col" style="height: 250px">
            <a href="#">
              <img class="rounded img-fluid shadow w-100 fit-cover img-thumbnail" src="@/assets/img/insta3.jpg" />
            </a>
            <div class="image-description rounded-bottom px-2">
              <p>
                今週の安息日学校の教科研究は第8課「貪欲に対する警告」です。担当は東清志牧師になります。
              </p>
            </div>
          </div>
          <div class="col d-none d-sm-none d-md-block" style="height: 250px">
            <a href="#">
              <img class="rounded img-fluid shadow w-100 fit-cover img-thumbnail" src="@/assets/img/insta2.jpg"
                style="height: 250px" />
            </a>
            <div class="image-description rounded-bottom px-2">
              <p>
                今週の安息日学校の教科研究は第8課「貪欲に対する警告」です。担当は東清志牧師になります。
              </p>
            </div>
          </div>
          <div class="col d-none d-sm-none d-md-none d-lg-block" style="height: 250px">
            <a href="#">
              <img class="rounded img-fluid shadow w-100 fit-cover img-thumbnail" src="@/assets/img/insta1.jpg"
                style="height: 250px" />
            </a>
            <div class="image-description rounded-bottom px-2">
              <p>
                今週の安息日学校の教科研究は第8課「貪欲に対する警告」です。担当は東清志牧師になります。
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="news-section mt-2" ref="section">
      <div class="container full-width py-4" id="news-container" style="background-color: rgba(255, 217, 190, 0.52)">
        <div class="row d-flex mx-auto pb-4 mb-4 news shadow">
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
                  <span style="color: rgb(119, 119, 119)">天沼教会主任牧師 近藤光顕</span>
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
          <div class="col-12 col-lg-5 d-flex justify-content-md-center m-lg-auto pt-4">
            <img class="img-thumbnail img-fluid" src="@/assets/img/turky.jpg" loading="lazy" />
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
        <div class="row d-lg-flex justify-content-lg-center">
          <div class="col text-center d-lg-flex justify-content-lg-center">
            <a class="btn btn-primary shadow" href="News.html" role="button">さらに記事を見る</a>
          </div>
        </div>
      </div>
    </section>
    <section class="py-4 py-xl-5">
      <div class="container py-4 px-4 shadow warship-card">
        <div class="row gy-4 gy-md-0">
          <div class="col">
            <div class="row">
              <div class="col rounded pt-2" style="background-color: var(--bs-green); color: white">
                <h3 class="fw-bold">2023年3月4日（土） No.9日（土）&nbsp;</h3>
              </div>
            </div>
            <div class="row">
              <div class="col offset-md-1 mt-2">
                <div class="row">
                  <div class="col-12 col-sm-12 col-md-6 col-lg-auto">
                    <span class="fs-4 text-primary">教課研究</span>
                    <p class="fw-normal text-muted">
                      &nbsp;2023年 第1期 9課<br />「貪欲に対する警告」
                    </p>
                  </div>
                  <div class="col-12 col-sm-12 col-md-6 col-lg-auto">
                    <span class="fs-4 text-primary">説教</span>
                    <p class="fw-normal text-muted">
                      &nbsp;｢隅のかしら石か、さまたげの石か｣<br />
                      東 清志 天沼教会副牧師
                    </p>
                  </div>
                  <div class="col-12 col-sm-12 col-md-12 col-lg-auto">
                    <span class="fs-4 text-primary">聖書朗読</span>
                    <p class="fw-normal text-muted">
                      &nbsp;マルコによる福音書 11章27～33節&nbsp;
                    </p>
                  </div>
                </div>
                <div class="row">
                  <div class="col-12 col-sm-12">
                    <span class="fs-4 text-primary">心のマナ</span>
                    <p class="fw-normal text-muted">
                      「あなたがたは、ただ万軍の主を聖として、彼をかしこみ、彼を恐れなければならない。主はイスラエルの二つの家には聖所となり、またさまたげの石、つまずきの岩となり、エルサレムの住民には網となり、わなとなる。多くの者はこれにつまずき、かつ倒れ、破られ、わなにかけられ、捕えられる。」イザヤ書8章
                      13～15節
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="py-4">
      <div class="container">
        <div class="bg-info border rounded border-0 border-primary overflow-hidden">
          <div class="row g-0">
            <div class="col-md-6 d-flex flex-column justify-content-center">
              <div class="text-white p-4 p-md-5">
                <h2 class="fw-bold text-white mb-3 text-shadow">教会情報</h2>
                <ul class="list-group my-4">
                  <li class="list-group-item text-nowrap justify-content-between">
                    <div class="row">
                      <div class="col">
                        <span class="justify-content-lg-start">安息日学校</span>
                      </div>
                      <div class="col">
                        <span class="justify-content-end">9:30-10:40</span>
                      </div>
                    </div>
                  </li>
                  <li class="list-group-item text-nowrap justify-content-between">
                    <div class="row">
                      <div class="col">
                        <span class="justify-content-lg-start">教会発表</span>
                      </div>
                      <div class="col">
                        <span class="justify-content-end">10:40-11:00</span>
                      </div>
                    </div>
                  </li>
                  <li class="list-group-item text-nowrap justify-content-between">
                    <div class="row">
                      <div class="col">
                        <span class="justify-content-lg-start">礼拝</span>
                      </div>
                      <div class="col">
                        <span class="justify-content-end">11:00-12:00</span>
                      </div>
                    </div>
                  </li>
                </ul>
                <p class="mb-4">
                  当教会の礼拝（毎週土曜・１１時）には、毎週300名を超える方々が集い、聖歌隊とパイプオルガンのリードのもと、共に讃美歌を歌い、心を豊かにする慰めと励ましに満ちた聖書の言葉を聞くことができます。ぜひお出かけ下さい
                </p>
                <div class="row">
                  <div class="col text-center d-lg-flex justify-content-lg-end">
                    <a class="btn btn-primary me-2 mt-2" role="button" href="worship">詳細</a>
                  </div>
                  <div class="col d-lg-flex justify-content-lg-start">
                    <a class="btn btn-light mt-2" role="button" href="#">マップ</a>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-12 col-md-6 d-flex justify-content-center align-items-center order-first order-md-last"
              style="min-height: 250px">
              <div class="fit-contain pt-5 pt-md-0 rounded" style="
                  min-width: 417.5px;
                  height: 434.5px;
                  background-size: cover;
                " :style="`${backgroundImage2} no-repeat`"></div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="py-4" style="
        background: linear-gradient(
            90deg,
            rgba(255, 255, 255, 0) 1%,
            rgba(255, 247, 205, 0.62) 22%,
            rgba(255, 247, 205, 0.62) 81%,
            rgba(255, 255, 255, 0) 100%
          ),
          rgba(255, 243, 221, 0);
      ">
      <div class="container justify-content-lg-center">
        <div class="row">
          <div class="col pb-4">
            <div class="row d-flex rounded">
              <div
                class="col fs-4 d-flex d-lg-flex justify-content-center align-items-lg-center justify-content-xl-center">
                <span class="text-center text-light text-shadow">礼拝説教をポッドキャスト(音声のみ）でお聞きになれます。</span>
              </div>
            </div>
          </div>
        </div>
        <div class="row d-flex justify-content-center mb-4">
          <a class="col-10 col-sm-9 col-md-8 col-lg-5 p-2 rounded linear-bg spotify-a btn">
            <div class="row rounded">
              <div class="col d-lg-flex align-items-lg-center justify-content-xl-end">
                <div class="text-white p-1">
                  <span class="fs-3">Spotify</span>
                </div>
              </div>
              <div class="col d-flex justify-content-end justify-content-xl-start">
                <img src="@/assets/img/spotify-2.svg" style="
                    width: 49px;
                    filter: brightness(0%) contrast(100%) hue-rotate(140deg)
                      invert(93%) saturate(100%) sepia(100%);
                  " />
              </div>
            </div>
          </a>
        </div>
        <div class="row d-xl-flex justify-content-center mb-4">
          <div class="col-10 col-sm-9 col-md-8 col-lg-5 p-2 rounded anchor-a">
            <div class="row rounded">
              <div class="col d-lg-flex align-items-lg-center justify-content-xl-end">
                <div class="text-white p-1"><span class="fs-3">Anchor</span></div>
              </div>
              <div class="col d-flex justify-content-end justify-content-xl-start">
                <img src="@/assets/img/Anchor_2021_logo.svg" style="
                    width: 120px;
                    filter: brightness(0%) contrast(100%) hue-rotate(140deg)
                      invert(93%) saturate(100%) sepia(100%);
                  " />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="py-4 py-xl-5">
      <div class="container">
        <div
          class="text-white bg-primary border rounded border-0 border-primary d-flex flex-column justify-content-between flex-lg-row p-4 p-md-5">
          <h5 class="fw-bold">
            ご意見、ご質問、メッセージ等々お気軽にお問い合わせください。
          </h5>
          <div class="my-2">
            <a class="btn btn-light fs-5 py-2 px-4" role="button" href="contacts.html">お問い合わせ</a>
          </div>
        </div>
      </div>
    </section>
    <footer>
      <div class="container py-4 py-lg-5">
        <div class="row row-cols-2 row-cols-md-4">
          <div class="col-12 col-md-3">
            <div class="fw-bold d-flex align-items-center mb-2">
              <span>ブランド</span>
            </div>
            <p class="text-muted">Made by Yugo Harago</p>
          </div>
          <!-- TODO: リンクを追加する -->
          <!-- <div class="col-sm-4 col-md-3 text-lg-start d-flex flex-column">
            <h3 class="fs-6 fw-bold">リンク</h3>
            <ul class="list-unstyled">
              <li><a disabled>SDA</a></li>
              <li><a>医療事業</a></li>
              <li><a>福祉事業</a></li>
              <li><a>教育事業</a></li>
              <li><a>地域の情報</a></li>
            </ul>
          </div>
          <div class="col-sm-4 col-md-3 text-lg-start d-flex flex-column">
            <h3 class="fs-6 fw-bold">プライバシーポリシー</h3>
            <ul class="list-unstyled">
              <li><a>Google アナリティクスの補足</a></li>
              <li><a>reCAPTCHA</a></li>
            </ul>
          </div>
          <div class="col-sm-4 col-md-3 text-lg-start d-flex flex-column">
            <h3 class="fs-6 fw-bold">活動支援</h3>
            <ul class="list-unstyled">
              <li><a>一緒に働きませんか？</a></li>
              <li><a>教会献金</a></li>
              <li><a>IT献金</a></li>
            </ul>
          </div> -->
        </div>
        <hr />
        <div class="text-muted d-flex justify-content-between align-items-center pt-3">
          <p class="mb-0">Copyright © 2023 天沼教会コミュニケーション部</p>
          <ul class="list-inline mb-0">
            <li class="list-inline-item">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                class="bi bi-facebook">
                <path
                  d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z">
                </path>
              </svg>
            </li>
            <!-- <li class="list-inline-item">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                class="bi bi-twitter">
                <path
                  d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z">
                </path>
              </svg>
            </li> -->
            <li class="list-inline-item">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                class="bi bi-instagram">
                <path
                  d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z">
                </path>
              </svg>
            </li>
          </ul>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import { useScrollEvent } from '../events/scrollEvent';
import { useHeaderStore } from '@/stores/header';
import YoutubeThumbnails from '@/components/YoutubeThumbnails.vue';

export default {
  name: 'AppHomeView',
  components: {
    YoutubeThumbnails
  },
  created() {
    const headerStore = useHeaderStore();
    useScrollEvent(scrollY => {
      const isVisible = scrollY >= 780;
      headerStore.backgroundColor = isVisible ? 'black' : 'transparent';
    });
  },
  computed: {
    jambotron() {
      const images = import.meta.globEager('@/assets/img/janbotron.jpg');
      const imageUrl = Object.values(images)[0].default;
      return `background: url(${imageUrl}) center / cover; height: 353pt;`;
    },
    backgroundImage2() {
      const images = import.meta.globEager('@/assets/img/image.jpg');
      const imageUrl = Object.values(images)[0].default;
      return `background: url(${imageUrl}) center / cover;`;
    },
  }
}
</script>

<style scoped lang="scss">
@import '../styles/styles.scss';

.home {
  background: linear-gradient(#f67273, #ffc368 99%), #f98a6b !important;
}
</style>
