import axios from 'axios'
import { defineStore } from 'pinia'
import { News } from '@/types/news'
import consts from '@/consts/consts.ts'

interface ModuleState {
  newsList: News[]
  errors: any
}

export const useNewsStore = defineStore('news', {
  state: (): ModuleState => ({
    newsList: [],
    errors: {},
  }),
  actions: {
    fecthNewsList(length: number) {
      return axios
        .get(`${consts.BASE_URL}/news/?limit=${length ?? '10'}`)
        .then(({ data }) => {
          this.newsList = data
        })
    },
    postNews(payload: any) {
      return axios
        .post(`${consts.BASE_URL}/news/`, payload)
        .then(({ data }) => {
          this.errors = {}
        })
        .catch((err) => {
          this.errors = err.response.data
        })
    },
    deleteNews(id: number) {
      return axios
        .delete(`${consts.BASE_URL}/news/${id}/`)
        .then(({ data }) => {
          this.errors = {}
        })
        .catch((err) => {
          this.errors = err.response.data
        })
    }
  },
})
