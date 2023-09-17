<template>
  <div class="d-flex flex-column" id="content-wrapper">
    <div id="page-top">
      <section
        class="contact-clean p-4"
      >
        <div class="row justify-content-center p-5">
          <div class="col-12 col-md-12 col-lg-10 col-xl-6 mb-3">
            <form
              class="bg-white shadow-sm p-4"
              @submit.prevent="submit"
            >
              <h2 class="text-center mb-4">お知らせ</h2>
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
                <label class="form-label">画像</label>
                <div>
                  <input type="file" ref="fileInput" />
                </div>
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
            <div class="col-12 col-md-12 col-lg-10 col-xl-6">
              <div
                class="bg-white shadow-sm mb-2 text-center p-3"
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
                class="row bg-white shadow-sm mb-3 mx-2 p-4 pb-2"
              >
                <div class="col-10">
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
                  <div v-if="news.image" class="form-group mb-3">
                    <label class="form-label">
                      <img :src="'http://localhost/api' + news.image"
                      class="img-thumbnail img-fluid"
                      loading="lazy">
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
                <div class="col-2 text-end">
                  <button @click="deleteNewsItem(news.id)" class="btn btn-light">
                    <svg class="bi bi-trash" xmlns="http://www.w3.org/2000/svg" width="1.2em" height="1.2em" fill="currentColor" viewBox="0 0 16 16">
                        <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6Z"></path>
                        <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1ZM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118ZM2.5 3h11V2h-11v1Z"></path>
                    </svg>
                  </button>
                </div>
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
import { useNewsStore } from '@/stores/news'

export default {
  name: 'NewsView',
  data: () => {
    return {
      loading: true,
    }
  },
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
    ...mapActions(useNewsStore, ['fecthNewsList', 'postNews', 'deleteNews']),
    async submit() {

      const fileInput = this.$refs.fileInput.files[0];
      const formData = new FormData();
      formData.append('date', this.date);
      formData.append('title', this.title);
      formData.append('author', this.author);
      formData.append('content', this.content);
      formData.append('image', fileInput);
      formData.append('links', JSON.stringify([{ url: this.link, text: this.textLink }]));

      await this.postNews(formData);
      await this.fecthNewsList(10)
    },
    async deleteNewsItem(id){
      await this.deleteNews(id);
      await this.fecthNewsList()
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
