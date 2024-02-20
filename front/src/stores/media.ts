import axios from 'axios'
import { defineStore } from 'pinia'
import consts from '@/consts/consts.ts'

interface ModuleState {
  youtube: []
}

export const useYoutubeStore = defineStore('youtube', {
  state: (): ModuleState => ({
    youtube: [],
  }),
  actions: {
    fetchYoutubeInfo() {
      return axios
        .get(`${consts.BASE_URL}/youtube`)
        .then(({ data }) => {
            for (const d of data) {
                const thumbnail = d.thumbnail_url
                const title = d.title
                const videoId = d.video_id
                this.youtube.push({thumbnail, title, videoId})
            }
        })
    },
  },
})
