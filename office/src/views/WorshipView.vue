<template>
    <div class="d-flex flex-column" id="content-wrapper">
      <div id="page-top">
        <section
          class="contact-clean p-4"
        >
          <div class="row justify-content-center p-5">
            <div class="col-12 mb-3">
              <form
                v-for="info in worshipInfos"
                class="bg-white shadow-sm p-4"
                @submit.prevent="submit"
              >
                <h3 class="text-center mb-4">{{ info.name }}</h3>
                <hr>
                <div v-for="event in info.events" class="form-group mb-3">
                    <label class="form-label">{{ event.name }}</label>
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
                                                <input class="form-control" type="time" v-model="event.startTime">
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
                                                <input class="form-control" type="time" v-model="event.endTime">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div v-for="(subEvent, index) in event.subEvents" class="d-flex mb-2">
                                <div class="col-6">
                                    <div class="row">
                                        <div class="d-flex">
                                            <div class="d-flex align-items-center me-2">
                                                <span>行事/詳細</span>
                                            </div>
                                            <div class="col-9 me-2">
                                                <input class="form-control" type="text" placeholder="行事名" v-model="subEvent.name"/>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-5">
                                    <div class="row">
                                        <div class="d-flex">
                                            <div class="d-flex align-items-center me-2">
                                                <span>担当者</span>
                                            </div>
                                            <div class="col-9 me-2">
                                                <input class="form-control" type="text" placeholder="担当者名" v-model="subEvent.responsible"/>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-1">
                                    <div class="row">
                                        <div class="d-flex">
                                            <button type="button" @click="removeSubEvent(event, index)" class="btn btn-light">-</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-11 text-end">
                                    <button type="button" @click="addSubEvent(event)" class="btn btn-light">+</button>
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
                    <button class="ms-4 btn btn-primary" type="button">キャンセル</button>
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
  import { reactive } from 'vue';
  
  export default {
    name: 'NewsView',
    data: () => {
      return {
        loading: true,
      }
    },
    setup() {
  
      const worshipInfos = reactive([
        {
            id: '1',
            weekday: 'sat',
            name: '土曜日プログラム',
            events: [
                {
                    name: '安息日学校礼拝',
                    startTime: "09:00",
                    endTime: "12:00",
                    subEvents: [{
                        name: '司会',
                        responsible: '司会者さん'
                    }]
                },
                {
                    name: '休憩',
                    startTime: "10:40",
                    endTime: "10:50"
                },
                {
                    name: '教会発表',
                    startTime: "10:50",
                    endTime: "11:00"
                },
                {
                    name: '礼拝',
                    startTime: "09:00",
                    endTime: "12:00",
                    subEvents: [{
                        name: '安息日学校',
                        responsible: '近藤先生'
                    }]
                }
            ]
        }
      ]);
  
      return {
        worshipInfos
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
  
        const fileInput = this.$refs.fileInput.files?.[0];
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
      addSubEvent(event){
        if(!event.subEvents){
            event.subEvents = []
        }
        event.subEvents.push({name:'', responsible: ''})
      },
      removeSubEvent(event, index){
        if (event.subEvents && index > -1 && index < event.subEvents.length) {
            event.subEvents.splice(index, 1);
        }
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
  