<template>
    <div class="d-flex flex-column" id="content-wrapper">
      <div id="page-top">
        <section
          class="contact-clean p-4"
        >
          <div class="row justify-content-center p-5">
            <div class="col-12 mb-3">
              <form
                class="bg-white shadow-sm p-4"
                @submit.prevent="submit"
              >
                <h3 class="text-center mb-4">土曜日プログラム</h3>
                <hr>
                <div class="form-group mb-3">
                    <label class="form-label">安息日学校</label>
                    <div class="row mb-2 ms-3">
                        <div class="col-12">
                            <div class="d-flex mb-2">
                                <div class="col-6">
                                    <div class="row">
                                        <div class="d-flex">
                                            <div class="d-flex align-items-center me-2">
                                                <span>開始時間</span>
                                            </div>
                                            <div class="col-9 me-2">
                                                <input class="form-control" type="time">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-6">
                                    <div class="row">
                                        <div class="d-flex">
                                            <div class="d-flex align-items-center me-2">
                                                <span>終了時間</span>
                                            </div>
                                            <div class="col-9 me-2">
                                                <input class="form-control" type="time">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-1">
                                    行事
                                </div>
                                <div class="col-4">
                                    <input class="form-control" type="text" placeholder="行事名"/>
                                </div>
                                <div class="col-2">
                                    担当者
                                </div>
                                <div class="col-4">
                                    <input class="form-control" type="text" placeholder="担当者名"/>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="form-group mb-3">
                  <label class="form-label">休憩</label>
                    <div class="row mb-2 ms-3">
                        <div class="col-12">
                            <div class="d-flex mb-2">
                                <div class="col-6">
                                    <div class="row">
                                        <div class="d-flex">
                                            <div class="d-flex align-items-center me-2">
                                                <span>開始時間</span>
                                            </div>
                                            <div class="col-9 me-2">
                                                <input class="form-control" type="time">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-6">
                                    <div class="row">
                                        <div class="d-flex">
                                            <div class="d-flex align-items-center me-2">
                                                <span>終了時間</span>
                                            </div>
                                            <div class="col-9 me-2">
                                                <input class="form-control" type="time">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="form-group mb-3">
                  <label class="form-label">教会発表</label>
                    <div class="row mb-2 ms-3">
                        <div class="col-12">
                            <div class="d-flex mb-2">
                                <div class="col-6">
                                    <div class="row">
                                        <div class="d-flex">
                                            <div class="d-flex align-items-center me-2">
                                                <span>開始時間</span>
                                            </div>
                                            <div class="col-9 me-2">
                                                <input class="form-control" type="time">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-6">
                                    <div class="row">
                                        <div class="d-flex">
                                            <div class="d-flex align-items-center me-2">
                                                <span>終了時間</span>
                                            </div>
                                            <div class="col-9 me-2">
                                                <input class="form-control" type="time">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="form-group mb-3">
                    <label class="form-label">礼拝</label>
                    <div class="row mb-2 ms-3">
                        <div class="col-12">
                            <div class="d-flex mb-2">
                                <div class="col-6">
                                    <div class="row">
                                        <div class="d-flex">
                                            <div class="d-flex align-items-center me-2">
                                                <span>開始時間</span>
                                            </div>
                                            <div class="col-9 me-2">
                                                <input class="form-control" type="time">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-6">
                                    <div class="row">
                                        <div class="d-flex">
                                            <div class="d-flex align-items-center me-2">
                                                <span>終了時間</span>
                                            </div>
                                            <div class="col-9 me-2">
                                                <input class="form-control" type="time">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="d-flex mb-2">
                                <div class="col-6">
                                    <div class="row">
                                        <div class="d-flex">
                                            <div class="d-flex align-items-center me-2">
                                                <span>行事</span>
                                            </div>
                                            <div class="col-9 me-2">
                                                <input class="form-control" type="text" placeholder="行事名"/>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-6">
                                    <div class="row">
                                        <div class="d-flex">
                                            <div class="d-flex align-items-center me-2">
                                                <span>担当者</span>
                                            </div>
                                            <div class="col-9 me-2">
                                                <input class="form-control" type="text" placeholder="担当者名"/>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="form-group mb-3">
                  <label class="form-label">画像</label>
                  <div>
                    <input type="file" ref="fileInput" />
                  </div>
                </div>
                <div class="form-group mb-3">
                  <button class="btn btn-primary" type="submit">保存</button>
                </div>
              </form>
            </div>
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
  