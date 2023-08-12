import axios from 'axios'
import { defineStore } from 'pinia'
import { News } from '@/types/news'

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
        .get(`http://localhost:8100/api/news/?limit=${length ?? '10'}`)
        .then(({ data }) => {
          this.newsList = data
        })
    },
  },
})