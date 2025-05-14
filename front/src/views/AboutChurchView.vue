<style>
html {
  scrollbar-color: #0492c1 #013173;
}

body {
  margin: 0;
  padding: 0;
  background-color: #000;
  overflow-x: hidden;
  background: linear-gradient(to bottom, #013173, #F09457);
}

.content-wrapper {
  max-width: 800px;
  margin: 0 auto;
}

.space {
  height: 100vh;
}

.section-1 {
  height: 100vh;
  background-color: #013173;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: white;
  position: relative;
  overflow: hidden;
  padding: 2rem;
  text-align: center;
}

.section-1-text h1 {
  font-size: 4rem;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
  z-index: 1;
  margin-bottom: 1.5rem;
  animation: fadeIn 2s ease-in forwards;
}

.section-1-text p {
  font-size: 1.5rem;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
  z-index: 1;
  max-width: 800px;
  line-height: 1.6;
  margin: 0;
  opacity: 0;
  animation: fadeIn 2s ease-in forwards;
  animation-delay: 0.5s;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.section-2 {
  position: relative;
  background: linear-gradient(180deg, #013173 50%, #F09457 50%);
}

#mountain-1 {
  --mountain-index: 1;
}

#mountain-2 {
  --mountain-index: 2;
}

#mountain-3 {
  --mountain-index: 3;
}

#mountain-4 {
  --mountain-index: 4;
}

#mountain-5 {
  --mountain-index: 5;
}

#mountain-6 {
  --mountain-index: 6;
}

.mountains {
  height: 60vh;
  position: relative;
}

.mountain {
  --total-mountains: 6;
  animation: move-up linear forwards;
  animation-timeline: view();
  animation-range: 30%;
}

@keyframes move-up {
  0% {
    transform: translateY(0);
  }

  100% {
    transform: translateY(calc(var(--mountain-index) * -8%));
  }
}

.stars {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
}

#stars-behind-mountains {
  z-index: 1;
}

.section-2 svg {
  position: relative;
  z-index: 1;
  view-timeline-name: --clouds;
}

.star {
  position: absolute;
  animation: twinkle var(--duration) infinite;
  animation-delay: var(--delay);
  opacity: 0;
}

.star svg {
  width: var(--size);
  height: var(--size);
  filter: drop-shadow(0 0 2px rgba(255, 255, 255, 0.8));
}

@keyframes twinkle {

  0%,
  100% {
    opacity: 0;
    transform: scale(0.8);
  }

  50% {
    opacity: var(--opacity);
    transform: scale(1.2);
  }
}

.cloud-wrapper {
  background-color: #F09457;
  position: relative;
  height: 1px;
  view-timeline-name: --wrapper;
  view-timeline-axis: block;
  z-index: 2;
}

.clouds {
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
}

.cloud {
  transform: translateX(-100%);
  position: absolute;
}

#cloud-1 {
  animation: moveCloudLeft linear forwards;
  animation-timeline: --wrapper;
  animation-range: 10% 50%;
}

#cloud-2 {
  animation: moveCloudRight linear forwards;
  animation-timeline: --wrapper;
  animation-range: 10% 50%;
}

#cloud-3 {
  animation: moveCloudLeft linear forwards;
  animation-timeline: --wrapper;
  animation-range: 10% 50%;
}


@keyframes moveCloudLeft {
  0% {
    transform: translateX(-20px);
  }

  100% {
    transform: translateX(calc(100% + 70px));
  }
}

@keyframes moveCloudRight {
  0% {
    transform: translateX(calc(100% + 70px));
  }

  100% {
    transform: translateX(-20px);
  }
}

.spacer-section-2 {
  height: 70vh;
}

#section-2-text {
  position: relative;
  z-index: 2;
  padding: 2rem;
  margin-top: -60vh;
}

#section-2-text p {
  color: white;
  font-size: 1.5rem;
  line-height: 1.6;
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
  animation: fadeIn linear forwards;
  animation-timeline: view();
  animation-range: entry;
}

.section-3 {
  z-index: 3;
  position: relative;
  background: linear-gradient(180deg, #F09457 50%, #d2995f);
  height: 600px;
}

.station {
  position: absolute;
  width: 100%;
}

.building {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  opacity: 0;
  animation: showBuilding linear forwards;
  animation-timeline: view();
}

#BackBuildings {
  --index: 1;
  z-index: 1;
  animation-range: entry 0% entry 100%;
}

#FrontBuildings {
  --index: 2;
  z-index: 2;
  animation-range: entry 50% entry 100%;
}

#BusStation {
  --index: 3;
  z-index: 3;
  animation-range: entry 80% entry 100%;
}

#Bus {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  opacity: 0;
  z-index: 4;
  animation: busAnimation linear forwards;
  animation-timeline: view();
  animation-range: contain;
}

@keyframes showBuilding {
  from {
    transform: translateY(calc(var(--index) * 100px));
    opacity: 0;
  }

  to {
    transform: translateY(0);
    opacity: 1;
  }
}

@keyframes busAnimation {
  from {
    transform: translateX(-500px);
    opacity: 0.8;
  }

  to {
    transform: translateX(0);
    opacity: 1;
  }
}

.section-4 {
  z-index: 4;
  position: relative;
  height: 600px;
  view-timeline-name: --signal-section;
  view-timeline-axis: block;
}

.footpath {
  position: relative;
}

.footpath img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1;
}

.footpath svg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 2;
}

.signal {
  z-index: 2;
  opacity: 1;
  animation: signalAnimation linear forwards;
  animation-timeline: --signal-section;
}

#signal-1 {
  animation-range: contain 50% exit 100%;
}

#signal-2 {
  animation-range: contain 10% contain 50%;
}

#signal-3 {
  opacity: 0;
  animation-range: entry 0% contain 10%;
}

@keyframes signalAnimation {
  0% {
    opacity: 1;
  }

  1% {
    opacity: 0;
  }

  99% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

.text-section-4 {
  position: absolute;
  top: 30%;
  left: 20%;
  width: 75%;
  height: 100%;
  z-index: 2;
  font-size: 24px;
  line-height: 1.5;
  color: #fff;
}

.text-section-4 p {
  text-align: center;
  background-color: #000000bb;
  animation: fadeIn linear forwards;
  animation-timeline: --signal-section;
  animation-range: entry;
}

.section-5 {
  z-index: 5;
  position: relative;
  height: 1150px;
  background-color: #924e20;
}

.text-section-5 {
  position: absolute;
  top: 10%;
  left: 12%;
  width: 75%;
  height: 100%;
  color: #fff;
  font-size: clamp(24px, 4vw, 48px);
  z-index: 7;
  transform: perspective(1000px) rotateX(30deg);

}

.text-section-5 p {
  text-align: center;
  background-color: #000000bb;
  animation: fadeIn linear forwards;
  animation-timeline: --signal-section;
  animation-range: entry;
}

.commerce-street img {
  position: absolute;
  top: 0;
  left: 0;
}

.commerce-street-buildings {
  width: 100%;
  transform: translateY(200px);
  animation: showCommerceStreet linear forwards;
  animation-timeline: view();
  animation-range: entry;
}

#building-1 {
  animation-range: entry 0% entry 25%;
}

#building-2 {
  animation-range: entry 25% entry 50%;
}

#building-3 {
  animation-range: entry 50% entry 75%;
}

#building-4 {
  animation-range: entry 75% entry 100%;
}

@keyframes showCommerceStreet {
  from {
    transform: translateY(200px);
  }

  to {
    transform: translateY(0);
  }
}

.section-6 {
  position: relative;
  height: 797px;
  view-timeline-name: --section-6;
  background: linear-gradient(180deg, #e09d70 50%, #c24212 50%);
}

.section-6 img {
  position: absolute;
}

#hospital {
  animation: hospitalAnimation linear forwards;
  animation-range: entry;
  animation-timeline: view();
}

@keyframes hospitalAnimation {
  from {
    transform: translateY(600px);
    opacity: 0;
  }

  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.hospital-tree-wrapper {
  position: relative;
  z-index: 3;
}

.Hospital-tree {
  position: absolute;
  width: 100%;
}

.section-6-text {
  z-index: 4;
  position: absolute;
  top: 10%;
  left: 12%;
  width: 75%;
  height: 100%;
  color: #fff;
  font-size: clamp(24px, 4vw, 48px);
}

.section-6-text p {
  text-align: center;
  background-color: #000000bb;
  animation: fadeIn linear forwards;
  animation-timeline: --signal-section;
  animation-range: entry;
}

.typewrite {
  display: inline-block;
  overflow: hidden;
  white-space: nowrap;
  animation: typing 1s steps(40, end) forwards;
  animation-timeline: view();
  animation-range: entry 100% contain 50%;
  opacity: 0;
}

.typewrite:nth-child(1) {
  animation-delay: 0s;
}

.typewrite:nth-child(3) {
  animation-delay: 1s;
}

.typewrite:nth-child(5) {
  animation-delay: 2s;
}

.typewrite:nth-child(7) {
  animation-delay: 3s;
}

.typewrite:nth-child(9) {
  animation-delay: 4s;
}

.typewrite:nth-child(11) {
  animation-delay: 5s;
}

.typewrite:nth-child(13) {
  animation-delay: 6s;
}

.typewrite:nth-child(15) {
  animation-delay: 7s;
}

.typewrite:nth-child(17) {
  animation-delay: 8s;
}

.typewrite:nth-child(19) {
  animation-delay: 9s;
}

.typewrite:nth-child(21) {
  animation-delay: 10s;
}

.typewrite:nth-child(23) {
  animation-delay: 11s;
}

.typewrite:nth-child(25) {
  animation-delay: 12s;
}

@keyframes typing {
  from {
    width: 0;
    opacity: 1;
  }

  to {
    width: 100%;
    opacity: 1;
  }
}

.section-7 {
  position: relative;
  height: 1200px;
  view-timeline-name: --section-7;
  background-color: #9b615b;
}

.section-7-text {
  z-index: 4;
  position: absolute;
  top: 10%;
  left: 12%;
  width: 75%;
  height: 100%;
  color: #fff;
  font-size: clamp(24px, 4vw, 48px);
}

.section-7-text p {
  text-align: center;
  background-color: #000000bb;
  animation: fadeIn linear forwards;
  animation-timeline: --section-7;
  animation-range: entry;
}

.church-outside img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
}

#church-outside {
  animation: goingIn linear forwards;
  animation-timeline: --section-7;
}

@keyframes goingIn {
  exit 0% {
    transform: scale(1);
    opacity: 1;
  }

  exit 16% {
    transform: scale(5) translateY(-213px);
    opacity: 1;
  }

  exit 17% {
    opacity: 0;
  }

  exit 100% {
    opacity: 0;
  }
}

@keyframes goingIn {
  exit 0% {
    transform: scale(1);
    opacity: 1;
  }

  exit 15% {
    opacity: 1;
  }

  exit 16% {
    transform: scale(5) translateY(-213px);
    opacity: 0;
  }

  exit 17% {
    opacity: 0;
  }

  exit 100% {
    opacity: 0;
  }
}

#transition-section-7-8 {
  position: absolute;
  opacity: 0;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #ffda8f;

  animation: transition linear forwards;
  animation-timeline: --section-7
}

@keyframes transition {
  exit 15% {
    opacity: 1;
    z-index: -1;
  }

  exit 16% {
    z-index: 99;
  }

  exit 99% {
    z-index: 99;
  }

  exit 100% {
    opacity: 1;
    z-index: -1;
  }
}

.section-8 {
  position: relative;
  height: 1490px;
  view-timeline-name: --section-8;
  background: linear-gradient(180deg, #ffda8f 50%, #ca5c13 50%);
}

.section-8-text {
  z-index: 4;
  position: absolute;
  top: 60%;
  left: 12%;
  width: 75%;
  color: #fff;
  font-size: clamp(24px, 4vw, 48px);
}

.section-8-text p {
  text-align: center;
  background-color: #000000bb;
  animation: fadeIn linear forwards;
  animation-timeline: --section-8;
  animation-range: entry;
}

.church-inside img {
  position: absolute;
  top: 0;
  left: 0;
  animation: curch-inside linear forwards;
  animation-timeline: --section-8;
  animation-range: entry
}

@keyframes curch-inside {
  0% {
    transform: translateY(0);
  }

  100% {
    transform: translateY(200px);
  }
}
</style>

<template>
  <div class="content-wrapper">
    <section class="section-1">
      <div class="section-1-text">
        <div ref="starsContainer" class="stars" id="stars"></div>
        <h1>天沼教会について</h1>
        <p>1896年にアメリカ人宣教師W.C.グレンジャーらが来日して東京で伝道を開始し、1899年には日本初のセブンスデー・アドベンチスト教会として「東京教会」が組織されました。<br>
          その後、1914年に現在地である東京・杉並区天沼の一帯に約3,320坪の土地を取得し、宣教本部や宣教師館、伝道学校などの施設とともに教会堂を建設しました。<br>
          1917年1月26日には天沼の地で教会堂の献堂式が行われ、当初は日本教団の本部教会として位置づけられました。<br>
          1919年に教会名を正式に「天沼教会」と改称し現在に至っています。</p>
      </div>
    </section>
    <section class="section-2">
      <div ref="starsBehindMountainsContainer" class="stars" id="stars-behind-mountains"></div>
      <div class="mountains">
        <svg width="100%" viewBox="0 0 789 1586" version="1.1" xmlns="http://www.w3.org/2000/svg"
          xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/"
          style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:2;">
          <rect id="Artboard1" x="0" y="0" width="788.889" height="1585.07" style="fill:none;" />
          <clipPath id="_clip1">
            <rect id="Artboard11" serif:id="Artboard1" x="0" y="0" width="788.889" height="1585.07" />
          </clipPath>
          <g clip-path="url(#_clip1)">
            <path
              d="M-100.781,375.39c-0,-11.461 24.733,-40.584 34.343,-50.194c10.784,-10.784 18.668,-28.487 33.022,-35.664c27.372,-13.686 80.132,-35.886 121.522,-30.38c56.263,7.485 115.836,65.161 125.484,75.29c21.995,23.096 71.925,47.835 118.88,38.306c20.077,-4.075 47.933,-24.911 54.156,-29.059c30.527,-20.352 53.796,-49.634 87.179,-60.761c51.155,-17.052 128.852,55.626 169.073,54.156c136.599,-4.99 183.069,-92.068 272.103,-47.552c11.933,5.967 -51.775,351.766 -51.775,351.766l-930.722,33.594l-33.265,-299.502Z"
              style="fill:#0492c1;" class="mountain" id="mountain-1" />
            <path
              d="M-26.604,924.629c0,0 -141.088,-462.889 -127.814,-480.587c41.572,-55.43 105.397,-75.29 171.715,-75.29c71.819,-0 144.685,42.429 203.417,80.574c36.698,23.835 90.216,33.969 132.088,40.947c41.118,6.853 95.06,-4.111 133.41,-18.492c27.107,-10.165 54.788,-18.895 81.895,-29.06c71.996,-26.998 148.122,-68.282 228.513,-56.798c103.419,14.774 61.034,561.71 61.034,561.71l-884.258,-23.004Z"
              style="fill:#a1d86b;" class="mountain" id="mountain-2" />
            <path
              d="M919.443,664.272c-28.712,7.178 -64.994,-0.301 -90.811,-13.209c-14.156,-7.079 -26.532,-19.852 -41.277,-24.767c-14.212,-4.737 -25.296,-21.641 -39.627,-26.418c-13.458,-4.486 -22.971,-23.617 -36.324,-28.068c-17.678,-5.893 -31.776,-20.499 -49.534,-26.418c-13.125,-4.375 -28.922,-7.031 -41.277,-13.209c-9.554,-4.777 -24.431,1.763 -34.673,-1.651c-8.087,-2.696 -23.92,-3.726 -31.372,-0c-7.345,3.672 -20.192,-0.974 -28.068,1.651c-18.488,6.162 -36.224,13.726 -54.487,19.813c-12.517,4.173 -32.722,17.862 -41.278,26.418c-4.852,4.853 -17.017,10.16 -23.115,13.209c-29.33,14.665 -54.261,39.514 -84.207,54.486c-16.057,8.029 -32.063,15.206 -47.882,23.116c-13.927,6.963 -32.032,6.109 -46.231,13.209c-14.88,7.44 -76.914,3.646 -90.811,-3.302c-17.289,-8.645 -40.995,-10.363 -59.44,-16.512c-51.495,-17.165 -150.276,-48.415 -203.086,-13.208c-10.459,6.972 3.322,581.345 3.322,581.345l1124.4,1.713l-84.226,-568.198Z"
              style="fill:#8de08b;" class="mountain" id="mountain-3" />
            <path
              d="M-27.221,1159.31c0,-0 -110.034,-314.366 -92.053,-333.064c38.92,-40.471 93.503,-67.045 147.94,-77.933c62.154,-12.431 106.46,28.847 159.827,50.194c15.026,6.01 30.743,4.828 46.231,7.925c7.065,1.413 16.464,2.784 23.776,1.321c29.008,-5.801 57.017,-11.282 85.858,-18.492c19.27,-4.818 36.591,-19.055 55.477,-23.776c6.2,-1.55 11.255,-7.767 17.171,-9.246c22.127,-5.532 60.599,-26.472 84.537,-18.493c20.815,6.939 41.163,10.711 60.761,23.776c24.317,16.212 43.97,40.043 72.649,51.515c25.504,10.201 48.695,14.06 75.29,18.492c25.555,4.259 55.803,-1.155 80.574,-5.283c45.741,-7.624 11.795,333.064 11.795,333.064l-829.833,-0Z"
              style="fill:#e7fd8b;" class="mountain" id="mountain-4" />
            <path
              d="M-46.952,926.013c19.564,-19.564 121.22,-27.597 147.564,-22.355c46.806,9.314 84.369,37.538 112.328,58.507c60.373,45.28 128.61,49.559 205.512,49.559c101.649,0 195.756,-39.714 290.595,-71.327c42.881,-14.294 85.664,-35.825 130.768,-42.269c46.731,-6.676 -50.926,519.214 -50.926,519.214l-788.889,-24.045l-46.952,-467.284Z"
              style="fill:#fcc164;" class="mountain" id="mountain-5" />
            <path
              d="M788.889,2071.55c-0,-0 72.221,-782.692 36.573,-826.989c-37.67,-46.81 -80.908,-144.467 -151.616,-145.954c-45.541,-0.958 -78.974,26.47 -118.043,44.156c-29.242,13.237 -62.975,19.742 -94.839,24.953c-41.783,6.832 -126.085,14.91 -166.025,-2.726c-34.442,-15.209 -76.996,-29.981 -113.647,-29.584c-55.219,0.599 -93.921,33.538 -163.447,65.55c-47.644,21.937 -145.822,98.884 -145.822,98.884l127.977,771.71l788.889,-0Z"
              style="fill:#f09457;" class="mountain" id="mountain-6" />
          </g>
        </svg>
      </div>
      <div class="spacer-section-2"></div>
      <div id="section-2-text">
        <p>
          その後も天沼教会は日本におけるアドベンチスト教会の中心的存在として発展を続け、1929年には同じ敷地内に東京衛生病院が開院し、医療伝道の拠点ともなりました。<br>
          第二次世界大戦中の宗教弾圧により一時教団の活動停止や財産接収などの困難を経験しましたが、戦後いち早く教会再建が図られます。1945年9月には安息日学校が再開し、1947年6月に信徒約300名で天沼教会が正式に再組織されました。<br>
          接収されていた教会資産も返還され、同年11月には東京衛生病院も営業を再開しています。
        </p>
      </div>
      <div class="cloud-wrapper">
        <div class="clouds">
          <svg viewBox="0 0 192 72" version="1.1" xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/"
            style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:2;">
            <path
              d="M0,25.756l-56.092,0c-0,0 -14.432,-8.552 -0.211,-15.033c-0,0 0.948,-11.421 12.536,-10.689c11.587,0.732 12.746,8.87 12.746,8.87c-0,-0 1.58,-3.187 4.53,-3.082c2.949,0.105 5.182,1.666 5.182,3.564c-0,0 5.523,-0.259 5.825,2.934c-0,0 6.558,0.345 6.3,4.142c-0,0 6.99,-0.733 6.99,3.193c-0,0 7.798,3.573 2.194,6.101Z"
              style="fill:url(#_Linear1);" class="cloud" id="cloud-1" />
            <path
              d="M0,30.784c0.782,-2.895 3.429,-5.028 6.57,-5.028c3.756,0 6.805,3.049 6.805,6.805c-0,0.168 -0.007,0.336 -0.019,0.502l0.019,-0c2.333,-0 4.227,1.894 4.227,4.227c-0,0.831 -0.241,1.606 -0.656,2.26c1.626,0.513 2.807,2.034 2.807,3.829c0,2.216 -1.799,4.014 -4.014,4.014l-29.49,0c-1.621,0 -2.938,-1.316 -2.938,-2.938c0,-1.622 1.317,-2.938 2.938,-2.938c0.058,-0 0.114,0.001 0.171,0.005c-0.112,-0.444 -0.171,-0.909 -0.171,-1.387c0,-3.139 2.549,-5.688 5.688,-5.688c0.152,0 0.304,0.007 0.453,0.018c-0.29,-0.572 -0.453,-1.219 -0.453,-1.904c-0,-2.333 1.894,-4.227 4.227,-4.227c1.699,-0 3.165,1.004 3.836,2.45Z"
              style="fill:url(#_Linear2);" class="cloud" id="cloud-2" />
            <path
              d="M0,71.522l-58.895,0c-0,0 -5.58,0.377 -6.2,-5.144c-0.686,-6.103 6.131,-8.092 10.109,-7.269c0,-0 -0.684,-8.005 7.458,-10.12c7.884,-2.048 11.111,6.292 11.111,6.292c-0,0 2.229,-4.886 7.372,-4.886c5.144,-0 7.167,4.389 7.03,6.172c-0,-0 11.35,-2.486 11.35,3.686c0,0 8.367,0.686 8.367,5.212c0,0 5.418,0.729 2.298,6.057Z"
              style="fill:url(#_Linear3);" class="cloud" id="cloud-3" />
            <defs>
              <linearGradient id="_Linear1" x1="0" y1="0" x2="1" y2="0" gradientUnits="userSpaceOnUse"
                gradientTransform="matrix(3.16066e-16,5.16175,-5.16175,3.16066e-16,162.489,20.5945)">
                <stop offset="0" style="stop-color:#fff;stop-opacity:1" />
                <stop offset="1" style="stop-color:#b3b3b3;stop-opacity:1" />
              </linearGradient>
              <linearGradient id="_Linear2" x1="0" y1="0" x2="1" y2="0" gradientUnits="userSpaceOnUse"
                gradientTransform="matrix(5.99313e-16,9.78752,-9.78752,5.99313e-16,18.1317,41.3448)">
                <stop offset="0" style="stop-color:#fff;stop-opacity:1" />
                <stop offset="1" style="stop-color:#b3b3b3;stop-opacity:1" />
              </linearGradient>
              <linearGradient id="_Linear3" x1="0" y1="0" x2="1" y2="0" gradientUnits="userSpaceOnUse"
                gradientTransform="matrix(9.31749e-16,15.2166,-15.2166,9.31749e-16,113.695,63.8195)">
                <stop offset="0" style="stop-color:#fff;stop-opacity:1" />
                <stop offset="1" style="stop-color:#b3b3b3;stop-opacity:1" />
              </linearGradient>
            </defs>
          </svg>
        </div>
      </div>
    </section>
    <section class="section-3">
      <div class="station">
        <div id="BackBuildings" class="building">
          <img src="@/assets/img/BackBuildings.svg" style="width: 100%;">
        </div>
        <div id="FrontBuildings" class="building">
          <img src="@/assets/img/FrontBuilding.svg" alt="Front Buildings" style="width: 100%;">
        </div>
        <div id="BusStation" class="building">
          <img src="@/assets/img/BusStation.svg" alt="Front Buildings" style="width: 100%;">
        </div>
        <div id="Bus">
          <img src="@/assets/img/Bus.svg" alt="Front Buildings" style="width: 100%;">
        </div>
      </div>
    </section>
    <section class="section-4">
      <div class="footpath">
        <svg width="100%" viewBox="0 0 800 620">
          <circle cx="289.428" cy="39.221" r="20" style="fill:#d5d5d5;" class="signal" id="signal-1" />
          <circle cx="335.53" cy="39.221" r="20" style="fill:#d5d5d5;" class="signal" id="signal-2" />
          <circle cx="380.893" cy="39.221" r="20" style="fill:#d5d5d5;" class="signal" id="signal-3" />
        </svg>
        <img src="@/assets/img/footpath.svg" alt="Footpath" style="width: 100%;">
      </div>
      <div class="text-section-4">
        <p>
          天沼教会の会堂は時代と共に整備・拡張されてきました。1959年には教会堂の移設・改築を行い、1983年7月には現在使用している新会堂を新築献堂しました。<br>
          現在の会堂は収容人数も増え、パイプオルガンなど充実した設備を備えています。2012年時点で教会員数は約909名に達し、敷地内には東京衛生アドベンチスト病院や付属のクリニック、三育学院大学東京校舎なども併設されています。<br>
          100年以上にわたり、地域と共に歩んできた天沼教会は、創立当初からの使命と伝統を受け継ぎつつ、現在も活発に活動を続けています。
        </p>
      </div>
    </section>
    <section class="section-5">
      <div class="text-section-5">
        <p>
          <span class="typewrite">天沼教会は同じ敷地にある</span><br>
          <span class="typewrite">東京衛生アドベンチスト病院や</span><br>
          <span class="typewrite"> 教会関連施設と隣接しており、</span><br>
          <span class="typewrite">教会の建物はそれらと中庭や通路で</span><br>
          <span class="typewrite">つながっています。</span><br>
          <span class="typewrite">教会と病院を結ぶ通りは「教会通り」</span><br>
          <span class="typewrite">と呼ばれ、そこに面した一角には</span><br>
          <span class="typewrite">教会関係のクリニックも</span><br>
          <span class="typewrite">併設されています。</span><br>
          <span class="typewrite">天沼教会は礼拝の場であると同時に、</span><br>
          <span class="typewrite">医療・教育施設が一体となった</span><br>
          <span class="typewrite">アドベンチストセンターの役割も果たす</span><br>
          <span class="typewrite">特色あるロケーションにあります。</span>
        </p>
      </div>
      <div class="commerce-street">
        <img src="@/assets/img/Commerce_street_buildings_1.svg" class="commerce-street-buildings" id="building-1"
          style="z-index: 5;">
        <img src="@/assets/img/Commerce_street_buildings_2.svg" class="commerce-street-buildings" id="building-2"
          style="z-index: 6;">
        <img src="@/assets/img/Commerce_street_buildings_3.svg" class="commerce-street-buildings" id="building-3"
          style="z-index: 7;">
        <img src="@/assets/img/Commerce_street_buildings_4.svg" class="commerce-street-buildings" id="building-4"
          style="z-index: 8;">
        <img src="@/assets/img/Commerce_street.svg" style="width: 100%;z-index: 0;">
      </div>
    </section>
    <section class="section-6">
      <div class="section-6-text">
        <p>
          教会のミッションは神の愛を実践することにあります。聖書が示す神様の無償の愛と救いのメッセージをすべての人に伝えるとともに、その愛を地域社会のニーズに応える様々な活動を通して具体的に表すことを目指しています。
          これはイエス・キリストが示された愛の模範に倣うものであり、天沼教会では礼拝や伝道のみならず、教育、医療、福祉、ボランティア活動など多方面での奉仕を大切にしています。
        </p>
      </div>
      <div class="hospital">
        <img src="@/assets/img/Hospital_bg.svg" class="commerce-street-buildings" id="hospital-bg" style="z-index: 0;">
        <img src="@/assets/img/Hospital.svg" class="commerce-street-buildings" id="hospital" style="z-index: 1;">
        <img src="@/assets/img/Hospital_grass.svg" class="commerce-street-buildings" id="hospital-grass"
          style="z-index: 2;">

        <div class="hospital-tree-wrapper">
          <div class="Hospital-tree">
            <svg ref="hospitalTreeSvg" id="hospitalTreeSvg" width="100%" viewBox="0 0 800 797">

              <defs>
                <mask id="m1" maskUnits="userSpaceOnUse" x="0" y="0" width="800" height="797">
                  <rect id="TreeWrapper" x="121.717" y="350" width="510.277" height="300" fill="#fff" />
                </mask>
              </defs>

              <g mask="url(#m1)">
                <image ref="hospitalTree" :href="hospitalTrees" width="800" height="797" transform="translate(0,270)" />
              </g>
            </svg>

          </div>
        </div>
      </div>
    </section>
    <section class="section-7">
      <div class="section-7-text">
        <p>
          天沼教会は、セブンスデー・アドベンチスト教会の一員として聖書に基づくキリスト教信仰を守り伝えています。その信仰の中心的価値観は、「聖書のみ」を信仰と実践の基準とし、イエス・キリストによる救いを信じてその恵みに生きることです。
          私たちは週の第七日である土曜日を聖なる安息日として重んじ、創造主なる神を礼拝します。また、主イエス・キリストがやがて再びこの地上に来られる（再臨される）という聖書の約束を堅く信じ、その希望を抱いて日々の歩みを続けています。
          天沼教会のメンバーは老若男女問わず、この希望に満ちた信仰によって互いに励まし合い、支え合っています。
        </p>
      </div>
      <div class="church-outside">
        <img src="@/assets/img/ChurchBackground.png" style="z-index: 1;">
        <img src="@/assets/img/Church_outside.svg" id="church-outside" style="z-index: 2;">
      </div>
      <div id="transition-section-7-8"></div>
    </section>
    <section class="section-8">
      <div class="section-8-text">
        <p>天沼教会では、毎週土曜日（安息日）を中心に様々な定例集会やプログラムが行われています。初めての方でも参加しやすいよう案内役のスタッフも配置されており、教会員と来訪者がともに交われる温かな雰囲気づくりがされています。
        </p>
      </div>
      <div class="church-inside">
        <img src="@/assets/img/ChurchInside.svg">
      </div>
    </section>
  </div>
</template>

<script>
import hospitalTrees from '@/assets/img/Hospital_trees.svg';
const STAR_MARKUP = `
  <svg width="10" height="10" xmlns="http://www.w3.org/2000/svg"
       style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:2;">
    <g transform="translate(-292.448 -219.083)">
      <g transform="translate(0 104.416)">
        <path d="M297.378 114.667L298.484 118.074L302.066 118.074
                 L299.168 120.179L300.275 123.585L297.378 121.48
                 L294.48 123.585L295.587 120.179L292.69 118.074
                 L296.271 118.074L297.378 114.667Z" fill="white"/>
      </g>
    </g>
  </svg>`;

export default {
  name: 'AboutChurchView',
  data() {
    return {
      /* star config */
      STAR_COUNT: 50,

      /* scroll-animation magic numbers */
      INITIAL_POSITION: 270,
      CENTER_X: 0,
      START_ANIM_OFFSET: 0,
      SCROLL_POS_OFFSET: -370,
      MASK_BOTTOM: 398.5 + 300,

      /* refs we’ll stash after mount */
      hospitalTreeSvgEl: null,
      hospitalTreeEl: null,
      hospitalTrees,
    };
  },
  setup() {
  },
  mounted() {
    /* 1. create star fields */
    this.populateStars(this.$refs.starsContainer, this.STAR_COUNT, 0, 100);
    this.populateStars(
      this.$refs.starsBehindMountainsContainer,
      this.STAR_COUNT,
      0,
      40
    );

    /* 2. cache refs for scroll handler */
    this.hospitalTreeSvgEl = this.$refs.hospitalTreeSvg;
    this.hospitalTreeEl = this.$refs.hospitalTree;

    /* 3. hook scroll */
    window.addEventListener('scroll', this.handleScroll, { passive: true });
    this.handleScroll(); // run once in case user’s mid-page
  },

  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll);
  },

  /* ——————————————————
     Methods
     —————————————————— */
  methods: {
    /* create one star container */
    populateStars(container, count, minTop, maxTop) {
      if (!container) return;

      for (let i = 0; i < count; i++) {
        const star = document.createElement('div');
        star.className = 'star';

        /* random positioning */
        star.style.left = `${Math.random() * 95}%`;
        star.style.top = `${Math.random() * (maxTop - minTop) + minTop}%`;

        /* random visual tweaks */
        star.style.setProperty('--size', `${Math.random() * 20 + 10}px`);
        star.style.setProperty('--duration', `${Math.random() * 2 + 2}s`);
        star.style.setProperty('--opacity', Math.random() * 0.6 + 0.4);
        star.style.setProperty('--delay', `${Math.random() * 2}s`);

        star.innerHTML = STAR_MARKUP;
        container.appendChild(star);
      }
    },

    /* main scroll-driven animation */
    handleScroll() {
      const svgEl = this.hospitalTreeSvgEl;
      const treeEl = this.hospitalTreeEl;
      if (!svgEl || !treeEl) return;

      const viewportH = window.innerHeight;
      const rect = svgEl.getBoundingClientRect();
      const startAnim = rect.top + this.MASK_BOTTOM;

      if (startAnim <= viewportH - this.SCROLL_POS_OFFSET && rect.bottom >= 0) {
        const newY =
          (this.INITIAL_POSITION +
            rect.top +
            this.SCROLL_POS_OFFSET +
            this.START_ANIM_OFFSET) *
          2;

        if (newY > 0) {
          treeEl.setAttribute('transform', `translate(${this.CENTER_X} ${newY})`);
        }
      } else {
        /* reset when SVG is out of view */
        treeEl.setAttribute(
          'transform',
          `translate(${this.CENTER_X} ${this.INITIAL_POSITION})`
        );
      }
    },
  },
};
</script>
