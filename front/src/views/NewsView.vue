<template>
  <div id="header-margin"></div>
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
      <template v-if="newsList.length">
        <template v-for="(news, index) in newsList" :key="index">
          <div
              :class="{'reverse': index % 1 === 0}"
               class="row d-flex mx-auto pb-4 mb-4 news">
            <div 
              :class="news.image ? 'col-lg-7' : 'col-lg-12'"
              class="col-lg-7 h-100">
              <div class="row">
                <div class="col">
                  <div><span class="badge bg-primary mb-2">{{ news.date }}</span></div>
                </div>
              </div>
              <div class="row">
                <div class="col">
                  <h5 class="fs-3 fw-bold mb-4">
                    <strong>{{ news.title }}</strong>
                  </h5>
                  <p class="text-muted">
                    {{ news.content }}
                  </p>
                  <span class="d-flex justify-content-lg-end author">
                    <br />
                    <span style="color: rgb(119, 119, 119)">
                      {{ news.author }}
                    </span
                    >
                  </span>
                </div>
              </div>
              <!-- Large Screen -->
              <div class="row d-none d-lg-flex">
                <div class="col">
                  <ul class="list-group mt-2">
                    <template v-for="link in news.links">
                      <li v-if="link.text" class="list-group-item btn btn-primary mb-2">
                        <a :href="getLink(link.url)">{{ link.text }}</a>
                      </li>
                    </template>
                  </ul>
                </div>
              </div>
            </div>
            <div
              v-if="news.image"
              :class="{'text-center justify-content-md-center order-lg-first my-4': index % 2 === 0}"
              class="col-12 col-lg-5 d-flex justify-content-md-center m-lg-auto pt-4"
            >
              <div class="row">
                <div class="col">
                  <img
                    class="img-thumbnail img-fluid"
                    :src="consts.IMAGE_URL + news.image"
                    loading="lazy"
                  />
                </div>
              </div>
            </div>
            <!-- Small Screen -->
            <div 
              v-if="news.image" class="col-lg-7 d-lg-none">
              <div class="row">
                <div class="col">
                  <ul class="list-group mt-2">
                    <li v-for="link in news.links" class="list-group-item btn btn-primary mb-2">
                      <a :href="getLink(link.url)">{{ link.text }}</a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </template>
      </template>
    </div>
  </section>
</template>

<script>
import { mapActions, mapState } from 'pinia'
import { useNewsStore } from '@/stores/news'
import consts from '@/consts/consts'

export default {
  name: 'NewsView',
  data: () => {
    return {
      loading: true,
    }
  },
  async mounted() {
    this.loading = true
    await this.fecthNewsList()
    this.loading = false
  },
  methods: {
    ...mapActions(useNewsStore, ['fecthNewsList']),
    getLink(url){
      if (!url)
        return
      if (url.startsWith('https://'))
        return url
      return "https://" + url
    },
  },
  computed: {
    ...mapState(useNewsStore, ['newsList', 'errors']),
  },
}
</script>
