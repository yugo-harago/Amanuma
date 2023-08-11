<template>
  <div class="d-flex flex-column" id="content-wrapper">
    <div id="content">
      <section
        class="contact-clean"
        style="background: rgb(255, 255, 255); padding: 20px"
      >
        <div class="row justify-content-center p-5">
          <div class="col-12 col-md-12 col-lg-10 col-xl-6">
            <form
              class="bg-white shadow-sm"
              @submit.prevent="submit"
              style="background: rgb(248, 248, 249); padding: 20px"
            >
              <h2 class="text-center" style="margin-bottom: 20px">お知らせ</h2>
              <div class="form-group mb-3">
                <label class="form-label">日にち</label>
                <input class="form-control" v-model="date" type="date" />
              </div>
              <div class="form-group mb-3">
                <label class="form-label">タイトル</label>
                <input
                  class="form-control"
                  v-model="title"
                  type="text"
                  placeholder="タイトル"
                />
              </div>
              <div class="form-group mb-3">
                <label class="form-label">作者</label>
                <input
                  class="form-control"
                  v-model="author"
                  type="text"
                  placeholder="作者"
                />
              </div>
              <div class="form-group mb-3">
                <label class="form-label">記事</label>
                <textarea
                  class="form-control"
                  v-model="content"
                  placeholder="記事"
                  rows="5"
                ></textarea>
              </div>
              <div class="form-group mb-3">
                <label class="form-label">リンク</label>
                <div class="row">
                  <div class="col-5">
                    <input
                      class="form-control"
                      v-model="textLink"
                      type="text"
                      placeholder="テキストリンク"
                    />
                  </div>
                  <div class="col">
                    <input
                      class="form-control"
                      v-model="link"
                      type="text"
                      placeholder="リンク"
                    />
                  </div>
                </div>
              </div>
              <div class="form-group mb-3">
                <button class="btn btn-primary" type="submit">send</button>
              </div>
            </form>
          </div>
          <template v-if="!newsList.length">
            <div class="col-12 col-md-12 col-lg-10 col-xl-6 mt-2">
              <div
                class="bg-white shadow-sm mb-2 text-center"
                style="background: white; padding: 20px"
              >
                No data
              </div>
            </div>
          </template>
          <template v-else>
            <div
              class="col-12 col-md-12 col-lg-10 col-xl-6"
            >
              <div
                v-for="news in newsList"
                class="bg-white shadow-sm mb-2 mt-3"
                style="background: white; padding: 20px"
              >
                <div class="form-group mb-3">
                  <label class="form-label">{{ news.date }}</label>
                </div>
                <div class="form-group mb-3">
                  <label class="form-label">{{ news.title }}</label>
                </div>
                <div class="form-group mb-3">
                  <label class="form-label">{{ news.author }}</label>
                </div>
                <div class="form-group mb-3">
                  <label class="form-label">
                    {{ news.content }}
                  </label>
                </div>
                <template v-for="link in news.links">
                  <div v-if="link.text" class="form-group mb-3">
                    <label class="form-label">
                      <a :href="getLink(link.url)">{{ link.text }}</a>
                    </label>
                  </div>
                </template>
              </div>
            </div>
          </template>
        </div>
      </section>
    </div>
    <footer class="bg-white sticky-footer">
      <div class="container my-auto">
        <div class="text-center my-auto copyright">
          <span>Copyright © Brand 2023</span>
        </div>
      </div>
    </footer>
  </div>
  <a class="border rounded d-inline scroll-to-top" href="#page-top"
    ><i class="fas fa-angle-up"></i
  ></a>
</template>
<script>
import { mapActions, mapState } from 'pinia'
import { ref } from 'vue'
import { useNewsStore } from '../stores/news'

export default {
  name: 'NewsView',
  // data: () => {
  //   return {
  //     loading: true,
  //   }
  // },

  setup() {
    const date = ref('')
    const title = ref('')
    const author = ref('')
    const content = ref('')
    const textLink = ref('')
    const link = ref('')

    return {
      date,
      title,
      author,
      content,
      textLink,
      link,
    }
  },
  async mounted() {
    this.loading = true
    await this.fecthNewsList()
    this.loading = false
  },
  methods: {
    ...mapActions(useNewsStore, ['fecthNewsList', 'postNews']),
    async submit() {

      const news = {
        date: this.date,
        title: this.title,
        author: this.author,
        content: this.content,
        links: [{ url: this.link, text: this.textLink }],
      };
      await this.postNews(news)
      await this.fecthNewsList(10)
    },
    getLink(url){
      if (!url)
        return
      if (url.startsWith('https://'))
        return url
      return "https://" + url
    }
  },
  computed: {
    ...mapState(useNewsStore, ['newsList', 'errors']),
  },
}
</script>
